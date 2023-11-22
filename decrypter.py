class RSA_Decrypter():
    def __init__(self, d: int, N: int) -> None:
        self.d = d
        self.N = N
    
    def decrypt_num(self, num: int) -> int:
        return pow(num, self.d, self.N)
    
    def decrypt_text(self, text: str, sep="\\") -> str:
        decrypted = ""
        for code in text.split(sep):
            if code.isdigit():
                decrypted += chr(pow(int(code), self.d, self.N))
        return decrypted
    
    def decrypt_file(self, input_loc, output_loc, sep="\\") -> None:
        with open(input_loc, "r") as inputf:
            with open(output_loc, "w") as outputf:
                outputf.write(self.decrypt_text(inputf.read()))