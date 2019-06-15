class StringDistanceOpt:
    def __init__(self, str_A, str_B):
        self.str_A = str_A
        self.str_B = str_B
        self.dist1 = [-1] * (len(str_B) + 1)
        self.dist2 = [-1] * (len(str_B) + 1)

        for a in range(len(str_A) + 1):
            for b in range(len(str_B) + 1):
                if a == 0:
                    self.dist2[b] = b
                elif b == 0:
                    self.dist2[b] = a
                else:
                    replace_cost = 0 if self.str_A[a - 1] == self.str_B[b - 1] else 1
                    cost_delete = self.dist1[b] + 1
                    cost_insert = self.dist2[b - 1] + 1
                    cost_replace = self.dist1[b - 1] + replace_cost
                    self.dist2[b] = min(cost_delete, cost_insert, cost_replace)
            print(self.dist2)
            (self.dist1, self.dist2) = (self.dist2, self.dist1)

    def distance(self):
        return self.dist1[len(self.str_B)]


#dist = StringDistanceOpt("TodayIsSaturday", "TomorrowIsSunday")
dist = StringDistanceOpt("Saturday", "Sundays")
print(dist.distance())
