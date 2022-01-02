class Solution:
    def minimumBuckets(self, street: str) -> int:
        if 'HHH' in street or street[:2] == 'HH' or street[-2:] == 'HH' or street == 'H':
            return -1
        
        count = street.count('H') - street.count('H.H')

        return count