import sys


class TextJustifyDyn:
    def __init__(self, txt, line_length):
        self.txt = txt
        self.line_length = line_length

    def ugly_score(self, txt_length):
        if txt_length <= self.line_length:
            return (self.line_length - txt_length) ** 2
        else:
            return sys.maxsize

    def count_chars(self, fr, to):
        total_chars = 0
        for i in range(fr, to):
            total_chars += len(self.txt[i])
            if i < to - 1:
                total_chars += 1
        return total_chars

    def format_txt(self):
        scores = [0] * (len(self.txt) + 1)
        ptrs = [0] * len(self.txt)

        for i in range(len(self.txt) - 1, -1, -1):
            score = sys.maxsize
            for j in range(i + 1, len(self.txt) + 1):
                curr_score = self.ugly_score(self.count_chars(i, j)) + scores[j]
                if curr_score < score:
                    score = curr_score
                    ptrs[i] = j
            scores[i] = score

        self.print_txt(ptrs)
        return scores[0]

    def print_txt(self, ptrs):
        i = 0
        while i < len(ptrs):
            line = self.txt[i:ptrs[i]]
            print(" ".join(line))
            i = ptrs[i]


justify = TextJustifyDyn("Isabel sat on the step".split(), 10)
print(justify.format_txt())
