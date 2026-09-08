
class Solution:
    def frequencySort(self, s: str) -> str:
    
        char_frequency = Counter(s)
        sorted_chars = sorted(char_frequency.items(), key=lambda item: -item[1])
        result = ''.join(char * freq for char, freq in sorted_chars)
        return result



