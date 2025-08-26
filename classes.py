import time
import os
class Livro:
    def __init__(self, titulo, autor, ano, categoria):
        self.__titulo = titulo
        self.__autor = autor
        self.__ano = ano
        self.__categoria = categoria
        self.__disponibilidade = True

    def emprestar(self):
        if self.__disponibilidade == True:
            self.__disponibilidade = False
            print(f"Você emprestou '{self.__titulo}'")
            print()
            os.system("pause")
        else:
            print(f"'{self.__titulo}' já está emprestado!")
            print()
            os.system("pause")

    def devolver(self):
        if self.__disponibilidade == False:
            self.__disponibilidade = True
            print(f"Você devolveu este livro '{self.__titulo}'")
            print()
            os.system("pause")
        else:
            print(f"'{self.__titulo}' já está disponível!")
            print()
            os.system("pause")

    # ---------------- get ------------------------------
    def getTitulo(self):
        return self.__titulo

    def getAutor(self):
        return self.__autor

    def getAno(self):
        return self.__ano

    def getCategoria(self):
        return self.__categoria

    def getDisponibilidade(self):
        return self.__disponibilidade

    # ---------------- set -------------------------
    def setTitulo(self, titulo):
        self.__titulo = titulo

    def setAutor(self, autor):
        self.__autor = autor

    def setAno(self, ano):
        self.__ano = ano

    def setCategoria(self, categoria):
        self.__categoria = categoria

    def setDisponibilidade(self, disponibilidade):
        self.__disponibilidade = disponibilidade


