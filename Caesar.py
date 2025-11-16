class Caesar:
    @staticmethod
    def Caesar_cipher_endpoint(encryption: str, hist: int = 2):
        letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",]
        for word in encryption:
            w = word.isalpha()