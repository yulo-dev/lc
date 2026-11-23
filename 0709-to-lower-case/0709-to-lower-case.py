class Solution:
    def toLowerCase(self, s: str) -> str:
        
        new_s =""

        for char in s:
            if 65 <= ord(char) <= 90: #65=A 90=Z
            #或直接寫if "A" <= char <= "Z":
                new_s += chr(ord(char)+32)
            else:
                new_s += char

        return new_s

