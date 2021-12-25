class Solution:
    def reverse(self, x: int) -> int:  
        if x < 0 and x >= (-2**31):
            # x_str = str(x)
            # x_str_rev = '-'
            # access from the 2nd last element excluding "-" sign
            x_str_rev = '-' + str(x)[len(str(x)):0:-1] 
            if int(x_str_rev) < (-2**31):
                return_value = 0
            else:
                return_value = int(x_str_rev)
            
        elif x >= 0 and x <= ((2**31)-1):
            # x_str = str(x) # convert the int into str
            x_str_rev = str(x)[::-1]
            if int(x_str_rev) > (2**31)-1:
                return_value = 0
            else:
                return_value = int(x_str_rev)
        else:
            return 0
        return return_value
