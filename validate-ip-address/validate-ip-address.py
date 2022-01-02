class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        if len(queryIP) < 7: return "Neither"
        
        ip_parts = []
        separator, curr = '', ''
        sep_count = 0
        
        for ch in queryIP:
            if len(separator) > 0 and ch in '.:' and ch not in separator:
                return "Neither"
            
            elif ch in '.:':
                if len(separator) == 0:
                    separator += ch
                ip_parts.append(curr)
                curr = ''
                sep_count += 1
            
            else:
                curr += ch
        
        # add the last part into ip_parts
        ip_parts.append(curr)
        
        if len(ip_parts) == 4: ip_type = 'IPv4'
        elif len(ip_parts) == 8: ip_type = 'IPv6'
        elif abs(len(ip_parts)-sep_count) > 1: return "Neither" 
        else: return "Neither"
        
        # validating Ipv4 address
        if ip_type == 'IPv4':
            for item in ip_parts:
                if len(item) < 1 or len(item) > 3: return "Neither"
                elif len(item) > 1 and item[0] == '0': return "Neither"
                for ch in item:
                    if not ch.isdigit(): return "Neither"
                if int(item) < 0 or int(item) > 255: return "Neither"
            return ip_type

        # validating Ipv6 address
        dict_ = 'abcdefABCDEF'
        if ip_type == 'IPv6':
            for item in ip_parts:
                if len(item) < 1 or len(item) > 4: return "Neither"
                for ch in item:
                    if not ch.isdigit() and ch not in dict_: return "Neither"
            return ip_type

        