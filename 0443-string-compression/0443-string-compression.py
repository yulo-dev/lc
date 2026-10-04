class Solution:
    def compress(self, chars: list[str]) -> int:
        start = 0
        read = 0
        write = 0

        while read < len(chars):

            length = 0

            while read < len(chars) and chars[read] == chars[start]:
                read += 1
                length = read - start 

            chars[write] = chars[start]
            write += 1
            if length > 1:
                for num in str(length):
                    chars[write] = num
                    write += 1

            start = read

        return write