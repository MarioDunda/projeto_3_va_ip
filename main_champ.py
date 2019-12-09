def main_champ():
    print("""
[ 1 ] - Simular campeonato
[ 2 ] - Ver tabela de classificação
[ 0 ] - Voltar
    """)
    menu = input("Digite uma opção: ")
    if(menu == "1"):
        print("simular")
    elif(menu == "2"):
        print("tabela")
    elif(menu == "0"):
        print("exit")
    else:
        print("""

Digite uma opção valida

        """)
