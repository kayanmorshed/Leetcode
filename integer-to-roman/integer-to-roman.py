class Solution:
    def intToRoman(self, num: int) -> str:
        symbol_map = {1000: 'M',
                      900: 'CM',
                      500: 'D',                    
                      400: 'CD',
                      100: 'C',
                      90: 'XC',
                      50: 'L',
                      40: 'XL',
                      10: 'X',
                      9: 'IX',
                      5: 'V',
                      4: 'IV',
                      1: 'I'
                     }
        
        result = ''
        
        for key in symbol_map.keys():
            if num >= key:
                quotient = num//key
                num = num % key
                result += quotient * symbol_map[key]
            else: 
                continue

        return result