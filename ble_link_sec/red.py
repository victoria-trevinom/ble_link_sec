"""MÃ³dulo de red para cÃ¡lculo de distancia basado en atenuaciÃ³n RSSI."""


def calcular_distancia_rssi(
    rssi: float, rssi_1m: float = -60.0, n: float = 2.5
) -> float:
    """Calcula la distancia estimada en metros a partir del valor RSSI."""
    return 10 ** ((rssi_1m - rssi) / (10 * n))
