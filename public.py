class PublicKey:
    def __init__(self, e: int, N: int) -> None:
        self.__e = e
        self.__N = N
    
    def getE(self) -> int:
        return self.__e
    
    def getN(self) -> int:
        return self.__N

    def encrypt(self, text) -> list:
        return [str(pow(ord(char), self.getE(), self.getN())) for char in text]

    def encrypt_file(self, input: str, output: str, sep: str="\\") -> None:
        with open(input) as inputF:
            with open(output, "w") as outputF:
                outputF.write(sep.join(self.encrypt(inputF.read())))
