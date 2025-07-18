# Simple One Time Pad

a python class with simple implementation of One Time Pad encryption using bitwise XOR operations.

## Usage
```python
import OneTimePad 

# create the class object and insert the secret
# text to generate a random key of the same length as your text
otp = OneTimePad('secret text!') 

# returns an encrypted list of your text
encrypted = otp.encrypt('secret text!')

# returns a decrypted text again
decrypted = otp.decrypt(encrypted)
```
### OR

```python
import OneTimePad

# random key input by user
Key = 1231       #has to be an integer, byte or bit

# no need to mention text to encrypt in the class object
# parameter as its only used to generate random key
otp = OneTimePad(key=Key)  

# returns an encrypted list of your text using your custom Key
encrypted = otp.encrypt('secret text!')

# returns a decrypted text again
decrypted = otp.decrypt(encrypted)
```
please check the code to see how random bytes are generated and how the function works for custom usage. 

## Contributing

Pull requests are welcome. This is just a hobby project which I plan to slowly expand. 

## License

No licenses for now.