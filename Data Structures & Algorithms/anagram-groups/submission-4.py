class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagrams: dict[tuple[int], list[str]] = {}
        SUB = ord("a")

        for word in strs:

            freq_word = (0,) * 26

            for letter in word:

                index = ord(letter) - SUB
                l = list(freq_word)
                l[index] += 1
                freq_word = tuple(l)
            
            if freq_word in anagrams:
                anagrams[freq_word].append(word)
            else:
                anagrams[freq_word] = [word]

        return list(anagrams.values())