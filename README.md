# Configuración del Módulo Wakie Talkie SA818

![Imagen del Módulo](https://cdn.tindiemedia.com/images/resize/TBo71vDup6BnSKvgnYHW_JFvgaI=/p/fit-in/400x266/filters:fill(fff)/i/9289/products/2022-10-26T06%3A41%3A47.032Z-SA828-05.jpg?1666741354)

Este proyecto es una aplicación en Python diseñada para modificar las frecuencias del módulo Wakie Talkie SA818, de la casa G-NiceRF, mediante conexión serie. Además de permitir consultar la información del módulo (nombre y modelo), también posibilita visualizar y actualizar la configuración de los canales (1-16) modificando las frecuencias, subtonos y el squelch.

Los subtonos y squelch son globales para todos los canales.

## Requisitos Previos
Antes de ejecutar la aplicación, asegúrese de tener instalado:
- **Python 3**
- **pyserial** (puede instalarlo con `pip install pyserial`)


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

Para obtener la información básica del módulo (nombre y modelo), simplemente ejecutar:

```bash
python3 sa818.py
```

### Consulta de la Configuración Actual de un Canal

Si deseas ver la configuración de un canal específico (del 1 al 16), usa el parámetro `--ch`:

```bash
python3 sa818.py --ch 1
```

Se mostrará la configuración actual del canal, que incluye las frecuencias, subtonos y el valor del squelch. (Subtonos y squelch son gobales a todos los canales)

### Modificación de la Configuración de un Canal

Para modificar la configuración, se deben proporcionar los siguientes argumentos junto con el número de canal (`--ch`):

- **Puerto Serie:**
  - `--port` : Puerto serie (default: `/dev/serial0`)
  
- **Canal:**
  - `--ch`   : Número de canal (1-16)
  
- **Frecuencias:**
  - `--fr`   : Asigna la misma frecuencia para TX y RX (formato `xxx.xxxx`)
  - `--tx`   : Frecuencia de transmisión (formato `xxx.xxxx`)
  - `--rx`   : Frecuencia de recepción (formato `xxx.xxxx`)
    
- **Subtonos:**
  - `--st`   : Subtono para transmisión y recepción (formato 3 dígitos, ej. `067`)
  - `--stx`  : Subtono de transmisión (formato 3 dígitos)
  - `--srx`  : Subtono de recepción (formato 3 dígitos)
  
- **Squelch:**
  - `--sql`  : Squelch (formato de un dígito, ej. `1`)

**Ejemplo 1:** Modificar las frecuencias TX y RX del canal 2, y asignar un subtono común:

```bash
python3 sa818.py --ch 2 --tx 123.4567 --rx 234.5678 --st 67
```

**Ejemplo 2:** Configurar el canal 3 para que la misma frecuencia sea asignada a TX y RX, y asignar un subtono:

```bash
python3 sa818.py --ch 3 --fr 345.6789 --st 71
```

Al ejecutar el script con parámetros de modificación, se mostrará la configuración que se va a guardar y se solicitará una confirmación para actualizar la configuración en el módulo.

## Tabla de Correspondencia de Tonos

- **Analógicos:**
1 |Data  Tono|Data  Tono|Data   Tono|Data   Tono|Data   Tono|Data   Tono|Data   Tono|
2 |----------|----------|-----------|-----------|-----------|-----------|-----------|
3 | 001 67   | 007 85.4 | 013 103.5 | 019 127.3 | 025 156.7 | 031 192.8 | 037 241.8 |
4 | 002 71.9 | 008 88.5 | 014 107.2 | 020 131.8 | 026 162.2 | 032 203.5 | 038 250.3 |
5 | 003 74.4 | 009 91.5 | 015 110.9 | 021 136.5 | 027 167.9 | 033 210.7 |           |
6 | 004 77   | 010 94.8 | 016 114.8 | 022 141.3 | 028 173.8 | 034 218.1 |           |
7 | 005 79.7 | 011 97.4 | 017 118.8 | 023 146.2 | 029 179.9 | 035 225.7 |           |
8 | 006 82.5 | 012 100  | 018 123   | 024 151.4 | 030 186.2 | 036 233.6 |           |

     

- **Digitales:**
 1 |Data  Tono|Data  Tono|Data  Tono|Data  Tono|Data  Tono|Data  Tono|Data  Tono|
 2 |----------|----------|----------|----------|----------|----------|----------|
 3 | 039 023I | 063 156I | 087 365I | 111 654I | 135 074N | 159 263N | 183 506N |
 4 | 040 025I | 064 162I | 088 371I | 112 662I | 136 114N | 160 265N | 184 516N |
 5 | 041 026I | 065 165I | 089 411I | 113 664I | 137 115N | 161 271N | 185 532N |
 6 | 042 031I | 066 172I | 090 412I | 114 703I | 138 116N | 162 306N | 186 546N |
 7 | 043 032I | 067 174I | 091 413I | 115 712I | 139 125N | 163 311N | 187 565N |
 8 | 044 043I | 068 205I | 092 423I | 116 723I | 140 131N | 164 315N | 188 606N |
 9 | 045 047I | 069 223I | 093 431I | 117 731I | 141 132N | 165 331N | 189 612N |
10 | 046 051I | 070 226I | 094 432I | 118 732I | 142 134N | 166 343N | 190 624N |
11 | 047 054I | 071 243I | 095 445I | 119 734I | 143 143N | 167 346N | 191 627N |
12 | 048 065I | 072 244I | 096 464I | 120 743I | 144 152N | 168 351N | 192 631N |
13 | 049 071I | 073 245I | 097 465I | 121 754I | 145 155N | 169 364N | 193 632N |
14 | 050 072I | 074 251I | 098 466I | 122 023N | 146 156N | 170 365N | 194 654N |
15 | 051 073I | 075 261I | 099 503I | 123 025N | 147 162N | 171 371N | 195 662N |
16 | 052 074I | 076 263I | 100 506I | 124 026N | 148 165N | 172 411N | 196 664N |
17 | 053 114I | 077 265I | 101 516I | 125 031N | 149 172N | 173 412N | 197 703N |
18 | 054 115I | 078 271I | 102 532I | 126 032N | 150 174N | 174 413N | 198 712N |
19 | 055 116I | 079 306I | 103 546I | 127 043N | 151 205N | 175 423N | 199 723N |
20 | 056 125I | 080 311I | 104 565I | 128 047N | 152 223N | 176 431N | 200 731N |
21 | 057 131I | 081 315I | 105 606I | 129 051N | 153 226N | 177 432N | 201 732N |
22 | 058 132I | 082 331I | 106 612I | 130 054N | 154 243N | 178 445N | 202 734N |
23 | 059 134I | 083 343I | 107 624I | 131 065N | 155 244N | 179 464N | 203 743N |
24 | 060 143I | 084 346I | 108 627I | 132 071N | 156 245N | 180 465N | 204 754N |
25 | 061 152I | 085 351I | 109 631I | 133 072N | 157 251N | 181 466N |          |
26 | 062 155I | 086 364I | 110 632I | 134 073N | 158 261N | 182 503N |          |




## Contribuciones y Licencia

Las contribuciones son bienvenidas. Si deseas mejorar este proyecto o reportar errores, por favor abre un *issue* o envía un *pull request*.



---


