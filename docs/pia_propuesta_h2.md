# PIA - H2: Propuesta y primera señal (Parte 2 de 6)

**Universidad Autónoma de Nuevo León**  
**Facultad de Ciencias Físico Matemáticas**  
**Asignatura:** Señales de Transmisión  
**Docente:** Guillermo Ezequiel Sánchez Guerrero  
**Fecha:** 16 de Octubre de 2026  

---

### Datos del Equipo (Grupo D)
| Nombre Completo | Matrícula | Correo Universitario | Rol en el Equipo |
| :--- | :---: | :---: | :--- |
| **Victoria Treviño Martínez** | 2225372 | victoria.trevinom@uanl.edu.mx | Investigadora (Marco Teórico, Gráficas y Desarrollo) y Programadora |
| **Marco Antonio Rivera Moreno** | 2119040 | marco.riveram@uanl.edu.mx | Verificador (Protocolos y Pruebas de Seguridad) |
| **Fabian Solis Flores Rangel** | 2159498 | fabian.floresr@uanl.edu.mx | Programador Principal (Implementación y Cifrado) |
| **Luis Eduardo Téllez García** | 2154647 | eduardo.tellezg@uanl.edu.mx | Analista Cuantitativo (Cálculos Matemáticos y Tasa de Bits) y Finanzas |

---

## 1. Propuesta Técnica del Enlace (C1)

### 1.1 Medio Seleccionado
- **Medio:** Bluetooth Low Energy (BLE) / Bluetooth (Teléfono ↔ Laptop).

### 1.2 Montaje del Enlace (Diagrama / Croquis)
## 1.1 Medio Seleccionado
* **Medio:** Bluetooth Low Energy (BLE) / Comunicación bidireccional (Teléfono Inteligente ⟷ Laptop).
* **Hardware de Interfaz:** Se utilizará el **adaptador Bluetooth interno** integrado de fábrica en la laptop (compatible con la capa BLE nativa del sistema operativo), evitando la necesidad de adquirir adaptadores o hardware externo adicional (costo cero).
* **Software de Adquisición:** Se empleará un **script de desarrollo propio en Python** utilizando la librería asíncrona `bleak`, el cual se encargará de establecer el enlace activo, escanear el entorno y registrar métricas de potencia de señal (RSSI).

## 1.2 Montaje del Enlace (Diagrama / Croquis y Software)

## 1.2 Montaje del Enlace (Diagrama / Croquis y Software)

## 1.2 Montaje del Enlace (Diagrama / Croquis y Software)

```mermaid
flowchart LR
    subgraph Emisor [Smartphone / Emisor BLE]
        A["📱 Dispositivo Móvil<br/>(Transmisor BLE 2.4 GHz)"]
    end

    subgraph Canal [Canal Inalámbrico RF]
        C1((( )))
        C2((( )))
        C3((( )))
    end

    subgraph Receptor [Laptop / Estación Base]
        B["💻 Adaptador Bluetooth Interno<br/>+ Script Python (Bleak)"]
    end

    A ==>|"🔵 Señal BLE<br/>(Distancia 'd')"| C1
    C1 ~~~ C2 ~~~ C3
    C3 ==>|"Métricas RSSI"| B

    style Canal fill:transparent,stroke:none
    style C1 fill:#e1f5fe,stroke:#0288d1,stroke-width:2px
    style C2 fill:#b3e5fc,stroke:#0288d1,stroke-width:2px
    style C3 fill:#81d4fa,stroke:#0288d1,stroke-width:2px
```

- **Descripción del Montaje:** El teléfono inteligente actúa como emisor enviando tramas de prueba por BLE en la banda de 2.4 GHz hacia la laptop (receptor). Ambos dispositivos se colocan en línea de vista directa a una distancia inicial $d_0 = 1.0\text{ m}$.

### 1.3 Fenómeno Físico y Variable de Estudio
- **Fenómeno Físico a Medir:** Atenuación de la potencia de la señal de radiofrecuencia (RF) recibida (RSSI en dBm) y pérdida por trayectoria en el canal inalámbrico.
- **Variable a Variar:** Distancia física ($d$) entre el emisor y el receptor (de $0.5\text{ m}$ a $5.0\text{ m}$ en incrementos de $0.5\text{ m}$).

### 1.4 Lista de Materiales y Costos
| Cantidad | Material / Componente | Función en el Montaje | Costo ($) |
| :---: | :--- | :--- | :---: |
| 1 | Smartphone con Bluetooth / BLE | Emisor de la señal / tramas de prueba | $0.00 (Propietario) |
| 1 | Laptop con adaptador BLE | Receptor y decodificador de datos | $0.00 (Propietario) |
| 1 | Cinta métrica / Flexómetro (5 m) | Medición precisa de la distancia del canal | $0.00 (Disponible) |
| 1 | Entorno Python (Librería Bleak) | Captura y procesamiento de tramas | $0.00 (Open Source) |
| **Total** | | | **$0.00 (Grupo A)** |

---

## 2. Evidencia de Primera Señal, Fuentes y Riesgos (C2)

### 2.1 Video Corto de la Primera Señal
- **Evidencia:** Recuperación exitosa de la primera señal (un bit o tono de prueba en el receptor que demuestra que el enlace está vivo).
- **Enlace al Video:** `[Insertar enlace de evidencia: Google Drive / OneDrive / YouTube]`

### 2.2 Fuentes Verificables (Formato IEEE)
---

## 1.4 Referencias Bibliográficas

[1] Bluetooth Special Interest Group (SIG), *Core Specification Version 5.3*, In-Halt: Vol. 6, Part B, 2021.
[2] Python Software Foundation, *Python 3 Documentation: asyncio — Asynchronous I/O*, Disponible en: https://docs.python.org/3/library/asyncio.html. [Accedido: Oct. 2026].
[3] C. Knight et al., *Bleak: Bluetooth Low Energy platform agnostics client for Python*, GitHub Repository, Disponible en: https://github.com/hbldh/bleak. [Accedido: Oct. 2026].
[4] W. Stallings, *Cryptography and Network Security: Principles and Practice*, 7va ed., Pearson, 2017.

### 2.3 Breve Análisis de Riesgos (Seguridad y Legalidad)

