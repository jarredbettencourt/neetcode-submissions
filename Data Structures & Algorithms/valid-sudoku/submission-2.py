class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROWS, COLS = len(board), len(board[0])
        
        row_mem = {}
        col_mem = {}
        diag_mem = {}

        def isValidDiag(r, c, mem, num):
            if (r,c) not in mem:
                mem[(r,c)] = set()
                mem[(r,c)].add(num)
            else:
                if num in mem[(r,c)] and num != '.':
                    return False
                mem[(r,c)].add(num)
            return True

        def isValid(i, mem, num):
            if i not in mem:
                mem[i] = set()
                mem[i].add(num)
            else:
                if num in mem[i] and num != '.':
                    return False
                mem[i].add(num)
            return True


        for r in range(ROWS):
            for c in range(COLS):
                valid_diag = isValidDiag(r // 3 , c // 3 , diag_mem, board[r][c])
                valid_row = isValid(r, row_mem, board[r][c])
                valid_col = isValid(c, col_mem, board[r][c])
                if not (valid_row and valid_col and valid_diag): return False
        return True