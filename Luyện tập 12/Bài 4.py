n = int(input("nhap  vao 1 so n: "))
a, b = 0, 1
for i in range(n):
    print(a, end =  " ")
    a, b = b , a +b
