class CountDerangementsOpt:
    def __init__(self, set_size):
        self.set_size = set_size
        self.solution_n, solution_n_minus_1, solution_n_minus_2 = 0, 0, 0
        for n in range(1, set_size + 1):
            if n == 1:
                self.solution_n = 0
            elif n == 2:
                self.solution_n = 1
            else:
                self.solution_n = (n - 1) * (solution_n_minus_1 +
                                            solution_n_minus_2)
            solution_n_minus_2 = solution_n_minus_1
            solution_n_minus_1 = self.solution_n

    def count_derangements(self):
        return self.solution_n


# for i in range(1,64):
for i in range(1, 11):
    n = CountDerangementsOpt(i).count_derangements()
    print("Derangments in set size {} -> {}".format(i, n))
