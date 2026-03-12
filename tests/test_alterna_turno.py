from pessoa import Pessoa
from tabuleiro import Tabuleiro
from motor import Motor


def test_motor_alterna_turno_apos_jogada():
    jogador_a = Pessoa("A", "X")
    jogador_b = Pessoa("B", "O")
    tabuleiro = Tabuleiro()
    motor = Motor(jogador_a, jogador_b, tabuleiro)

    motor.jogadores = [jogador_a, jogador_b]
    motor.turno = 0

    status, _ = motor.realizar_jogada(0, 0)

    assert status == "continua"
    assert motor.turno == 1
    assert motor.jogador_atual() == jogador_b