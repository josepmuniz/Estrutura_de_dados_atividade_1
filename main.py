from vetor import Vetor
from aluno import Aluno

def testa_vetor():

    aluno1 = Aluno("Júnior")
    print(aluno1)
    aluno2 = Aluno("Muniz")
    print(aluno2)

    vetor_alunos = Vetor()
    vetor_alunos.adiciona_fim(aluno1)
    vetor_alunos.adiciona_fim(aluno2)

    print(vetor_alunos)
    print(vetor_alunos.contem(aluno1))
    print(vetor_alunos.pega(1))

if __name__ == '__main__':
    testa_vetor()

