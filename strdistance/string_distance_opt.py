class StringDistanceOpt:
    def __init__(self, str_A, str_B):
        self.str_A = str_A
        self.str_B = str_B
        self.dist_read = [-1] * (len(str_B) + 1)
        self.dist_write = [-1] * (len(str_B) + 1)

        for a in range(len(str_A) + 1):
            for b in range(len(str_B) + 1):
                if a == 0:
                    self.dist_write[b] = b
                elif b == 0:
                    self.dist_write[b] = a
                else:
                    replace_cost = 0 if self.str_A[a - 1] == self.str_B[b - 1] else 1
                    cost_delete = self.dist_read[b] + 1
                    cost_insert = self.dist_write[b - 1] + 1
                    cost_replace = self.dist_read[b - 1] + replace_cost
                    self.dist_write[b] = min(cost_delete, cost_insert, cost_replace)
            (self.dist_read, self.dist_write) = (self.dist_write, self.dist_read)
            print(self.dist_read)

    def distance(self):
        return self.dist_read[len(self.str_B)]


#dist = StringDistanceOpt("TodayIsSaturday", "TomorrowIsSunday")
dist = StringDistanceOpt("Saturday", "Sundays")
print(dist.distance())
