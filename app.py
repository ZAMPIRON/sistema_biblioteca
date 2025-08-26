import time # importei a biblioteca time
import os # importei a biblioteca os
from classes import Biblioteca
biblioteca = Biblioteca()

while True:                   # criação do menu
    os.system("cls")
    print("BEM VINDO AO MENU!")
    print(30*"- ")
    time.sleep(1)
    print("Você está no sistema da biblioteca, selecione uma opção.")
    print()
    time.sleep(1)

    print("1- CADASTRO DE LIVRO \n2- EMPRESTAR LIVRO \n3- LISTAR \n4- ATUALIZAR \n5- EXCLUIR \n6- DEVOLVER \n0- SAIR")
    

    escolha = int(input("--> "))
    time.sleep(1)

    if escolha == 1:        # opção de cadastro
        biblioteca.cadastrar()

    elif escolha == 2:
        biblioteca.emprestar_livro()
        
    elif escolha == 3:
        biblioteca.qual_listar()
        
    elif escolha == 4:
        biblioteca.atualizar_livros()

    elif escolha == 5:
        biblioteca.excluir()
    
    elif escolha == 6:
        biblioteca.devolver_livro()

    elif escolha == 0:
        print("SAINDO...")
        time.sleep(1)
        os.system("pause")

        break

    else:
        print("ESCOLHA INVALIDA")
        time.sleep(1)
        os.system("pause")
