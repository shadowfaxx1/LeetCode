class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels="aeiouAEIOU"
        s=list(s)
        l=0
        r=len(s)-1
        while(l<r):
            if s[l] in vowels and s[r] in vowels:
                s[l], s[r] = s[r], s[l]  
                l+=1
                r-=1
            elif s[l] not in vowels:
                l+=1
            else:
                r-=1
        return ''.join(s)


s=Solution()
sz="miniemeso"
print(s.reverseVowels(sz))


        


                    