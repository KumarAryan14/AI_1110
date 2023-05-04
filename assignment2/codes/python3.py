import random as r

l1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


l2 = list(l1)
x1 = r.choice(l2)
l2.remove(x1)
x2 = r.choice(l2)
l2.remove(x2)
x3 = r.choice(l2)
l2.remove(x3)
x4 = r.choice(l2)

print('Let the password be :',x1,x2,x3,x4)

simul = 1555559
j = 0

ans = x1*1000+x2*100+x3*10+x4
number = 0
for i in range(0, simul):
    l3 = list(l1)
    t1 = r.choice(l3)
    l3.remove(t1)
    t2 = r.choice((l3))
    l3.remove(t2)
    t3 = r.choice(l3)
    l3.remove(t3)
    t4 = r.choice(l3)
    number = t1*1000+t2*100+t3*10+t4
    password = x1*1000+x2*100+x3*10+x4
    if number == password:
        j = j +1

print('Probability : ',j/simul)

