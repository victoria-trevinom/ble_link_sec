"""Interfaz de lÃ­nea de comandos (CLI) para BLE Link Security Tool."""
import argparse
import asyncio
from ble_link_sec.crypto import xor_encrypt_decrypt
from ble_link_sec.red import calcular_distancia_rssi
from ble_link_sec.interop import escanear_dispositivos


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
        "--key", type=str, default="clave_secreta",
        help="Llave de cifrado"
    )
    parser.add_argument(
        "--escanear", action="store_true",
        help="Escanea dispositivos BLE"
    )

    args = parser.parse_args()

    if args.rssi:
        dist = calcular_distancia_rssi(args.rssi)
        print(
            f"[+] RSSI: {args.rssi} dBm -> "
            f"Distancia estimada: {dist:.2f} m"
        )

    if args.cifrar:
        cifrado = xor_encrypt_decrypt(
            args.cifrar.encode("utf-8"),
            args.key.encode("utf-8")
        )
        print(f"[+] Texto cifrado (hex): {cifrado.hex()}")

    if args.escanear:
        print("[*] Buscando dispositivos BLE cercanos...")
        loop = asyncio.get_event_loop()
        dispositivos = loop.run_until_complete(
            escanear_dispositivos()
        )
        if not dispositivos:
            print("[-] No se encontraron dispositivos BLE cercanos.")
        for d in dispositivos:
            dist = calcular_distancia_rssi(d["rssi"])
            print(
                f"[+] {d['nombre']} ({d['direccion']}) | "
                f"RSSI: {d['rssi']} dBm | "
                f"Distancia: {dist:.2f} m"
            )


if __name__ == "__main__":
    main()
