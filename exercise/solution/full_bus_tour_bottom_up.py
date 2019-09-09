class FullBusTour:
    def __init__(self, group_sizes, full_cap):
        self.group_sizes = group_sizes
        self.full_cap = full_cap
        self.sub_solutions = [[]] * (len(group_sizes) + 1)
        for length in range(len(group_sizes) + 1):
            self.sub_solutions[length] = [None] * (full_cap + 1)
            for c in range(full_cap + 1):
                if c == 0:
                    self.sub_solutions[length][c] = True
                elif length == 0:
                    self.sub_solutions[length][c] = False
                else:
                    c_remaining = c - self.group_sizes[length - 1]
                    self.sub_solutions[length][c] = self.sub_solutions[length - 1][c] or (
                            c_remaining >= 0 and self.sub_solutions[length - 1][c_remaining])

    def fits_exactly(self):
        return self.sub_solutions[len(self.group_sizes)][self.full_cap]

