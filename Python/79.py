from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        # Hjelpefunksjon for å sjekke gyldige retninger med backtracking
        def dfs(x, y, index):
            # Hvis vi har funnet hele ordet
            if index == len(word):
                return True
            # Hvis vi er utenfor grenser eller bokstaven ikke matcher
            if x < 0 or y < 0 or x >= rows or y >= cols or board[x][y] != word[index]:
                return False
            # Midlertidig markere cellen som brukt
            temp = board[x][y]
            board[x][y] = "#"
            
            # Utforsk alle retninger
            found = (
                dfs(x + 1, y, index + 1) or  # Ned
                dfs(x - 1, y, index + 1) or  # Opp
                dfs(x, y + 1, index + 1) or  # Høyre
                dfs(x, y - 1, index + 1)     # Venstre
            )
            
            # Tilbakestill cellen
            board[x][y] = temp
            
            return found

        # Start DFS fra hver celle
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0] and dfs(i, j, 0):
                    return True
        
        return False