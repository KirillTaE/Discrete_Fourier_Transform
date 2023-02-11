from sympy import *

abc = str("абвгдеёжзийклмнопрстуфхцчшщъыьэюя")

#print('Размер матрицы перехода:')
#n = int(input())

print('1-ввести слово, 2-ввести вектор (числа):')

vbr = int(input())
if vbr == 1:
    print('Введите букавы (русские):')
    vec = Matrix()
    slovo = str(input()).lower().replace(' ', '')
    n=len(slovo)
    ggg = []

    for i in range(len(slovo)):
        ggg.append(abc.index(slovo[i]) + 1)

    print(ggg)
    vec = vec.col_insert(0, ggg)

elif vbr == 2:
    print('Введите вектор (числа через пробел):')
    vec = Matrix()
    masv=list(map(int, input().split()))
    n=len(masv)
    vec = vec.col_insert(0, masv)

else:
    print('Дурак?')
    exit(0)

b = exp((-2 * pi * I) / n)

a = [[] for i in range(n)]
for i in range(n):
    for j in range(n):
        a[i].append((b ** ((i) * (j))).rewrite(cos).simplify())

print()

matPer = Matrix(a)
print('Матрица перехода:')
# print(matPer)
print(*a, sep='\n')

print()

W = matPer * vec

for i in range(n):
    pair = W[i].as_real_imag()
    W[i] = pair[0] + pair[1] * I

print('Ответ:  и все это умножить на 1/8')
for i in range(n):
    print(W[i])

for i in range(n):
    W[i]=W[i]/8

#####-------------------------------------------

a1 = [[] for i in range(n)]
for i in range(n):
    for j in range(n):
        a1[i].append(conjugate((b ** ((i) * (j))).rewrite(cos).simplify()))

print()

matPer1 = Matrix(a1)
print('Матрица перехода для обратного преобразования:')
# print(matPer)
print(*a1, sep='\n')

print()

W1 = matPer1 * W

'''
for i in range(n):
    pair = W1[i].as_real_imag()
    W1[i] = pair[0] + pair[1] * I
'''

for i in range(n):
    W1[i]=(W1[i].simplify())

for i in range(n):
    print(W1[i])



###----------------
print()
Wos=Matrix([[100/8], [0], [-17+7*I], [0], [0], [0], [-17-7*I], [0]])

Zos=matPer1 * Wos

for i in range(n):
    Zos[i]=(Zos[i].simplify())

print('Значения после манипуляций:')
for i in range(n):
    print(Zos[i])