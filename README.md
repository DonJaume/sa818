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
001 67      007 85.4    013 103.5   019 127.3   025 156.7   031 192.8   037 241.8
002 71.9    008 88.5    014 107.2   020 131.8   026 162.2   032 203.5   038 250.3
003 74.4    009 91.5    015 110.9   021 136.5   027 167.9   033 210.7
004 77      010 94.8    016 114.8   022 141.3   028 173.8   034 218.1
005 79.7    011 97.4    017 118.8   023 146.2   029 179.9   035 225.7
006 82.5    012 100     018 123     024 151.4   030 186.2   036 233.6
     

- **Digitales:**
039 023I 122 023N    051 073I 134 073N    063 156I 146 156N    075 261I 158 261N    087 365I 170 365N    099 503I 182 503N    111 654I    194 654N
040 025I 123 025N    052 074I 135 074N    064 162I 147 162N    076 263I 159 263N    088 371I 171 371N    100 506I 183 506N    112 662I    195 662N
041 026I 124 026N    053 114I 136 114N    065 165I 148 165N    077 265I 160 265N    089 411I 172 411N    101 516I 184 516N    113 664I    196 664N
042 031I 125 031N    054 115I 137 115N    066 172I 149 172N    078 271I 161 271N    090 412I 173 412N    102 532I 185 532N    114 703I    197 703N
043 032I 126 032N    055 116I 138 116N    067 174I 150 174N    079 306I 162 306N    091 413I 174 413N    103 546I 186 546N    115 712I    198 712N
044 043I 127 043N    056 125I 139 125N    068 205I 151 205N    080 311I 163 311N    092 423I 175 423N    104 565I 187 565N    116 723I    199 723N
045 047I 128 047N    057 131I 140 131N    069 223I 152 223N    081 315I 164 315N    093 431I 176 431N    105 606I 188 606N    117 731I    200 731N
046 051I 129 051N    058 132I 141 132N    070 226I 153 226N    082 331I 165 331N    094 432I 177 432N    106 612I 189 612N    118 732I    201 732N
047 054I 130 054N    059 134I 142 134N    071 243I 154 243N    083 343I 166 343N    095 445I 178 445N    107 624I 190 624N    119 734I    202 734N
048 065I 131 065N    060 143I 143 143N    072 244I 155 244N    084 346I 167 346N    096 464I 179 464N    108 627I 191 627N    120 743I    203 743N
049 071I 132 071N    061 152I 144 152N    073 245I 156 245N    085 351I 168 351N    097 465I 180 465N    109 631I 192 631N    121 754I    204 754N
050 072I 133 072N    062 155I 145 155N    074 251I 157 251N    086 364I 169 364N    098 466I 181 466N    110 632I 193 632N



## Contribuciones y Licencia

Las contribuciones son bienvenidas. Si deseas mejorar este proyecto o reportar errores, por favor abre un *issue* o envía un *pull request*.



---


