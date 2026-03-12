from pessoa import Pessoa
from tabuleiro import Tabuleiro
from motor import Motor

class Game:
    def __init__(self):
        jogador_a = Pessoa(input("Nome do jogador 1: "), None)
        jogador_b = Pessoa(input("Nome do jogador 2: "), None)
        tabuleiro = Tabuleiro()
        self.motor = Motor(jogador_a, jogador_b, tabuleiro)

    def iniciar(self):
        self.motor.selecao_aleatoria_token()
        print(f"{self.motor.jogadores[0].nome} começa com {self.motor.jogadores[0].token}")

        while True:
            print("\n" + self.motor.tabuleiro.tabuleiro_get())
            jogador = self.motor.jogador_atual()

            try:
                linha = int(input(f"{jogador.nome}, linha (1-3): ")) - 1
                coluna = int(input(f"{jogador.nome}, coluna (1-3): ")) - 1

                status, vencedor = self.motor.realizar_jogada(linha, coluna)

            except ValueError as e:
                print(f"Erro: {e}")
                continue

            if status == "vitoria":
                print("\n" + self.motor.tabuleiro.tabuleiro_get())
                print(f"\n{vencedor.nome} venceu!")
                break

            if status == "empate":
                print("\n" + self.motor.tabuleiro.tabuleiro_get())
                print("\nEmpate!")
                break


if __name__ == "__main__":
    Game().iniciar()