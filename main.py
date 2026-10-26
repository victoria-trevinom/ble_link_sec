"""Interfaz de línea de comandos (CLI)
para BLE Link Security Tool."""
import argparse
from ble_link_sec.crypto import xor_encrypt_decrypt
from ble_link_sec.red import calcular_distancia_rssi


def main():
    parser = argparse.ArgumentParser(
        description="Herramienta CLI de Seguridad BLE - PIA H3"
    )
    parser.add_argument(
        "--rssi", type=float, help="Valor de RSSI medido en dBm"
    )
    parser.add_argument(
        "--cifrar", type=str, help="Texto plano a cifrar mediante XOR"
    )
    parser.add_argument(
        "--key", type=str, default="clave_secreta", help="Llave de cifrado"
    )

    args = parser.parse_args()

    if args.rssi:
        dist = calcular_distancia_rssi(args.rssi)
        print(f"[+] RSSI: {args.rssi} dBm -> Distancia estimada: {dist:.2f} m")

    if args.cifrar:
        cifrado = xor_encrypt_decrypt(
            args.cifrar.encode(), args.key.encode()
        )
        print(f"[+] Texto cifrado (hex): {cifrado.hex()}")


if __name__ == "__main__":
    main()
