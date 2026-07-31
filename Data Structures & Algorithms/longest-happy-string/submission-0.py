class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        res = ""
        counter = 0
        while a != 0 or b != 0 or c != 0:
            print(res, counter)
            if counter != 2:
                if max(a, b, c) == a:
                    if not res or res[-1] == 'a':
                        counter += 1
                    res += 'a'
                    a -= 1
                elif max(a, b, c) == b:
                    if not res or res[-1] == 'b':
                        counter += 1
                    res += 'b'
                    b -= 1
                else:
                    if not res or res[-1] == 'c':
                        counter += 1
                    res += 'c'
                    c  -= 1
            elif counter == 2:
                if max(a, b) == 0 or max(a, c) == 0 or max(b, c) == 0:
                    break
                else:
                    # pick the second highest and use that and then reset counter
                    if max(a,b,c) == a:
                        if max(b,c) == b:
                            res += 'b'
                            b -= 1
                        else:
                            res += 'c'
                            c -= 1
                    if max(a,b,c) == b:
                        if max(a,c) == a:
                            res += 'a'
                            a -= 1
                        else:
                            res += 'c'                        
                            c -= 1
                    if max(a,b,c) == c:
                        if max(a,b) == a:
                            res += 'a'
                            a -= 1
                        else:
                            res += 'b'
                            b-= 1
                    counter = 1
        return res