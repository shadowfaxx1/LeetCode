

def groupAnagram(arr):
    d={}
    res=[]
    for c in arr:
        s = list(c)  # Convert string to a list of characters
        s.sort()
        s = ''.join(s)

        if not (s in d) :
            d[s]=[c]
        else:
            d[s].append(c)
            
    for value in d.values():
        res.append(value)
    return res

inp=["eat","tea","tan","ate","nat","bat"]
print(groupAnagram(inp))
