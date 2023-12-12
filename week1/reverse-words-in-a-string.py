class Solution:
    def reverseWords(self, s: str) -> str:

        string = []
        for char in s.strip():
            if (char == ' ' and string[-1] == ' '):
                continue
            string.append(char)


        first , last = 0, len(string) - 1
        while (first < last):
            string[first], string[last] = string[last], string[first]
            first += 1
            last -= 1


        start = 0
        for idx in range(1, len(string)):
            if (string[idx - 1] == ' '):
                end = idx - 2
                while (start < end):
                    string[start], string[end] = string[end], string[start]
                    start += 1
                    end -= 1
                start = idx
        end = len(string) - 1
        while (start < end):
            string[start], string[end] = string[end], string[start]
            start += 1
            end -= 1
        return "".join(string)