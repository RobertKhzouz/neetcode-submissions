class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""

        if not strs:
            return encoded
        
        for s in strs:
            length = len(s)
            digits = 0
            if length == 0:
                pass
            elif length < 10:
                digits = 1
            elif length < 100:
                digits = 2
            else:
                digits = 3
            encoded += f"{digits}{length}{s}"

        return encoded

    def decode(self, s: str) -> List[str]:

        if not s:
            return []
        
        decoded = []
        length = len(s)
        cur = 0
        
        next_seq_empty = s[cur] == "0" and s[cur + 1] == "0" 
        if next_seq_empty:
            decoded.append("")
            cur += 2

        while cur < length:
            print(f"BEGINNING CUR: {cur}")

            jump_str = ""
            num_digits = int(s[cur])
            for digit in range(1, num_digits + 1):
                jump_str += s[cur + digit]
            jump = int(jump_str) if jump_str else 0
            cur += num_digits if num_digits != 0 else 1

            string = ""
            for i in range(1, jump+1):
                string += s[cur + i]

            decoded.append(string)
            cur += jump + 1

            next_seq_empty = cur < length and s[cur] == "0" and s[cur + 1] == "0" 
            if next_seq_empty:
                decoded.append("")
                cur += 2

        return decoded
            