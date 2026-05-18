class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # by row
        for i in range(len(board)):
            a = dict()
            for j in range(len(board[i])):
                if board[i][j].isdigit():
                    a[board[i][j]] = a.get(board[i][j], 0) + 1
                    if a[board[i][j]] > 1:
                        return False

        # by colummn 
        for i in range(len(board)):
            k = 0
            a = dict()
            for j in range(len(board[k])):
                if board[k][i].isdigit():
                    a[board[k][i]] = a.get(board[k][i], 0) + 1
                    if a[board[k][i]] > 1:
                        return False 
                k += 1
        #return True
        # for i in range(len(board)):
        #     a = dict()
        #     for j in range(len(board)):
        #         if board[i][j].isdigit():
        #             if 0 <= j <= 2 and 0 <= i <= 2:
        #                 a[board[i][j]] = a.get(board[i][j], 0) + 1
        #                 if a[board[i][j]] > 1:
        #                     return False
        #             elif 3 <= j <= 5 and 0 <= i <= 2:
        #                 a[board[i][j]] = a.get(board[i][j], 0) + 1
        #                 if a[board[i][j]] > 1:
        #                     return False
        #             elif 6 <= j <= 8 and 0 <= i <= 2:
        #                 a[board[i][j]] = a.get(board[i][j], 0) + 1
        #                 if a[board[i][j]] > 1:
        #                     return False
        a = dict()
        for i in range(9):
            for j in range(9):

                num = board[i][j]
                b = (i // 3, j // 3)

                if num.isdigit():
                    if b not in a:
                        a[b] = set()
                    if num in a[b]:
                        return False 
                    a[b].add(num)

        return True