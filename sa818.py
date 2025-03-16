#!/usr/bin/env python3
import argparse
import serial # type: ignore
import time
import re

# Parámetros de la conexión
SERIAL_PORT = "/dev/serial0"  # Cambia según tu configuración
BAUD_RATE = 9600
TIMEOUT = 2  # segundos

def send_command(ser, command):
    """
    Envía el comando ASCII al módulo y retorna la respuesta.
    """
    ser.write(command.encode('ascii'))
    time.sleep(0.5)
    response = ser.read_all().decode('ascii')
    return response

def get_module_info(ser):
    """
    Envía el comando AAFAA para obtener el nombre y modelo del módulo.
    """
    response = send_command(ser, "AAFAA")
    return response.strip()

def get_programmed_data(ser):
    """
    Envía el comando AAFA1 para leer los datos programados.
    Se descarta el prefijo 'AA' y se retorna la lista de valores.
    """
    response = send_command(ser, "AAFA1")
    if response.startswith("AA"):
        response = response[2:]
    response = response.strip()
    data_list = response.split(',')
    return data_list

def update_programmed_data(ser, data_list):
    """
    Envía el comando AAFA3 concatenado con la cadena de datos (todos los parámetros)
    para actualizar la configuración del módulo.
    """
    data_string = ",".join(data_list)
    command = "AAFA3" + data_string
    response = send_command(ser, command)
    return response.strip()

def validate_frequency(freq):
    """
    Valida que la frecuencia tenga el formato xxx.xxxx
    """
    pattern = r'^\d{3}\.\d{4}$'
    if not re.match(pattern, freq):
        raise argparse.ArgumentTypeError(f"Frecuencia '{freq}' no tiene el formato xxx.xxxx")
    return freq

def validate_subtone(st):
    """
    Valida que el subtono tenga el formato de uno a tres dígitos (xxx)
    """
    pattern = r'^\d{1,3}$'
    if not re.match(pattern, st):
        raise argparse.ArgumentTypeError(f"Subtono '{st}' no tiene el formato esperado (hasta 3 dígitos)")
    return st

def validate_squelch(sql):
    """
    Valida que el squelch tenga el formato de un dígito (x)
    """
    pattern = r'^\d$'
    if not re.match(pattern, sql):
        raise argparse.ArgumentTypeError(f"Squelch '{sql}' no tiene el formato x")
    return sql

