import os
import hashlib

class SIUCryptoEngine:
    """
    Cryptographic utility engine for pseudo-random scrambling 
    and non-recoverable entropic noise generation.
    """
    @staticmethod
    def generate_entropy_key(length: int = 32) -> bytes:
        return os.urandom(length)

    @staticmethod
    def apply_state_scramble(data: bytes, key: bytes) -> bytes:
        key_hash = hashlib.sha256(key).digest()
        scrambled = bytearray()
        for i, byte in enumerate(data):
            scrambled.append(byte ^ key_hash[i % len(key_hash)])
        return bytes(scrambled)

    @staticmethod
    def generate_irreversible_noise(length: int) -> bytes:
        return os.urandom(length)
