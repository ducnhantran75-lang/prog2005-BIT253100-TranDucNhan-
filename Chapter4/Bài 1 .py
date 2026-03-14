def thong_ke(numbers):
    tong = sum(numbers)
    lon_nhat = max(numbers)
    nho_nhat = min(numbers)
    return tong, lon_nhat, nho_nhat



# test
data = (3, 7, 1, 9, 5, 2)
tong, max_val, min_val = thong_ke(data)

print("Tong:", tong)
print("Lon nhat:", max_val)
print("Nho nhat:",min_val)


