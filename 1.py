def fibonacci_sequencia(limite):
    sequencia = [0, 1]
    while sequencia[-1] < limite:
        sequencia.append(sequencia[-1] + sequencia[-2])
    return sequencia

def checagem(num):
    sequencia = fibonacci_sequencia(num)
    if num in sequencia:
        return f"O número {num} pertence a sequência de Fibonacci."
    else:
        return f"O número {num} não pertence a sequência de Fibonacci."

# Solicita ao usuário um número para verificar
num = int(input("Informe um número: "))
print(checagem(num))
