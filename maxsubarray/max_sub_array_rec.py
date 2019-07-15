class MaxSubArrayRec:
    def __init__(self, prices):
        self.prices = prices

    def max_sub_array(self):
        max_value = 0
        for j in range(len(self.prices)):
            max_value = max(max_value, self.max_sub_array_ending_at(j))
        return max_value

    def max_sub_array_ending_at(self, i):
        if i == 0:
            return self.prices[0]
        return max(self.prices[i], self.max_sub_array_ending_at(i - 1) + self.prices[i])


#msa = MaxSubArrayRec([5, -4, 8, -10, -2, 4, -3, 2, 7, -8, 3, -5, 3])
#print(msa.max_sub_array())

input = [1] * 900
for i in range(10):
    msa = MaxSubArrayRec(input)
    print(msa.max_sub_array())

