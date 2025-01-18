if __name__ == '__main__':
    r =[]
    g =[]
    for i in range(int(input())):
        name = input()
        score = float(input())
        r.append([name, score])
        g.append(score)
grade = sorted(set(g))
name=[]
m=grade[1]
for val in r:
    if m ==val[1]:
        name.append(val[0])
name.sort()
for nm in name:
    print(nm)
