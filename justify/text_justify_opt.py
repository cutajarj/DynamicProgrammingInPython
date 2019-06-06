import sys


class TextJustifyOpt:
    def __init__(self, txt, line_length):
        self.txt = txt
        self.line_length = line_length
        self.word_length = [[]] * len(txt)
        for i in range(len(txt)):
            self.word_length[i] = [0] * len(txt)
            self.word_length[i][i] = len(txt[i])
            for j in range(i + 1, len(txt)):
                self.word_length[i][j] = self.word_length[i][j - 1] + 1 + len(txt[j])
        for arr in self.word_length:
            print(arr)

    def ugly_score(self, txt_length):
        if txt_length <= self.line_length:
            return (self.line_length - txt_length) ** 2
        else:
            return sys.maxsize

    def format_txt(self):
        scores = [0] * (len(self.txt) + 1)
        ptrs = [0] * len(self.txt)

        for i in range(len(self.txt) - 1, -1, -1):
            score = sys.maxsize
            for j in range(i + 1, len(self.txt) + 1):
                curr_score = self.ugly_score(self.word_length[i][j - 1]) + scores[j]
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


justify = TextJustifyOpt("Isabel sat on the step".split(), 10)
print(justify.format_txt())
