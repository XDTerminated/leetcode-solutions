class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        # Using Kadane's algorithm

        # differences = []
        # for i in range(len(prices) - 1):
        #     differences.append(prices[i + 1] - prices[i])

        # differences = differences + [0]

        # maxProfit = differences[0]
        # maxTemp = differences[0]

        # for i in range(1, len(differences)):
        #     maxTemp = max(differences[i], maxTemp + differences[i])
        #     if maxTemp > maxProfit:
        #         maxProfit = maxTemp

        # return maxProfit


        if not prices:
            return 0
        minPrice = prices[0]
        maxProfit = 0

        for i in range(len(prices)):
            if prices[i] < minPrice:
                minPrice = prices[i]

            if prices[i] - minPrice > maxProfit:
                maxProfit = prices[i] - minPrice

        return maxProfit
