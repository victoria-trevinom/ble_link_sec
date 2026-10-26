"""Módulo de interoperabilidad GATT y escaneo con Bleak."""
import asyncio
from bleak import BleakScanner, BleakClient


async def escanear_dispositivos(timeout: int = 5):
    """Escanea dispositivos Bluetooth Low Energy (BLE)."""
    dispositivos = await BleakScanner.discover(timeout=timeout)
    resultados = []
    for d in dispositivos:
        resultados.append({
            "nombre": d.name or "Desconocido",
            "direccion": d.address,
            "rssi": d.rssi,
        })
    return resultados


async def mantener_conexion(
    direccion_mac: str, uuid_caracteristica: str = None
):
    """Conecta a un dispositivo BLE y mantiene el

    enlace mediante notificaciones GATT.
    """
    def callback_notificacion(sender, data):
        print(f"[Datos recibidos de {sender}]: {data.hex()}")

    def callback_desconexion(client):
        print("[-] El dispositivo se ha desconectado.")

    async with BleakClient(
        direccion_mac,
        disconnected_callback=callback_desconexion
    ) as client:
        print(
            f"[+] Conectado exitosamente a {direccion_mac}. "
            "Manteniendo enlace..."
        )

        # Si el dispositivo tiene una característica
        # de notificación, nos suscribimos
        if uuid_caracteristica:
            try:
                await client.start_notify(
                    uuid_caracteristica, callback_notificacion
                )
                print("[+] Suscrito a notificaciones GATT.")
            except Exception as e:
                print(
                    "[-] No se pudo suscribir a "
                    f"la característica: {e}"
                )

        # Mantener el bucle abierto escuchando los eventos BLE
        while client.is_connected():
            await asyncio.sleep(1.0)

        if uuid_caracteristica:
            try:
                await client.stop_notify(uuid_caracteristica)
            except Exception:
                pass
