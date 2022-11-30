class Cipher:
    """Кодирование и декодирование строк."""
    dict = {'A': 'C','B': 'R','C':'Y','D': 'P','E': 'T','F': 'O',
    'G': 'A','H': 'B','I': 'D','J': 'E','K': 'F','L': 'G','M': 'H',
    'N': 'I','O': 'J','P': 'K','Q': 'L','R': 'M','S': 'N','T': 'Q',
    'U': 'S','V': 'U','W': 'V','X': 'W','Y': 'X','Z': 'Z'}

    def __init__(self) -> None:
        self.dict

    def encode(self, string):
        result = []
        for i in string:
            symbol = self.dict.get(i.upper(),i.upper())
            result.append(symbol)
            encodes_string = "".join(result)
        return print(encodes_string.capitalize())

    def decode(self, string):
        result = []
        for i in string:
            symbol = dict(zip(self.dict.values(), self.dict.keys()))
            symbol = symbol.get(i.upper(), i.upper())
            result.append(symbol)
            decodes_string = "".join(result)
        return print(decodes_string.capitalize())


cipher = Cipher()
cipher.encode('Hello world')
cipher.decode('Fjedhc dn atidsn')