def main():
    # Crear la tabla de correspondencias de tonos en 4 columnas
    tone_mapping = [
        "1: 67", "2: 71.9", "3: 74.4", "4: 77", "5: 79.7", "6: 82.5", "7: 85.4", "8: 88.5", "9: 91.5", "10: 94.8",
        "11: 97.4", "12: 100", "13: 103.5", "14: 107.2", "15: 110.9", "16: 114.8", "17: 118.8", "18: 123", "19: 127.3", "20: 131.8",
        "21: 136.5", "22: 141.3", "23: 146.2", "24: 151.4", "25: 156.7", "26: 162.2", "27: 167.9", "28: 173.8", "29: 179.9", "30: 186.2",
        "31: 192.8", "32: 203.5", "33: 210.7", "34: 218.1", "35: 225.7", "36: 233.6", "37: 241.8", "38: 250.3"
    ]
    # Dividir la lista en 4 columnas
    col1 = tone_mapping[:10]        # Ítems 1 a 10
    col2 = tone_mapping[10:20]        # Ítems 11 a 20
    col3 = tone_mapping[20:30]        # Ítems 21 a 30
    col4 = tone_mapping[30:40]        # Ítems 31 a 38

    tone_table = "Tabla de correspondencias de tonos analógicos (solo información):\n"
    tone_table += "{:<15}{:<15}{:<15}{:<15}\n".format("Nº:Valor", "Nº:Valor", "Nº:Valor", "Nº:Valor")
    rows = max(len(col1), len(col2), len(col3), len(col4))
    for i in range(rows):
        c1 = col1[i] if i < len(col1) else ""
        c2 = col2[i] if i < len(col2) else ""
        c3 = col3[i] if i < len(col3) else ""
        c4 = col4[i] if i < len(col4) else ""
        tone_table += "{:<15}{:<15}{:<15}{:<15}\n".format(c1, c2, c3, c4)

    help_text = (
        "Programa para configurar el módulo walkie_SA828.\n\n"
        "Modo de uso:\n"
        " - Sin parámetros: muestra el nombre y modelo del módulo.\n"
        " - Con --ch: muestra la configuración actual del canal especificado (1-16).\n"
        " - Con --ch y parámetros de frecuencia/subtono: modifica la configuración del canal.\n\n"
        "Parámetros:\n"
        "  --port  : Puerto serie (default: /dev/serial0)\n"
        "  --ch    : Número de canal (1-16)\n"
        "  --tx    : Frecuencia de transmisión (formato xxx.xxxx)\n"
        "  --rx    : Frecuencia de recepción (formato xxx.xxxx)\n"
        "  --fr    : Asigna la misma frecuencia para TX y RX (formato xxx.xxxx)\n"
        "  --st    : Subtono para transmisión y recepción (formato xxx)\n"
        "  --stx   : Subtono de transmisión (formato xxx)\n"
        "  --srx   : Subtono de recepción (formato xxx)\n"
        "  --sql   : Squelch (formato x)\n\n"
    )
    full_help = help_text + tone_table + "\nVer tabla de correspondencia subtonos digitales en datasheet del SA828."

    parser = argparse.ArgumentParser(
        description=full_help,
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument("--port", type=str, default=SERIAL_PORT, help="Puerto serie (default: /dev/serial0)")
    parser.add_argument("--ch", type=int, help="Número de canal (1-16)")
    parser.add_argument("--tx", type=validate_frequency, help="Frecuencia de transmisión (formato xxx.xxxx)")
    parser.add_argument("--rx", type=validate_frequency, help="Frecuencia de recepción (formato xxx.xxxx)")
    parser.add_argument("--fr", type=validate_frequency, help="Asignar la misma frecuencia para TX y RX (formato xxx.xxxx)")
    parser.add_argument("--st", type=validate_subtone, help="Subtono para transmisión y recepción (formato xxx)")
    parser.add_argument("--stx", type=validate_subtone, help="Subtono de transmisión (formato xxx)")
    parser.add_argument("--srx", type=validate_subtone, help="Subtono de recepción (formato xxx)")
    parser.add_argument("--sql", type=validate_squelch, help="Squelch (formato x)")
    args = parser.parse_args()

    # Si se proporciona --fr, se asigna la misma frecuencia para TX y RX, sobreescribiendo si existían otros valores
    if args.fr:
        args.tx = args.fr
        args.rx = args.fr

    try:
        ser = serial.Serial(args.port, BAUD_RATE, timeout=TIMEOUT)
    except serial.SerialException as e:
        print("Error abriendo el puerto serie:", e)
        return

    # Sin canal, se muestra información del módulo
    if args.ch is None:
        info = get_module_info(ser)
        print("Información del módulo:", info)
        ser.close()
        return

    # Se obtiene la configuración programada
    data_list = get_programmed_data(ser)
    # Se espera recibir 35 valores: 32 para las frecuencias (16 canales TX y RX) + 3 (subtono TX, subtono RX y squelch)
    if len(data_list) < 35:
        print("Error: datos programados incompletos recibidos:", data_list)
        ser.close()
        return

    channel = args.ch
    if channel < 1 or channel > 16:
        print("Error: el canal debe estar entre 1 y 16.")
        ser.close()
        return

    # Cálculo de índices para TX y RX del canal
    tx_index = 2 * (channel - 1)
    rx_index = tx_index + 1

    current_tx = data_list[tx_index]
    current_rx = data_list[rx_index]
    tone_tx = data_list[32]   # Subtono TX
    tone_rx = data_list[33]   # Subtono RX
    squelch = data_list[34]

    # Mostrar la configuración actual del canal
    print(f"Canal {channel}:")
    print(f"  TX: {current_tx}")
    print(f"  RX: {current_rx}")
    print(f"  Subtono TX: {tone_tx}")
    print(f"  Subtono RX: {tone_rx}")
    print(f"  Squelch: {squelch}")

    # Se actualiza la configuración si se proporcionaron parámetros de modificación
    modified = False
    if args.tx:
        data_list[tx_index] = args.tx
        modified = True
    if args.rx:
        data_list[rx_index] = args.rx
        modified = True
    if args.st:
        data_list[32] = args.st
        data_list[33] = args.st
        modified = True
    if args.stx:
        data_list[32] = args.stx
        modified = True
    if args.srx:
        data_list[33] = args.srx
        modified = True
    if args.sql:
        data_list[34] = args.sql
        modified = True

    if modified:
        confirm = input("¿Desea actualizar la configuración en el módulo? (s/n): ")
        if confirm.lower() == 's':
            response = update_programmed_data(ser, data_list)
            print("Respuesta del módulo:", response)
        else:
            print("Actualización cancelada.")

    ser.close()

if __name__ == "__main__":
    main()
