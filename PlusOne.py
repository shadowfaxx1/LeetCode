def Addone(arr):
    i = len(arr) - 1
    carry = 0
    flag = 1
    res = []
    while i >= 0 or carry > 0:
        sum = carry
        if i >= 0 and flag == 1:
            sum += arr[i] + 1
            flag = 2
        elif i >= 0:
             sum += arr[i]
        res.append(sum % 10)
        carry = sum // 10
        i -= 1
        
    res.reverse()

    return res

ar = [1, 2, 3, 4]
ar2 = [2, 1, 9, 9]
ar3 = [9, 9]

print(Addone(ar))   # Output: [1, 2, 3, 5]
print(Addone(ar2))  # Output: [2, 2, 0, 0]
print(Addone(ar3))  # Output: [1, 0, 0]
