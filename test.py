a = ['name_1_100_out.txt', 'name_1_10_out.txt',
     'name_1_6_out.txt', 'name_1_5_out.txt', 'name_1_2_out.txt']

b = sorted(a, key=lambda x: x[7:8] if len(x) <= 16 else x[7:9] if len(x) >= 17 else x[7:10], reverse=True)

print(a[0][7:10])
print(a[1][7:9])
if a[0][7:10] > a[1][7:9]:
    print(True)
print(b)
