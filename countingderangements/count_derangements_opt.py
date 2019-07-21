class CountDerangementsOpt:
    def __init__(self, set_size):
        self.set_size = set_size
        self.solution_i, solution_i_minus_1, solution_i_minus_2 = 0, 0, 0
        for i in range(1, set_size + 1):
            if i == 1:
                self.solution_i = 0
            elif i == 2:
                self.solution_i = 1
            else:
                self.solution_i = (i - 1) * (solution_i_minus_1 + solution_i_minus_2)
            solution_i_minus_2 = solution_i_minus_1
            solution_i_minus_1 = self.solution_i

    def count_derangements(self):
        return self.solution_i


# for i in range(1,64):
for i in range(1, 11):
    n = CountDerangementsOpt(i).count_derangements()
    print("Derangments in set size {} -> {}".format(i, n))
