class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        start_list = []
        visit = set()
        def backtrack(word, r, c, visit):
            if r < 0 or c < 0 or r > (ROWS - 1) or c > (COLS - 1) or (r,c) in visit or board[r][c] != word[0]:
                return False
            elif len(word) == 1 and board[r][c] == word[0]:
                return True
            visit.add((r,c))
            result = backtrack(word[1:], r + 1, c, visit) or backtrack(word[1:], r - 1, c, visit) or backtrack(word[1:], r, c + 1, visit) or backtrack(word[1:], r, c - 1, visit) 
            visit.remove((r,c))
            return result

        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == word[0]:
                    start_list.append((r,c))           
        
        for start_row, start_col in start_list:
            return backtrack(word, start_row, start_col, visit)