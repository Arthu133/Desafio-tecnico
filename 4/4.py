def completar_sequencia():
    # sequências
    a = [1, 3, 5, 7]         # números ímpares
    b = [2, 4, 8, 16, 32, 64]  # potências de 2
    c = [0, 1, 4, 9, 16, 25, 36]  # Quadrados perfeitos
    d = [4, 16, 36, 64]      # Quadrados perfeitos de números pares
    e = [1, 1, 2, 3, 5, 8]   # Fibonacci
    f = [2, 10, 12, 16, 17, 18, 19]  # padrão misto

    # calculando os próximos números de cada sequência com base na lógica identificada
    proximo_a = a[-1] + 2  # números ímpares: adicionar 2 ao último número
    proximo_b = b[-1] * 2  # potências de 2: multiplicar o último número por 2
    proximo_c = (len(c))**2  # quadrados perfeitos: o próximo é o quadrado do próximo número na sequência
    proximo_d = (len(d) * 2) ** 2  # quadrados perfeitos de números pares
    proximo_e = e[-1] + e[-2]  # Fibonacci: soma dos dois últimos números
    proximo_f = 20  # sequência misturada: número consecutivo após 19 é 20

    # Exibindo os resultados
    print(f"Próximo número da sequência a) {a} é {proximo_a}")
    print(f"Próximo número da sequência b) {b} é {proximo_b}")
    print(f"Próximo número da sequência c) {c} é {proximo_c}")
    print(f"Próximo número da sequência d) {d} é {proximo_d}")
    print(f"Próximo número da sequência e) {e} é {proximo_e}")
    print(f"Próximo número da sequência f) {f} é {proximo_f}")

completar_sequencia()
