def Base_ToBase10(num, originalBase):
    if num == 0: return "0"
    if originalBase < 2 or originalBase > 36: return "2 <= base <= 36."

    chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    convertedNum = 0
    num = num[::-1]
    for i in range(len(num)):
        convertedNum += chars.index(num[i].upper()) * (originalBase ** i)

    return convertedNum

print(Base_ToBase10("1111011", 2)) #"num", originalBase