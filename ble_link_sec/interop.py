"""Módulo de interoperabilidad y
gestión de servicios GATT."""


class BLEInteropHandler:
    """Gestiona el intercambio de
    datos entre cliente y servidor."""

    def __init__(self, uuid_servicio: str):
        self.uuid_servicio = uuid_servicio
        self.conectado = False

    def establecer_conexion(self, direccion_mac: str) -> bool:
        """Establece la conexión lógica
        con el dispositivo remoto."""
        self.conectado = True
        return self.conectado

    def empaquetar_payload(self, mensaje: str) -> bytes:
        """Convierte texto en flujo
        de bytes para BLE."""
        return mensaje.encode("utf-8")
