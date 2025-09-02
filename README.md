# Sistema de Biblioteca (Python)
Este é um projeto simples de Sistema de Biblioteca desenvolvido em Python para fins didáticos.
O objetivo é praticar programação orientada a objetos (POO) e manipulação de listas/dicionários.

## A aplicação foi estruturada em dois arquivos principais:

app.py → responsável pelo menu interativo e pela interação com o usuário.

classes.py → contém as classes Livro e Biblioteca, responsáveis por toda a lógica do sistema.

## Como funciona?
### 1. Arquivo app.py

O app.py funciona como o programa principal da aplicação.

Cria uma instância da classe Biblioteca.

Exibe o menu interativo com opções numéricas.

Direciona cada escolha do usuário para o método correspondente da classe Biblioteca.

#### Fluxo do Menu:

Cadastrar Livro - biblioteca.cadastrar()

Emprestar Livro -  biblioteca.emprestar_livro()

Listar Livros - biblioteca.qual_listar()

Atualizar Livro - biblioteca.atualizar_livros()

Excluir Livro - biblioteca.excluir()

Devolver Livro - biblioteca.devolver_livro()

Sair - encerra o sistema

### 2. Arquivo classes.py

Esse arquivo concentra toda a lógica do sistema.
Ele contém duas classes principais:

#### Classe Livro

Representa um livro na biblioteca.

#### Atributos:
- titulo
- autor
- ano
- categoria
- disponibilidade (True = disponível, False = emprestado)

#### Métodos principais:

emprestar() = altera a disponibilidade para emprestado.

devolver() = altera a disponibilidade para disponível.

Métodos gets e sets para acessar e modificar atributos.

#### Classe Biblioteca

Gerencia a coleção de livros.
Ao iniciar, já possui alguns livros pré-cadastrados.

#### Principais métodos:

cadastrar() - permite adicionar novos livros ao sistema.

qual_listar() - abre um sub-menu para escolher como listar:

listar() - lista todos os livros.

listar_categoria() - filtra por categoria.

listar_autor() - filtra por autor.

listar_emprestados() - mostra apenas os emprestados.

atualizar_livros() - altera título, autor, ano ou categoria de um livro.

excluir() - remove um livro do acervo.

emprestar_livro() - registra o empréstimo de um livro.

devolver_livro() - registra a devolução.




## Autores
Projeto desenvolvido pelo G3 de desenvolvimentos de sistemas do SENAI.