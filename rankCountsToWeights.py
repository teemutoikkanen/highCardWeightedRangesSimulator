data = [0, 0, 2286675, 2061172, 2061909, 2060820, 2061260, 2060628, 1996029, 1935345, 1570847, 1488457, 1487284, 1354943, 1015871]

total = 0

for item in data:
    total += item
print(total)


odds_list = []
for i in range(1,16):
    odds_list.append(0)


for i in range(len(odds_list)):
    odds_list[i] = round(data[i]/total*100, 2)


print(odds_list)
#[0.0, 0.0, 9.75, 8.79, 8.8, 8.79, 8.79, 8.79, 8.52, 8.26, 6.7, 6.35, 6.34, 5.78, 4.33]

