class CountDerangementsTopDown:
    def __init__(self, set_size):
        self.set_size = set_size
        self.sub_solutions = [-1] * (set_size + 1)

    def count_derangements(self):
        return self.count_derangements_rec(self.set_size)

    def count_derangements_rec(self, i):
        if self.sub_solutions[i] != -1:
            return self.sub_solutions[i]
        if i == 1:
            return 0
        if i == 2:
            return 1
        n = (i - 1) * (self.count_derangements_rec(i - 1) + self.count_derangements_rec(i - 2))
        self.sub_solutions[i] = n
        return n

# for i in range(1,64):
for i in range(1,11):
    n = CountDerangementsTopDown(i).count_derangements()
    print("Derangments in set size {} -> {}".format(i,n))
