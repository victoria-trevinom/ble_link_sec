
"""Envio y recepcion de mensajes mediante Bluetooth BLE.

Librerias utilizadas:
- asyncio: incluida en Python.
- binascii: incluida en Python.
- bleak: instalar con pip install bleak.

Receptor: iPhone con LightBlue y dispositivo virtual Blank.
"""

import asyncio
import binascii

from bleak import BleakClient, BleakScanner


UUID = "00002222-0000-1000-8000-00805f9b34fb"

MENSAJE = (
    "Hola, este mensaje fue enviado desde mi ThinkPad "
    "a mi iPhone mediante Bluetooth BLE."
)

INICIO = bytes.fromhex("AA55")


def crear_trama(mensaje):
    datos = mensaje.encode("utf-8")
    longitud = len(datos).to_bytes(2, "big")
    contenido = longitud + datos
    crc = binascii.crc_hqx(contenido, 0xFFFF).to_bytes(2, "big")

    return INICIO + contenido + crc


def verificar_trama(trama):
    if len(trama) < 6 or trama[:2] != INICIO:
        raise ValueError("Inicio de trama incorrecto")

    longitud = int.from_bytes(trama[2:4], "big")

    if len(trama) != longitud + 6:
        raise ValueError("Longitud incorrecta")

    contenido = trama[2:-2]
    crc = binascii.crc_hqx(contenido, 0xFFFF).to_bytes(2, "big")

    if trama[-2:] != crc:
        raise ValueError("Error de CRC-16")

    return trama[4:-2].decode("utf-8")


async def main():
    print("Buscando iPhone...")

    dispositivo = await BleakScanner.find_device_by_name(
        "Blank", timeout=15
    )

    if dispositivo is None:
        print("No se encontro el dispositivo")
        return

    trama = crear_trama(MENSAJE)

    async with BleakClient(dispositivo) as cliente:
        print("Conexion BLE exitosa")
        print("Mensaje original:", MENSAJE)
        print("Longitud de trama:", len(trama), "bytes")

        await cliente.write_gatt_char(UUID, trama, response=True)
        recibido = bytes(await cliente.read_gatt_char(UUID))

    mensaje_recibido = verificar_trama(recibido)

    print("Marcador de inicio: AA55")
    print("CRC-16 valido")
    print("Mensaje recibido:", mensaje_recibido)
    print("Mensajes identicos:", mensaje_recibido == MENSAJE)


if __name__ == "__main__":
    asyncio.run(main())
