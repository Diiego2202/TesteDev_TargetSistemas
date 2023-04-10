n = int(input("Informe um número: "))

fibo = [0, 1]

while fibo[-1] < n:
    aux = fibo[-1] + fibo[-2]
    fibo.append(aux)

if n in fibo:
    print(n, "pertence à sequência")
else:
    print(n, "não pertence à sequência")
