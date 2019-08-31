class FullBusTourRec:
    def __init__(self, group_sizes, full_cap):
        self.group_sizes = group_sizes
        self.full_cap = full_cap

    def fits_exactly(self):
        return self.fits_exactly_rec(len(self.group_sizes), self.full_cap)

    def fits_exactly_rec(self, length, c):
        if c == 0:
            return True
        if length == 0:
            return False
        return self.fits_exactly_rec(length - 1, c) or (c - self.group_sizes[length - 1] >= 0 and self.fits_exactly_rec(length - 1, c - self.group_sizes[length - 1]))

