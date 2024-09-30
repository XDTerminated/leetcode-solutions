class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        hvertical = defaultdict(list)
        hhorizontal = defaultdict(list)
        hs = defaultdict(list)
        hsquare = 0
        for i in range(len(board)):
            for j in range(len(board[i])):
                if i < 3:
                    if j < 3:
                        hsquare = 0
                    elif j < 6:
                        hsquare = 1
                    elif j < 9:
                        hsquare = 2
                elif i < 6:
                    if j < 3:
                        hsquare = 3
                    elif j < 6:
                        hsquare = 4
                    elif j < 9:
                        hsquare = 5                   
                elif i < 9:
                    if j < 3:
                        hsquare = 6
                    elif j < 6:
                        hsquare = 7
                    elif j < 9:
                        hsquare = 8
                
                if board[i][j] == ".":
                    continue

                if board[i][j] in hvertical[j]:
                    return False

                hvertical[j].append(board[i][j])

                if board[i][j] in hhorizontal[i]:
                    return False

                hhorizontal[i].append(board[i][j])
                
                if board[i][j] in hs[hsquare]:
                    return False

                hs[hsquare].append(board[i][j])

        return True