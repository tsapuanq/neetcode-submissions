class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # by row
        for i in range(len(board)):
            counter = dict()
            
            for j in range(len(board[i])):

                if board[i][j].isdigit():
                    counter[board[i][j]] = counter.get(board[i][j], 0) + 1

                    if counter[board[i][j]] > 1:
                        return False

        # by column 
        for i in range(len(board)):
            k = 0
            counter = dict()

            for j in range(len(board[k])):

                if board[k][i].isdigit():
                    counter[board[k][i]] = counter.get(board[k][i], 0) + 1

                    if counter[board[k][i]] > 1:
                        return False 
                k += 1

        counter = dict()
        for i in range(len(board)):
            for j in range(len(board[i])):

                num = board[i][j]
                key = (i // 3, j // 3)

                if num.isdigit():

                    if key not in counter:
                        counter[key] = set()

                    if num in counter[key]:
                        return False 

                    counter[key].add(num)

        return True