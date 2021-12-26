class Solution:
    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:
        answer = []
        
        def count_number_of_instructions(currPos, s, pivot):
            num_iter = 0
            while pivot < len(s):                
                # update currPos based on the instruction
                if s[pivot] == 'L': currPos = [currPos[0], currPos[1]-1]
                if s[pivot] == 'R': currPos = [currPos[0], currPos[1]+1]
                if s[pivot] == 'U': currPos = [currPos[0]-1, currPos[1]]
                if s[pivot] == 'D': currPos = [currPos[0]+1, currPos[1]]
                
                # update the position of the current instruction
                pivot += 1    
                
                if currPos[0] < 0 or currPos[0] > n-1 or currPos[1] < 0 or currPos[1] > n-1:
                    return num_iter
                else:
                    num_iter += 1 # increase the counter
            return num_iter

        
        
        for i in range(len(s)):
            # num_iter = 0 # counter to count the number of instrcutions the robot can execute
            num_iter = count_number_of_instructions(startPos, s, i)
            answer.append(num_iter)
        
        return answer
            
            
            
        