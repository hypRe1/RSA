class PrivateKey:
    def __init__(self, d: int, N: int) -> None:
        self.__d = d
        self.__N = N
    
    def getD(self) -> int:
        return self.__d
    
    def getN(self) -> int:
        return self.__N

    def decryptChar(self, code: int) -> str:
        return chr(pow(code, self.getD(), self.getN()))
    
    def decrypt_file(self, input: str, output: str, sep: str = "\\") -> None:
        with open(input) as inputF:
            with open(output, "w") as outputF:
                outputF.write("".join([
                    self.decryptChar(int(char.strip())) for char in inputF.read().split(sep)
                    if char.strip().isdigit()
                    ]))
                    