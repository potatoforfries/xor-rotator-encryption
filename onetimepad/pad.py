import os           # for generating random bytes

class OneTimePad:
    def __init__(self):   
        self.key = None

    def generate_key(self, length:int):
        self.key = os.urandom(length)

    def encrypt(self, text:str) -> list[int]: 
        # generate a key if none exists or size doesnt match the text.
        if self.key == None or len(self.key) != len(text):
            self.generate_key(len(text))
        
        # convert each character in the text and key into integers 
        # Encrypt the text using XOR and returns a list of encrypted integers
        return [ord(char) ^ k_byte for char, k_byte in zip(text, self.key)]     

    def decrypt(self, encrypted:list):
        # Decrypt the text by XORing the encrypted values with the same key
        # XORing again with the same key gives back the original character
        # Join all decrypted characters into a string
        return "".join(chr(enc_val ^ k_byte) for enc_val, k_byte in zip(encrypted, self.key))




if __name__ == "__main__":
    otp = OneTimePad()                  # Create an one time pad object
    text = "Exaaaaactly20letters"       # value to encrypt(string)

    enc = otp.encrypt(text)             # encrypt text into a list[int]
    print("Encrypted list of integers: ", enc)
    print("Random k_bytes generated to encrypt and decrypt: ", otp.key)
    dec = otp.decrypt(enc)              # decrypt back into a string
    print("Decrypted string: ", dec)