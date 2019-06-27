class StringDistanceTopDown:
    def __init__(self, str_A, str_B):
        self.str_A = str_A
        self.str_B = str_B
        self.dist = [[]] * (len(str_A) + 1)
        for i in range(len(str_A) + 1):
            self.dist[i] = [-1] * (len(str_B) + 1)

    def distance(self):
            return self.distance_r(len(self.str_A), len(self.str_B))

    def distance_r(self, a, b):
        if self.dist[a][b] != -1:
            return self.dist[a][b]
        if a == 0:
            return b
        if b == 0:
            return a
        replace_cost = 0 if self.str_A[a - 1] == self.str_B[b - 1] else 1

        cost_delete = self.distance_r(a - 1, b) + 1
        cost_insert = self.distance_r(a, b - 1) + 1
        cost_replace = self.distance_r(a - 1, b - 1) + replace_cost
        min_cost = min(cost_delete, cost_insert, cost_replace)
        self.dist[a][b] = min_cost
        return min_cost


#dist = StringDistanceTopDown("TodayIsSaturday", "TomorrowIsSunday")
dist = StringDistanceTopDown("Saturday", "Sundays")
print(dist.distance())
