class CountDerangementsTopDown:
    def __init__(self, set_size):
        self.set_size = set_size
        self.sub_solutions = [-1] * (set_size + 1)

    def count_derangements(self):
        return self.count_derangements_rec(self.set_size)

    def count_derangements_rec(self, n):
        if self.sub_solutions[n] != -1:
            return self.sub_solutions[n]
        if n == 1:
            return 0
        if n == 2:
            return 1
        result = (n - 1) * (self.count_derangements_rec(n - 1) + self.count_derangements_rec(n - 2))
        self.sub_solutions[n] = result
        return result


# for i in range(1,64):
for i in range(1,11):
    n = CountDerangementsTopDown(i).count_derangements()
    print("Derangments in set size {} -> {}".format(i,n))
