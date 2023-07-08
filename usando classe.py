class Aluno:
    def __init__(self, nome, idade, serie):
        self.nome = nome
        self.idade = idade
        self.serie = serie

    def exibir(self):
        return f"{self.nome} - {self.idade} - {self.serie}"

class Escola:
    def __init__(self, nome, cnpj):
        self.nome = nome
        self.cnpj = cnpj
        self.alunos = []

    def adicionar(self, aluno):
        self.alunos.append(aluno)

    def exibir_alunos(self):
        for al in self.alunos:
            print(f'{al.nome} ')

escola = Escola('Cooepar', 1213313)

for i in range(3):
    nome = input()
    idade = input()
    serie = input()
    aluno = Aluno(nome,idade,serie)
    escola.adicionar(aluno)
    


print(escola.exibir_alunos())
