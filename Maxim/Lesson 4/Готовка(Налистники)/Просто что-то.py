data_db = [('292.2', '295.7', '301.1'), ('118.8', '125.6', '257.4'), ('206.1', '240.6', '330.1'), ('208.8', '191.5', '234.2')]
a = [tuple(float(x) for x in inner) for inner in data_db]
print(a)

b = []
for i in data_db:
    i_temp = []
    for k in i:
        i_temp.append(float(k))
    b.append(list(i_temp))
print(b)


