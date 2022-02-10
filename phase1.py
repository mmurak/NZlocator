count = 0
#shurui = {}

sortwork = []

with open('aotearoa-nz.csv') as f:
    for line in f:
        line = line.strip()
        arr = line.split(',')
        if arr[0] == 'id':
            continue
        arr[1] = arr[1].upper()
        arr[1] = arr[1].replace('Ā', 'A');
        arr[1] = arr[1].replace('Ē', 'E');
        arr[1] = arr[1].replace('Ī', 'I');
        arr[1] = arr[1].replace('Ō', 'O');
        arr[1] = arr[1].replace('Ū', 'U');
        arr[3] = arr[3].upper()
        sortwork.append([arr[1], arr[3], arr[4], arr[5]]);

print('let database = [')
for arr in sorted(sortwork, key=lambda kname: kname[0]):
    print(f'["{arr[0]}","{arr[1]}",{arr[2]},{arr[3]}],')
print('];')
#        count += 1
#print(count)
#for i in shurui:
#    print(i)

