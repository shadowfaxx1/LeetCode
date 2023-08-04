# longset substring using set and usign sliding windows in FUCKIIIIIINGGGGGGGG REAL TIME 
# so start with initializing the left and right pointers ok 


def sliding_window(s:str)->str:
    left=0
    right=0
    st=set()
    length=-2**31-1

    while(right<len(s)):
        if s[right] not in st:
            st.add(s[right])
            length=max(length,right-left+1)
            right+=1

        else:
            # remove from left side of window
            st.remove(s[left])
            left+=1

    return length


s="abcabcbb"
s1="bbbbb"
s3="pwwkew"

print(sliding_window(s)
)
print(sliding_window(s1)
)
print(sliding_window(s3)
)
