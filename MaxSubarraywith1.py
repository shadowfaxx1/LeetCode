def longestSubarray(list1):
    left = 0
    right = 0
    mx_1 = 0
    c_z = 0
    while right < len(list1):
        if list1[right] == 1:
            right += 1
        else:
            if c_z == 0:
                c_z += 1
                right += 1
            else:
                if list1[left] == 0:
                    c_z -= 1
                left += 1
        mx_1 = max(mx_1, right - left - 1)

    return mx_1                    

if __name__ == "__main__":
    print(longestSubarray([0, 1, 1, 1, 0, 1, 1, 0, 1]))

