class FullBusTour:
    def __init__(self, group_sizes, full_cap):
        self.group_sizes = group_sizes
        self.full_cap = full_cap
        self.sub_solutions = [[]] * (len(group_sizes) + 1)
        for i in range(len(group_sizes) + 1):
            self.sub_solutions[i] = [None] * (full_cap + 1)

    def fits_exactly(self):
        return self.fits_exactly_rec(len(self.group_sizes), self.full_cap)

    def fits_exactly_rec(self, length, c):
        if c == 0:
            return True
        if length == 0:
            return False
        if self.sub_solutions[length][c] is not None:
            return self.sub_solutions[length][c]
        c_remaining = c - self.group_sizes[length - 1]
        result = self.fits_exactly_rec(length - 1, c) or (
                c_remaining >= 0 and self.fits_exactly_rec(length - 1, c_remaining))
        self.sub_solutions[length][c] = result
        return result
