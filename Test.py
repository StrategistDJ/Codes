import base64

def convert_hex_base64(str_8b):
    
    binary = bytes.fromhex(str_8b)
    result = base64.b64encode(binary)
    
    return result.decode()

str_8b = "4a1b48d7322394a78326cd283f0834093e65421a7e98e90e5b452d160b5d07d8"
str_64b = convert_hex_base64(str_8b)
print("Stringa base64:", str_64b)