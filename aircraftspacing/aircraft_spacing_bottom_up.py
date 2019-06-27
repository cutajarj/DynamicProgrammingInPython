class AircraftSpacingBottomUp:
    def __init__(self, passengers):
        self.passengers = passengers
        self.sub_solutions = [-1] * len(passengers)
        for i in range(len(passengers) - 1, -1, -1):
            choosing_first = self.passengers[i] + (self.sub_solutions[i + 2] if i + 2 < len(self.sub_solutions) else 0)
            not_choosing_first = self.sub_solutions[i + 1] if i + 1 < len(self.sub_solutions) else 0
            self.sub_solutions[i] = max(choosing_first, not_choosing_first)

    def max_passengers(self):
        return self.sub_solutions[0]


# spacing = AircraftSpacingBottomUp([155, 55, 2, 96, 67, 203, 3, 66, 32, 65, 29, 8, 299, 323, 77, 3, 28,
#                              128, 19, 523, 372, 2, 3, 66, 124, 38, 34, 12,88, 23 ,74,65, 87, 434,
#                              14, 7, 49, 38, 27, 641, 61, 58, 14, 57, 71, 11, 82, 178, 93, 191, 4])
spacing = AircraftSpacingBottomUp([155, 55, 2, 96, 67, 203, 3])
print(spacing.max_passengers())
