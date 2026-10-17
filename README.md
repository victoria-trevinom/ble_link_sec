<h1>BLE Link Security Tool (ble_link_sec)</h1><p>Herramienta de analisis, caracterizacion y cifrado de enlace de capa fisica mediante Bluetooth Low Energy (BLE) entre dispositivos moviles y equipos portatiles.</p>2>Datos de los Integrantes (Equipo 06)</h2><table><thead><tr><th>Nombre Completo</th><th>Matricula</th><th>Carrera</th><th>Semestre</th><th>Grupo</th><th>Rol en el Equipo</th></tr></thead><tbody><tr><td>Victoria Trevino Martinez</td><td>2225372</td><td rowspan="4" align="center">LSTI / FCFM</td><td rowspan="4" align="center">3°</td><td rowspan="4" align="center">061</td><td>Investigadora y Programadora</td></tr><tr><td>Marco Antonio Rivera Moreno</td><td>2119040</td><td>Verificador</td></tr><tr><td>Fabian Solis Flores Rangel</td><td>2159498</td><td>Programador Principal</td></tr><tr><td>Luis Eduardo Tellez Garcia</td><td>2154647</td><td>Analista Cuantitativo y Finanzas</td></tr></tbody></table><hr/><h2>Estructura del Codigo Fuente</h2><ul><li><code>ble_link_sec/__init__.py</code>: Declaracion del modulo principal del paquete Python.</li><li><code>ble_link_sec/red.py</code>: Captura y procesamiento de tramas BLE (RSSI, anuncios GATT).</li><li><code>ble_link_sec/crypto.py</code>: Implementacion del cifrado XOR / One-Time Pad (OTP) y Hamming(7,4).</li><li><code>ble_link_sec/interop.py</code>: Modulo de interoperabilidad entre cliente BLE (Smartphone) y servidor BLE (Laptop).</li><li><code>main.py</code>: Interfaz de linea de comandos (CLI) construida mediante argparse.</li></ul><hr/><h2>Citacion del Codigo (Formato APA 7ma Edicion)</h2>1. Bleak (Libreria de comunicacion BLE en Python): Bleak Developers. (2023). Bleak: Bluetooth Low Energy platform Agnostic Klient for Python (Version 0.21.1) [Software de computación]. GitHub. https://github.com/hbldh/bleak<br/>2. Python Software Foundation (Logica del parser CLI): Python Software Foundation. (2026). argparse - Parser for command-line options, arguments and sub-commands (Python Standard Library v3.11) [Software de computacion]. https://docs.python.org/3/library/argparse.html<br/>3. Ejemplo de servidor GATT BLE: Blum, R. (2020). Python Bluetooth LE GATT Server Example [Codigo fuente]. https://github.com/hbldh/bleak/tree/develop/examples. 4 N. Pavur, R. A. Calvo, and J. A. Clark, "Security and Privacy Threats for Bluetooth Low Energy in IoT and Wearable Devices: A Comprehensive Survey," IEEE Xplore, [En línea]. Disponible en: https://ieeexplore.ieee.org/document/9706334 [Accedido: 15-oct-2026]. 5. M. Ryan, "Bluetooth: With Low Energy comes Low Security," in Proceedings of the 7th USENIX, [En línea]. Disponible en:
https://www.usenix.org/conference/woot13/workshop-program/presentation/ryan?hl=es-US/ [Accedido: 15-oct-2026].
6. Campus Ciberseguridad, "Seguridad de los dispositivos BLE," Campus Ciberseguridad, [En línea]. Disponible en: https://www.campusciberseguridad.com/blog-alumno/seguridad-de-los-dispositivos-ble/ [Accedido: 15-oct-2026].<hr/><h2>Instalacion y Uso</h2><pre>pip install -r requirements.txt`npython main.py --scan`npython main.py --receive</pre>



 ## Análisis de Riesgos y Legalidad


 - **Riesgos de Seguridad Técnico-Operativos:**
 -    **1. Intercepción de trafico** Dado que los dispositivos BLE se comunican en el canal inalámbrico, cualquier persona con un dispositivo de análisis de paquetes, como Ubertooth o SmartRF Sniffer, puede interceptar la comunicación. Se recomienda a los usuarios utilizar opciones de emparejamiento seguras, como la comparación numérica, el acceso fuera de rango o, al menos, la introducción de una clave de acceso.