class Biblioteca:
    def __init__(self):
        self.__livros = [
    Livro("1984", "George Orwell", 1949, "Distopia"),
    Livro("O Senhor dos Anéis", "Tolkien", 1954, "Fantasia"),
    Livro("Harry Potter e a Pedra Filosofal", "J.K. Rowling", 1997, "Fantasia"),
    Livro("Dom Quixote", "Miguel de Cervantes", 1605, "Clássico"),
    Livro("O Pequeno Príncipe", "Antoine de Saint-Exupéry", 1943, "Infantil"),
    Livro("Moby Dick", "Herman Melville", 1851, "Aventura"),
    Livro("Orgulho e Preconceito", "Jane Austen", 1813, "Romance"),
    Livro("O Hobbit", "Tolkien", 1937, "Fantasia"),
    Livro("O Código Da Vinci", "Dan Brown", 2003, "Suspense"),
    Livro("A Revolução dos Bichos", "George Orwell", 1945, "Satírico"),
    Livro("O Alquimista", "Paulo Coelho", 1988, "Ficção"),
    Livro("Cem Anos de Solidão", "Gabriel García Márquez", 1967, "Realismo Mágico"),
    Livro("O Morro dos Ventos Uivantes", "Emily Brontë", 1847, "Romance"),
    Livro("O Grande Gatsby", "F. Scott Fitzgerald", 1925, "Romance"),
    Livro("O Sol é Para Todos", "Harper Lee", 1960, "Romance"),
    Livro("A Menina que Roubava Livros", "Markus Zusak", 2005, "Ficção"),
    Livro("O Guia do Mochileiro das Galáxias", "Douglas Adams", 1979, "Ficção Científica"),
    Livro("Alice no País das Maravilhas", "Lewis Carroll", 1865, "Infantil"),
    Livro("Frankenstein", "Mary Shelley", 1818, "Terror"),
    Livro("Drácula", "Bram Stoker", 1897, "Terror"),
    Livro("O Perfume", "Patrick Süskind", 1985, "Suspense"),
    Livro("A Cabana", "William P. Young", 2007, "Ficção"),
    Livro("O Diário de Anne Frank", "Anne Frank", 1947, "Biografia"),
    Livro("Jogos Vorazes", "Suzanne Collins", 2008, "Distopia"),
    Livro("Crepúsculo", "Stephenie Meyer", 2005, "Romance")
]
    # get
    def getLivros(self):
        return self.__livros
    
    # set
    def setLivros(self, livros):
        self.__livros = livros
    
    # ---------------------------------metodos-------------------------------
    def cadastrar(self):
        os.system("cls")
        print("Você está na tela de cadastro de livro.\n")
        print("---------------------------------------------------------\n")
        qtd_livros = int(input("Quantos livros deseja cadastrar?\n-> "))
        for i in range(qtd_livros):
            titulo = input(f"DIGITE O NOME DO {i+1}º LIVRO: ")    
            autor = input(f"DIGITE O AUTOR(A) DO {i+1}º LIVRO: ")
            ano = int(input(f"DIGITE O ANO DO {i+1}º LIVRO: "))
            categoria = input(f"DIGITE A CATEGORIA DO {i+1}º LIVRO: ")
                        
            while True:
                disponibilidade = input("DIGITE s/n PARA A DISPONIBILIDADE DO LIVRO: ").lower()
                if disponibilidade == 's':
                    t_ou_f = True
                    break
                elif disponibilidade == 'n':
                    t_ou_f = False
                    break
                else:
                    print("DIGITE SOMENTE s OU n")
            livro = Livro(titulo, autor, ano, categoria)
            livro.setDisponibilidade(t_ou_f)
            self.__livros.append(livro)
            print("---------------------------------------------------------\n")
            
        print("LIVROS CADASTRADOS COM SUCESSO")
        print()
        os.system("pause")
    
    # --------------------------------------------------------------------------------
    def qual_listar(self):
        while True:
            print("\nVocê está na tela de listar.\n")
            print("---------------------------------------------------------\n")
            print("ESCOLHA UMA OPÇÃO: ")
            qual = int(input("1- LISTAR NORMALMENTE\n2- LISTAR POR CATEGORIA\n3- LISTAR POR AUTOR\n4- LISTAR POR EMPRESTADOS\n5- VOLTAR\n-> "))
            if qual == 1:
                self.listar()
            elif qual == 2:
                self.listar_categoria()
            elif qual == 3:
                self.listar_autor()
            elif qual == 4:
                self.listar_emprestados()
            elif qual == 5:
                break
            else:
                print("Escolha so o 1, 2 ou 3")
                print()
                os.system("pause")
    
    # -----------------------------------------------------------------------------------------
    def listar(self):
        os.system("cls")
        print("Você está na tela listar.\n")
        print("---------------------------------------------------------\n")
        if not self.__livros:
            print("Nenhum livro cadastrado")
            return
            
        for livro in self.__livros:
            status = "Disponível" if livro.getDisponibilidade() else "Emprestado"
            print(f"{livro.getTitulo()} - {livro.getAutor()} ({livro.getAno()}) - {livro.getCategoria()} | [{status}]")
        
        print()
        os.system("pause")
    # --------------------------------------------------------------------------------------------
    def listar_categoria(self):
        os.system("cls")
        print("Você está na parte de listar por categoria.\n")
        print("---------------------------------------------------------\n")
        categoria = input("DIGITE A CATEGORIA: ")
        lista_categoria = []
        for livro in self.__livros:
            if livro.getCategoria().lower() == categoria.lower():
                lista_categoria.append(livro)
        
        if not lista_categoria:
            print(f"Nenhum livro encontrado na categoria '{categoria}'")
            return
            
        for livro in lista_categoria:
            if livro.getDisponibilidade() == True:
                status = "Disponivel"
            else:
                status = "Emprestado"
            print(f"{livro.getTitulo()} - {livro.getAutor()} ({livro.getAno()}) | [{status}]")
        print()
        os.system("pause")

    def listar_autor(self):
        os.system("cls")
        print("Você está na parte de listar por autor.\n")
        print("---------------------------------------------------------\n")
        autor = input("DIGITE O AUTOR: ")
        lista_autor = []
        
        for livro in self.__livros:
            if livro.getAutor().lower() == autor.lower():
                lista_autor.append(livro)
        
        if not lista_autor:
            print(f"Nenhum livro encontrado com esse '{autor}'")
            return
            
        for livro in lista_autor:
            if livro.getDisponibilidade() == True:
                status = "Disponivel"
            else:
                status = "Emprestado"
            print(f"{livro.getTitulo()} - {livro.getCategoria()} ({livro.getAno()}) | [{status}]")
        os.system("pause")

    def listar_emprestados(self):
        os.system("cls")
        print("Você está na parte de listar por emprestados.\n")
        print("---------------------------------------------------------\n")
        lista_emprestados = []
        for livro in self.__livros:
            if livro.getDisponibilidade() == False:
                lista_emprestados.append(livro)
        
        if not lista_emprestados:
            print(f"Nenhum livro encontrado está emprestado")
            print()
            os.system("pause")
            return
            
        for livro in lista_emprestados:
            print(f"{livro.getTitulo()} - {livro.getCategoria()} - {livro.getAutor()} ({livro.getAno()})")
        print()
        os.system("pause")      
    # -------------------------------------------------------------------
    def atualizar_livros(self):
        atualizar_livro = input("Digite o nome do livro que deseja atualizar: ")

        livro_encontrado = None
        for livro in self.__livros:
            if livro.getTitulo().lower() == atualizar_livro.lower():
                livro_encontrado = livro
                break
        
        if livro_encontrado is None:
            print("Livro não encontrado!")
            return
        
        novo_autor = input("Atualize o autor do livro (Enter para manter atual):\n---> ")
        novo_titulo = input("Atualize o título do livro (Enter para manter atual):\n---> ")
        novo_ano = input("Atualize o ano do livro (Enter para manter atual):\n---> ")
        nova_categoria = input("Atualize a categoria do livro (Enter para manter atual):\n---> ")

        if novo_autor != "":
            livro_encontrado.setAutor(novo_autor)
        if novo_titulo != "":
            livro_encontrado.setTitulo(novo_titulo)
        if novo_ano != "":
            livro_encontrado.setAno(int(novo_ano))
        if nova_categoria != "":
            livro_encontrado.setCategoria(nova_categoria)
        
        print(f"Livro '{livro_encontrado.getTitulo()}' atualizado com sucesso!")
        print()
        os.system("pause")

    def excluir(self):
        titulo = input("Digite o título do livro que deseja excluir: ")
        for livro in self.__livros:
            if livro.getTitulo().lower() == titulo.lower():
                self.__livros.remove(livro)
                print(f"O livro '{titulo}' foi removido com sucesso!")
                time.sleep(2)
                return
        print("Livro não encontrado!")
        print()
        os.system("pause")

    def emprestar_livro(self):
        titulo = input("Digite o título do livro para empréstimo: ")
        for livro in self.__livros:
            if livro.getTitulo().lower() == titulo.lower():
                livro.emprestar() 
                return
        print("Livro não encontrado")
        print()
        os.system("pause")

    def devolver_livro(self):
        titulo = input("Digite o título do livro para devolução: ")
        for livro in self.__livros:
            if livro.getTitulo().lower() == titulo.lower():
                livro.devolver()  
                return
        print("Livro não encontrado")
        print()
        os.system("pause")