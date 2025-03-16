# Configuración del Módulo Wakie Talkie SA818

![Imagen del Módulo](https://cdn.tindiemedia.com/images/resize/TBo71vDup6BnSKvgnYHW_JFvgaI=/p/fit-in/400x266/filters:fill(fff)/i/9289/products/2022-10-26T06%3A41%3A47.032Z-SA828-05.jpg?1666741354)

Este proyecto es una aplicación en Python diseñada para modificar las frecuencias del módulo Wakie Talkie SA818, de la casa G-NiceRF, mediante conexión serie. Además de permitir consultar la información del módulo (nombre y modelo), también posibilita visualizar y actualizar la configuración de los canales (1-16) modificando las frecuencias, subtonos y el squelch.

## Requisitos Previos

Para que la aplicación funcione correctamente, es imprescindible tener instalado el paquete **pyserial**.  
Puedes instalarlo fácilmente ejecutando:

```bash
pip install pyserial
```

## Descripción General

La aplicación se conecta al módulo mediante un puerto serie (por defecto `/dev/serial0`) y ofrece dos modos de operación:

1. **Visualización de Información del Módulo:**  
   Al ejecutar el script sin parámetros, se obtiene el nombre y modelo del módulo.

2. **Consulta y Modificación de la Configuración de un Canal:**  
   Al especificar el número de canal (entre 1 y 16) mediante el parámetro `--ch`, se muestra la configuración actual, la cual incluye:
   - Frecuencia de transmisión (TX)
   - Frecuencia de recepción (RX)
   - Subtono de transmisión (STX)
   - Subtono de recepción (SRX)
   - Squelch

   Además, se pueden actualizar los parámetros del canal usando los argumentos correspondientes.

## Uso y Parámetros

### Ejecución sin Parámetros

Para obtener la información básica del módulo (nombre y modelo), simplemente ejecuta:

```bash
./tu_script.py
```

### Consulta de la Configuración Actual de un Canal

Si deseas ver la configuración de un canal específico (del 1 al 16), usa el parámetro `--ch`:

```bash
./tu_script.py --ch 1
```

Se mostrará la configuración actual del canal, que incluye las frecuencias, subtonos y el valor del squelch.

### Modificación de la Configuración de un Canal

Para modificar la configuración, se deben proporcionar los siguientes argumentos junto con el número de canal (`--ch`):

- **Puerto Serie:**
  - `--port` : Puerto serie (default: `/dev/serial0`)
  
- **Canal:**
  - `--ch`   : Número de canal (1-16)
  
- **Frecuencias:**
  - `--tx`   : Frecuencia de transmisión (formato `xxx.xxxx`)
  - `--rx`   : Frecuencia de recepción (formato `xxx.xxxx`)
  - `--fr`   : Asigna la misma frecuencia para TX y RX (formato `xxx.xxxx`)
  
- **Subtonos:**
  - `--st`   : Subtono para transmisión y recepción (formato de hasta 3 dígitos, ej. `67`)
  - `--stx`  : Subtono de transmisión (formato de hasta 3 dígitos)
  - `--srx`  : Subtono de recepción (formato de hasta 3 dígitos)
  
- **Squelch:**
  - `--sql`  : Squelch (formato de un dígito, ej. `1`)

**Ejemplo 1:** Modificar las frecuencias TX y RX del canal 2, y asignar un subtono común:

```bash
./tu_script.py --ch 2 --tx 123.4567 --rx 234.5678 --st 67
```

**Ejemplo 2:** Configurar el canal 3 para que la misma frecuencia sea asignada a TX y RX, y asignar un subtono:

```bash
./tu_script.py --ch 3 --fr 345.6789 --st 71
```

Al ejecutar el script con parámetros de modificación, se mostrará primero la configuración actual del canal. Luego, se solicitará una confirmación para actualizar la configuración en el módulo.

## Tabla de Correspondencia de Tonos

El programa genera y muestra una tabla de correspondencias de tonos analógicos con 4 columnas. Esta tabla ofrece una referencia de los valores asociados a cada canal (números y tonos), aunque para información detallada se recomienda consultar el datasheet del SA828.

## Ejecución del Script

Asegúrate de que el script tenga permisos de ejecución y se encuentre en un entorno compatible con Python 3:

```bash
chmod +x tu_script.py
./tu_script.py [opciones]
```

## Contribuciones y Licencia

Las contribuciones son bienvenidas. Si deseas mejorar este proyecto o reportar errores, por favor abre un *issue* o envía un *pull request*.

*Agrega aquí la licencia de tu proyecto según corresponda.*

---

Este README.md proporciona una guía completa y profesional para la configuración y uso de la aplicación destinada a modificar las frecuencias del módulo Wakie Talkie SA818. ¡Gracias por utilizar y contribuir a este proyecto!

