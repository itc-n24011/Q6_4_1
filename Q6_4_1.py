a = open('sample.txt')
taiki = 0
for kouta in a:
    print(kouta, end='')
    if taiki == 2:
        break
    taiki += 1
a.close()
