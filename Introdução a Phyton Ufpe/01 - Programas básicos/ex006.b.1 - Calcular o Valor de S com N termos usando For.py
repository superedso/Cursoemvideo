#QUESTÃO 06: Calcular o valor da série com N termos utilizando for.
somapar = somaimpar = s = 0
impar = 2/500
par = 5/490
n = int(input('Digite a quantidade de termos da série:'))
while n < 0 or n > 50:
    n = int(input('Você digitou um número inválido, digite um novo número inteiro:'))
for c in range(1, n+1):
    print(f'o valor de {c}')
    if(c%2 == 1):
        somaimpar += 2/(500 - (c-1)*20)
        print(f'Soma dos números ímpares:{somaimpar} +')
    elif(c%2 == 0):
        somapar += 5/(490 - (c-2)*20)
        print(f'Soma dos números pares:{somapar} + ')
if n == 1:
    s = somaimpar
s = somaimpar - somapar
print(f'A soma total é: {s:.4f}')