class Solution:
    def multiply(self, num1: str, num2: str) -> str:        
        
        if num1 == '0' or num2 == '0':
            return '0'
        
        maxlen = len(num1) + len(num2)
        product = ['0'] * maxlen # initialize a list to hold the product value
    
        carry1 = 0 # for product
        carry2 = 0 # for sum
                
        for j in range(len(num2)-1, -1, -1):
                        
            idx = maxlen - (len(num2) - j) # index to store the the product value (after doing taking mod 10)
            
            for i in range(len(num1)-1, -1, -1):
                temp_product = int(num1[i]) * int(num2[j])
                temp_sum = temp_product % 10 + int(product[idx]) + carry1
                
                product[idx] = str((temp_sum + carry2) % 10)
                
                carry2 = (temp_sum + carry2) // 10
                carry1 = temp_product // 10
                
                idx -= 1
            
            if carry1 > 0 or carry2 > 0:
                product[idx] = str(carry1 + carry2)
                carry1, carry2 = 0, 0
                
        # create the output product string from the list "product"
        result = ''
        
        for k in range(len(product)):
            if product[k] != '0': # first encounter of non-zero value
                for i in range(k, len(product)):
                    result += product[i]
                break
        
        return result
                
        