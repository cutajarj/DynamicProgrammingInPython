class CountDerangementsRec:
    def __init__(self, set_size):
        self.set_size = set_size

    def count_derangements(self):
        return self.count_derangements_rec(self.set_size)

    def count_derangements_rec(self, n):
        if n == 1:
            return 0
        if n == 2:
            return 1
        return (n - 1) * (self.count_derangements_rec(n - 1) + self.count_derangements_rec(n - 2))


for i in range(1, 64):
    n = CountDerangementsRec(i).count_derangements()
    print("Derangements in set size {} -> {}".format(i, n))

