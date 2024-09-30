class Solution:
    def isWinner(self, player1: list[int], player2: list[int]) -> int:
        sumPlayer1 = 0
        sumPlayer2 = 0

        sumDouble = 0
        sumDouble2 = 0
        for i in range(len(player1)):

            if sumDouble > 0:
                sumPlayer1+=(player1[i] * 2)
                sumDouble-=1
            else:
                sumPlayer1+=player1[i]


            if sumDouble2 > 0:
                sumPlayer2+=(player2[i] * 2)
                sumDouble2-=1

            else:
                sumPlayer2+=player2[i]

            if player1[i] == 10:
                sumDouble = 2
            if player2[i] == 10:
                sumDouble2 = 2

        print(sumPlayer1)
        print(sumPlayer2)
        if sumPlayer1 == sumPlayer2:
            return 0
        else:
            return 1 if sumPlayer1 > sumPlayer2 else 2
