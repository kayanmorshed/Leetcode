class Solution:
    def simplifyPath(self, path: str) -> str:
        spath = path.split('/')
        result = []
        
        for i in range(len(spath)):
            if spath[i] == '' or spath[i] == '.' or (spath[i] == '..' and len(result) == 0): 
                continue
            elif spath[i] == '..' and len(result) > 0:
                result.pop()
            else:
                result.append(spath[i])
        
        if len(result) == 0:
            return '/'
        
        output = ''
        for item in result:
            output += '/' + item
        
        return output