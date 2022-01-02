class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        
        if len(colors) < 3:
            return False
        
        Alice = 0
        Bob = 0
        
        for i in range(1, len(colors)-1):
            if colors[i-1] == colors[i] and colors[i] == colors[i+1]:
                if colors[i] == 'A':
                    Alice += 1
                else:
                    Bob += 1
        if Alice > Bob:
            return True
        else:
            return False
        