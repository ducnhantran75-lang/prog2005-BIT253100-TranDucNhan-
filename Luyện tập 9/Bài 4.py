text = input("nhap chuoi: ")

upper = lower = digit = special = space = vowel = consonant = 0
vowels = "aeiouAEIOU"

for ch in text:
    if ch.isupper():
        upper += 1

    elif ch.islower():
        lower += 1

    if ch.isdigit():
        digit += 1

    if ch.isspace():
        space += 1

    if ch.isalpha():
        if ch in vowels:
            vowel += 1
        else:
            consonant += 1

    if not ch.isalnum() and not ch.isspace():
        special += 1


print("chu hoa:", upper)
print("chu thuong:", lower)
print("chu so:", digit)
print("ky tu dac biet:", special)
print("khoang trang:", space)
print("nguyen am:", vowel)
print("phu am:", consonant)




