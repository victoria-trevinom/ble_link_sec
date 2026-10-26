"""Transmision de mensajes mediante Bluetooth Low Energy.

Libreria externa: bleak.
Librerias incluidas en Python: asyncio y binascii.
Receptor: LightBlue en iPhone, dispositivo virtual Blank.
"""

import asyncio
import binascii
import time

from bleak import BleakClient, BleakScanner


UUID = "00002222-0000-1000-8000-00805f9b34fb"
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
        raise ValueError("Error en CRC-16")

    return trama[4:-2].decode("utf-8")


async def main():
    mensaje = input("Escribe el mensaje que quieres enviar: ")

    if len(mensaje) < 32:
        print("El mensaje debe tener al menos 32 caracteres")
        return

    print("Buscando dispositivo BLE...")

    dispositivo = await BleakScanner.find_device_by_name(
        "Blank", timeout=15
    )

    if dispositivo is None:
        print("No se encontro el dispositivo")
        return

    trama = crear_trama(mensaje)

    async with BleakClient(dispositivo) as cliente:
        print("Conexion BLE exitosa")
        print("Mensaje original:", mensaje)
        print("Bytes de trama:", len(trama))
        inicio = time.perf_counter()
        await cliente.write_gatt_char(UUID, trama, response=True)
        tiempo = time.perf_counter() - inicio
        print(f"Tiempo de escritura BLE: {tiempo:.6f} segundos")

        recibido = bytes(await cliente.read_gatt_char(UUID))

    mensaje_recibido = verificar_trama(recibido)

    print("Preambulo de aplicacion: AA55")
    print("CRC-16 valido")
    print("Mensaje recibido:", mensaje_recibido)
    print("Verificacion exitosa:", mensaje_recibido == mensaje)


if __name__ == "__main__":
    asyncio.run(main())
