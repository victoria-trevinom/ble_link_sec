"""MÃ³dulo de criptografÃ­a para cifrado XOR y codificaciÃ³n Hamming."""


def xor_encrypt_decrypt(data: bytes, key: bytes) -> bytes:
    """Aplica cifrado o descifrado XOR entre los datos y una llave."""
    return bytes(b ^ key[i % len(key)] for i, b in enumerate(data))
