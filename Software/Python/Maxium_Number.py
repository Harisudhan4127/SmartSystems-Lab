'''x = input()
y = []
x = x.split(" ")

for i in x:
    y.append(int(i))

lager = y[0]
for val in y:
    if val > lager:
        lager = val

print(lager)
'''
'''
x = input()
length = len(x)
for i in range(length+1):
    if i%2 !=0:
        print(x[i-1],end="")
'''

x = input()
x = x.replace("s","S")
x = x.replace("r","R")
print(x)
