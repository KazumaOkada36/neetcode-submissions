class Solution:

    def encode(self, strs: List[str]) -> str:
        new_string = ""
        for word in strs:
            lengthy = len(word)
            new_string += str(lengthy)
            new_string += "#"
            new_string += word
        return new_string


    def decode(self, s: str) -> List[str]:
        listy = []
        word = ""
        are_we = 0
        county = ""
        i = 0
        real_count = 0
        while i < len(s):
            if are_we == 0 and s[i] != "#":
                county += s[i]
                i += 1            
            elif are_we == 0 and s[i] == "#":
                are_we = 1
                cont = int(county)
                i += 1
            if are_we == 1:
                while real_count < cont:
                    word += s[i]
                    real_count += 1
                    i += 1
                listy.append(word)
                county = ""
                word = ""
                real_count = 0
                are_we = 0

        return listy
