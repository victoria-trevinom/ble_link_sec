"""Módulo de criptografía y corrección de errores para el enlace BLE."""


def xor_encrypt_decrypt(data: bytes, key: bytes) -> bytes:
    """Aplica cifrado XOR (One-Time Pad simplificado) entre datos y clave."""
    return bytes(b ^ key[i % len(key)] for i, b in enumerate(data))


def hamming_74_encode(nibble: int) -> int:
    """Codifica un nibble (4 bits) usando el código Hamming(7,4)."""
    d1 = (nibble >> 3) & 1
    d2 = (nibble >> 2) & 1
    d3 = (nibble >> 1) & 1
    d4 = nibble & 1

    p1 = d1 ^ d2 ^ d4
    p2 = d1 ^ d3 ^ d4
    p3 = d2 ^ d3 ^ d4

    # Ensamblar código de 7 bits: p1 p2 d1 p3 d2 d3 d4
    encoded = (
        (p1 << 6)
        | (p2 << 5)
        | (d1 << 4)
        | (p3 << 3)
        | (d2 << 2)
        | (d3 << 1)
        | d4
    )
    return encoded