-    **2. Ataques de Hombre en el Medio (MitM):** Aquí si el mecanismo de emparejamiento o vinculación es débil, un dispositivo malicioso puede suplantar la identidad de la laptop y/o celular y hasta modificar y alterar el flujo de datos.

## Reglas de Seguridad y Legalidad

- **Uso ético y autorizado:** Las herramientas y scripts desarrollados en este proyecto (como `test_ble.py`) están diseñados exclusivamente con fines académicos y de prueba en entornos controlados, utilizando dispositivos propios para validar conceptos de conectividad de bajo consumo (BLE).
- **Cumplimiento normativo:** Las pruebas de conectividad inalámbrica y la manipulación de interfaces de red deben realizarse respetando las normativas locales vigentes y los marcos regulatorios aplicables a las telecomunicaciones.
- **Privacidad de los datos:** Queda estrictamente prohibido el escaneo no autorizado, la captura de tráfico o la interacción maliciosa con dispositivos pertenecientes a terceros sin su consentimiento explícito.
- **Responsabilidad del usuario:** Los integrantes del equipo son responsables de garantizar que cualquier ejecución de código o prueba de concepto se realice de manera segura, evitando afectaciones a redes ajenas o equipos externos.
 - **

 ## 🚀 Guía Rápida: Cómo descargar y probar el enlace BLE

Si vas a probar el programa en tu computadora para verificar la comunicación con tu teléfono, sigue estos sencillos pasos:

### 1. Requisitos previos
* Tener Python instalado en tu computadora (asegúrate de marcar la casilla *"Add Python to PATH"* durante su instalación).
* Tener Git instalado (o puedes descargar este repositorio directamente como un archivo ZIP desde el botón verde **"Code"** arriba en GitHub y descomprimirlo en tu computadora).

### 2. Abrir la terminal
* Abre tu terminal de comandos (en Windows busca **PowerShell** o **Símbolo del sistema**).
* Colócate en la carpeta donde descargaste o clonaste el proyecto. Por ejemplo, si lo guardaste en tu Escritorio:
  ```bash
  cd Desktop/ble_link_sec
  ```

### 3. Instalar las herramientas necesarias
Ejecuta el siguiente comando para que la computadora descargue automáticamente las librerías que el programa utiliza (para la interfaz gráfica y el Bluetooth):
```bash
pip install -r requirements.txt
```

### 4. Ejecutar el programa
Entra a la carpeta del programa y lánzalo con este comando:
```bash
cd ble_link_sec/ble_link_sec
python test_ble.py
```

### 5. Cómo realizar la prueba del enlace en vivo
1. En tu teléfono celular, entra a **Ajustes > Bluetooth** y déjate en esa pantalla para que el dispositivo sea visible.
2. En la ventana que se abrió en la computadora, escribe el nombre exacto de tu celular en el espacio indicado.
3. Haz clic en el botón **"📡 Buscar y Conectar al Enlace"**.
4. La pantalla de la aplicación te mostrará el avance:
   * Encontrará la dirección MAC de tu teléfono.
   * Establecerá el enlace físico por Bluetooth de manera automática.
   * Solicitará los servicios remotos (`GATT`), mostrando en la consola de la app el mensaje de éxito de que **el bit y los datos del enlace ya están activos y fluyendo**.
5. Si llega a haber algún problema de conexión, solo haz clic en el botón **"💡 ¿Qué hacer si no se conecta?"** dentro de la misma aplicación para ver los consejos de solución paso a paso.
