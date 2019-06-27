class AircraftSpacingTopDown:
    def __init__(self, passangers):
        self.passangers = passangers
        self.sub_solutions = [-1] * len(passangers)

    def max_passangers(self, i):
        if i >= len(self.passangers):
            return 0
        if self.sub_solutions[i] != -1:
            return self.sub_solutions[i]
        choosing_first = self.passangers[i] + self.max_passangers(i + 2)
        not_choosing_first = self.max_passangers(i + 1)
        max_pass = max(choosing_first, not_choosing_first)
        self.sub_solutions[i] = max_pass
        return max_pass


# spacing = AircraftSpacingTopDown([155, 55, 2, 96, 67, 203, 3, 66, 32, 65, 29, 8, 299, 323, 77, 3, 28,
#                              128, 19, 523, 372, 2, 3, 66, 124, 38, 34, 12,88, 23 ,74,65, 87, 434,
#                              14, 7, 49, 38, 27, 641, 61, 58, 14, 57, 71, 11, 82, 178, 93, 191, 4])
spacing = AircraftSpacingTopDown([155, 55, 2, 96, 67, 203, 3])
print(spacing.max_passangers(0))
