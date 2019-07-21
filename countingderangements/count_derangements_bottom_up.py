class CountDerangementsBottomUp:
    def __init__(self, set_size):
        self.set_size = set_size
        self.sub_solutions = [-1] * (set_size + 1)
        for i in range(1, set_size + 1):
            if i == 1:
                self.sub_solutions[i] = 0
            elif i == 2:
                self.sub_solutions[i] = 1
            else:
                self.sub_solutions[i] = (i - 1) * (self.sub_solutions[i - 1] + self.sub_solutions[i - 2])

    def count_derangements(self):
        return self.sub_solutions[self.set_size]


# for i in range(1,64):
for i in range(1, 11):
    n = CountDerangementsBottomUp(i).count_derangements()
    print("Derangments in set size {} -> {}".format(i, n))
