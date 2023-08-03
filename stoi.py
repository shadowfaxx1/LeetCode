#atoi function imitation i.e converting the string to integer 
# firstly remove all of the whitespaces and then get the polarity sign 
# we also have to check for the overflow of the integer and in case return INT MAX or INT MIN; 


class solution(object):
    def __init__(self,s=None) -> str:
        self.s=s
    def myAtoi(self):
        i =0
        ss=self.s
        ss=ss.strip()   #reomving whitepaces
        flag=1
        if(ss[i] == '-' or ss[i]=='+'): #checking the sign 
            flag=-1 if ss[i]=='-' else 1
            i+=1
        

        res=0
        n=len(ss)

        while i < n and ss[i].isdigit(): #storing the result in the res int 
                res = res * 10 + int(ss[i])
                i += 1
            
        res=res*flag
        if(res>2**31-1 ): #overflow checking 
            return 2**31-1
        if(res<-2**31-1):
            return -2**31-1
        return res

if __name__=="__main__":
    s=solution("       -4222 ok fs ")
    print(s.myAtoi())

