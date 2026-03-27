def count_vowels(s):
    vowels = "ueoaiUEOAI"
    count = 0

    for c in s:
        if c in vowels:
            count += 1
    return count


s = input("Nhập chuỗi: ")
print("Số nguyên âm:", count_vowels(s))