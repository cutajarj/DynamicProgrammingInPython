class AircraftSpacingRec:
    def __init__(self, passengers):
        self.passengers = passengers

    def max_passengers(self, i):
        if i >= len(self.passengers):
            return 0
        choosing_first = self.passengers[i] + self.max_passengers(i + 2)
        not_choosing_first = self.max_passengers(i + 1)
        return max(choosing_first, not_choosing_first)


# spacing = AircraftSpacingRec([155, 55, 2, 96, 67, 203, 3, 66, 32, 65, 29, 8, 299, 323, 77, 3, 28,
#                              128, 19, 523, 372, 2, 3, 66, 124, 38, 34, 12,88, 23 ,74,65, 87, 434,
#                              14, 7, 49, 38, 27, 641, 61, 58, 14, 57, 71, 11, 82, 178, 93, 191, 4])
spacing = AircraftSpacingRec([155, 55, 2, 96, 67, 203, 3])
print(spacing.max_passengers(0))
