class CountDerangementsRec:
    def __init__(self, set_size):
        self.set_size = set_size

    def count_derangements(self):
        return self.count_derangements_rec(self.set_size)

    def count_derangements_rec(self, i):
        if i == 1:
            return 0
        if i == 2:
            return 1
        return (i - 1) * (self.count_derangements_rec(i - 1) + self.count_derangements_rec(i - 2))


for i in range(1, 64):
    # for i in range(1,11):
    n = CountDerangementsRec(i).count_derangements()
    print("Derangments in set size {} -> {}".format(i, n))
