import ctypes
import os

class MemorySanitizationEngine:
    """
    Enforces secure byte-level volatile memory erasure 
    to prevent cold-boot RAM recovery attacks.
    """
    @staticmethod
    def secure_wipe_bytearray(target_buffer: bytearray):
        """
        Overwrites memory address directly with zero-fill patterns 
        followed by high-entropy noise.
        """
        if not isinstance(target_buffer, bytearray):
            raise TypeError("Target must be a mutable bytearray for hardware-level overwrite.")

        length = len(target_buffer)
        
        # Pass 1: Overwrite with zeros
        for i in range(length):
            target_buffer[i] = 0x00

        # Pass 2: Overwrite with cryptographic noise
        noise = os.urandom(length)
        for i in range(length):
            target_buffer[i] = noise[i]

    @staticmethod
    def zero_out_ctypes_pointer(address: int, size: int):
        """Direct C-level memory zeroing for raw memory pointers."""
        ctypes.memset(address, 0, size)
