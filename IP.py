class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        if '.' in queryIP:
            ips = queryIP.split('.')
            if len(ips) !=4:
                return 'Neither'
            for a in ips:
                try:
                    if a.startsswith('0') and len(a)!=1:
                        return 'Neither'
                    elif int(a)<0 or int(a)>255:
                        return 'Neither'
                except:
                    return 'Neither'
            return 'IPv4'
        
        elif ':' in queryIP:
            ips = queryIP.split(':')
            if len(ips) !=8:
                return 'Neither'
            for a in ips:
                if len(a)>4 or len(a) ==0:
                    return 'Neither'
                for aa in a:
                    if aa not in '0123456789abcdefABCDEF':
                        return 'Neither'
            return 'IPv6'
        
        return 'Neither'
    
