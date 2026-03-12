from pessoa import Pessoa
from tabuleiro import Tabuleiro
import random

class Motor():
    '''
    Esta classe serve como a Engine do jogo é aqui onde estão as regras e jogadas.
    '''
    def __init__(self, jogador_a, jogador_b, tabuleiro):
        self.jogador_a = jogador_a
        self.jogador_b = jogador_b
        self.jogadores = []
        self.tabuleiro = tabuleiro
        self.turno = 0

    def selecao_aleatoria_token(self):
        var_temp = random.randint(1,2)
        if var_temp == 1:
            self.jogador_a.token = "X"
            self.jogador_b.token = "O"
            self.jogadores = [self.jogador_a, self.jogador_b]
        else:
            self.jogador_b.token = "X"
            self.jogador_a.token = "O"
            self.jogadores = [self.jogador_b,self.jogador_a]
        self.turno = 0

    def jogador_atual(self) :
        return self.jogadores[self.turno]
    
    def realizar_jogada(self, linha : int, coluna: int):
        jogador = self.jogador_atual()
        self.tabuleiro.jogar(linha,coluna,jogador.token)

        if self.tabuleiro.verificar_vitoria(jogador.token):
            return "vitoria", jogador
        if self.tabuleiro.verificar_empate():
            return "empate", None
        self.turno = 1 - self.turno
        return "continua", None