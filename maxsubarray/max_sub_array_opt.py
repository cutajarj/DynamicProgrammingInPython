class MaxSubArrayOpt:
    def __init__(self, prices):
        self.prices = prices
        self.global_max, local_max = 0, 0
        for i in range(len(self.prices)):
            if i == 0:
                local_max = self.prices[0]
            else:
                local_max = max(self.prices[i], local_max + self.prices[i])
            self.global_max = max(self.global_max, local_max)

    def max_sub_array(self):
        return self.global_max


msa = MaxSubArrayOpt([5, -4, 8, -10, -2, 4, -3, 2, 7, -8, 3, -5, 3])
print(msa.max_sub_array())

# input = [1] * 900
# for i in range(10):
#     msa = MaxSubArrayOpt(input)
#     print(msa.max_sub_array())


