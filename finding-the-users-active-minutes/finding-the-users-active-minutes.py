class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        unique_minutes = {}
        
        for log in logs:
            if log[0] not in unique_minutes:
                unique_minutes[log[0]] = [log[1]]
            elif log[1] not in unique_minutes[log[0]]:
                unique_minutes[log[0]].append(log[1])
            else:
                continue
        
        answer = [0] * k
        
        for id_ in unique_minutes:
            answer[len(unique_minutes[id_]) - 1] += 1
        
        return answer