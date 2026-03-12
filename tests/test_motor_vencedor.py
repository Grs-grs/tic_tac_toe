from pessoa import Pessoa
from tabuleiro import Tabuleiro
from motor import Motor




def test_motor_retorna_vencedor():
    jogador_a = Pessoa("A", "X")
    jogador_b = Pessoa("B", "O")
    tabuleiro = Tabuleiro()
    motor = Motor(jogador_a, jogador_b, tabuleiro)

    motor.jogadores = [jogador_a, jogador_b]
    motor.turno = 0

    motor.realizar_jogada(0, 0)  # A
    motor.realizar_jogada(1, 0)  # B
    motor.realizar_jogada(0, 1)  # A
    motor.realizar_jogada(1, 1)  # B
    status, vencedor = motor.realizar_jogada(0, 2)  # A vence

    assert status == "vitoria"
    assert vencedor == jogador_a