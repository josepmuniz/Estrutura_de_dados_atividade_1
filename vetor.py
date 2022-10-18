import copyreg

from aluno import Aluno

class Vetor:
    def __init__(self):
        self.__alunos = [None] * 10
        self.__total_de_alunos = 0

    def adiciona_comeco(self, aluno):
        pass

    def adiciona_fim(self, aluno):
        self.__alunos[self.__total_de_alunos] = aluno
        self.__total_de_alunos += 1


    def adiciona_posicao(self, aluno, posicao):
        if posicao == 0:
            self.adiciona_fim(aluno)
        elif posicao == self.__total_de_alunos:
            self.adiciona_fim(aluno)
        else:

            anterior = self.pega(posicao - 1)

            nova = Aluno(anterior.proxima, aluno)
            anterior.proxima = nova

            self.__total_de_alunos += 1


    def pega(self, posicao):
        if posicao>self.__total_de_alunos:
            return "ERRO"
        return self.__alunos[posicao]

    def remove(self, aluno):
        if self.contem(aluno):
            numero_aluno = self.adiciona_fim(aluno)
            lista_aluno = self.__total_de_alunos[numero_aluno]
            lista_aluno.remove(aluno)

            self.__total_de_alunos -= 1

    def remover_posicao(self, posicao, aluno):
        if posicao == 0:
            self.adiciona_fim(aluno)

        else:

            self.adiciona_posicao -= 1

        return self.adiciona_posicao(aluno, posicao)



    def remover_elemento(self, aluno):
        self.__alunos[self.__total_de_alunos] = aluno
        self.__total_de_alunos -= 1

    def remover_todos_elementos(self, aluno):
        a = self.__total_de_alunos
        a.clear(aluno)

    def contem(self,aluno):
        for index in range(self.__total_de_alunos):
            if(aluno == self.__alunos[index]):
                return True

        return False

    def tamanho(self):
        return self.__total_de_alunos

    def __str__(self):
        ret = ' '.join(str(elemento) for elemento in self.__alunos)
        return ret