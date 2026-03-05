def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0

    for char in s:
        if char in vowels:
            count += 1

    return count


text = input("Nhap chuoi: ")
print("So nguyen am:", count_vowels(text))
