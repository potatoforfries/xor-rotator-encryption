import os 

def export_key(key: bytes) -> str:
    """
    Converts a bytes object into a space-separated string of integers.
    """
    return ''.join(map(str, key))  

def import_key(key_str: str) -> bytes:
    """
    Converts a space-separated string of integers back into bytes.
    """
    return bytes(map(int, key_str.strip().split()))

def validate_key_length(text: str, key: bytes):
    if len(text) != len(key):
        raise ValueError("Key length must match the text length.")

def rotate_key(key: bytes, rotation:int) -> bytes:
    """
    Rotates each byte in the key by a given integer value.
    Wraps around at 255 (mod 256). (so it doesnt exceed 255 i.e. max value for 1 byte) 
    """
    return bytes((k_byte + rotation) % 256 for k_byte in key)