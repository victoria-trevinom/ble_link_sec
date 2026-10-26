"""Módulo de procesamiento de señales y modelo de atenuación BLE."""
import math


def calcular_distancia_rssi(
    rssi: float, rssi_1m: float = -60.0, n: float = 2.5
) -> float:
    """Calcula la distancia estimada usando el Log-Distance Path Loss Model."""
    return 10 ** ((rssi_1m - rssi) / (10 * n))


def analizar_tasa_nyquist(ancho_banda: float, niveles_m: int) -> float:
    """Calcula la capacidad máxima del canal según el criterio de Nyquist."""
    return 2 * ancho_banda * math.log2(niveles_m)
