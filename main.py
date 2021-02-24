a = open('A.txt','r')
A = a.read()

b = open('B.txt','r')
B = b.read()

a = open('A.txt','w')
a.write(B)

b = open('B.txt','w')
b.write(A)

