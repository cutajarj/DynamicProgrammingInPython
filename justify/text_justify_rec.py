import sys


class TextJustifyRec:
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

    def format_txt(self, i):
        if i == len(self.txt):
            return 0
        score = sys.maxsize
        for x in range(i + 1, len(self.txt) + 1):
            line_len = self.count_chars(i, x)
            curr_score = self.ugly_score(line_len)
            curr_score += self.format_txt(x)
            score = min(curr_score, score)
        return score


justify = TextJustifyRec("Isabel sat on the step".split(), 10)
print(justify.format_txt(0))
