def verificar_letra_a(texto):
    contagem = texto.lower().count('a')
    
    if contagem > 0:
        return f"a letra 'a' aparece {contagem} vezes no texto."
    else:
        return "a letra 'a' não foi encontrada no texto."

texto = input("informe um texto para verificarmos a presença da letra 'a': ")

print(verificar_letra_a(texto))
