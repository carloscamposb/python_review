def calculate_love_score(name1, name2):
    # Removendo espaços e convertendo para maiúsculas
    name1 = name1.replace(" ", "").upper()
    name2 = name2.replace(" ", "").upper()
    
    # Concatenando os nomes
    name_all = name1 + name2
    print(f"Nomes combinados: {name_all}")

    word1 = 'TRUE'
    word2 = 'LOVE'

    sum_num1 = 0
    sum_num2 = 0

    # Contando letras da palavra "TRUE"
    print("\nContagem para 'TRUE':")
    for letter in word1:
        count = name_all.count(letter)
        sum_num1 += count  # Soma acumulada
        

    print(f"Soma final para 'TRUE': {sum_num1}")

    # Contando letras da palavra "LOVE"
    print("\nContagem para 'LOVE':")
    for letter in word2:
        count = name_all.count(letter)
        sum_num2 += count  # Soma acumulada
   

    print(f"Soma final para 'LOVE': {sum_num2}")

    # Criando a pontuação final
    score_love = int(f"{sum_num1}{sum_num2}")
    
    print(f"\nTotal: {score_love}")

# Testando
calculate_love_score(name1='Carlos Campos', name2='Fabian Giovanni')
