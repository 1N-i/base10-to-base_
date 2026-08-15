def Base10ToBase_(num, base):
    if num == 0: return "0"
    if base < 2 or base > 36: return "2 <= base <= 36."

    convertedNum = ""
    chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    while num != 0:
        remain = num % base
        convertedNum += chars[remain]
        num //= base

    return convertedNum[::-1]

print(Base10ToBase_(123, 2)) #num, base