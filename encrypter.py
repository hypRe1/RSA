class RSA_Encrypter():
    def __init__(self, e: int, N: int) -> None:
        self.e = e
        self.N = N
    
    def encrypt_num(self, num) -> int:
        return pow(num, self.e, self.N)
    
    def encrypt_text(self, text, sep="\\") -> str:
        encrypted = ""
        for char in text:
            code = pow(ord(char), self.e, self.N)
            encrypted += str(code) + sep
        return encrypted
    
    def encrypt_file(self, input_loc, output_loc, sep="\\") -> None:
        with open(input_loc, "r") as inputf:
            with open(output_loc, "w") as outputf:
                outputf.write(str(self.encrypt_text(inputf.read(), sep)))