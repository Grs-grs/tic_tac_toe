import pytest
from tabuleiro import Tabuleiro


def test_tabuleiro_inicia_vazio():
    tabuleiro = Tabuleiro()
    assert tabuleiro.grid == [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "],
    ]


def test_jogada_valida_preenche_posicao():
    tabuleiro = Tabuleiro()
    tabuleiro.jogar(0, 0, "X")
    assert tabuleiro.grid[0][0] == "X"


def test_nao_permite_jogar_em_casa_ocupada():
    tabuleiro = Tabuleiro()
    tabuleiro.jogar(0, 0, "X")

    with pytest.raises(ValueError):
        tabuleiro.jogar(0, 0, "O")


def test_detecta_vitoria_horizontal():
    tabuleiro = Tabuleiro()
    tabuleiro.jogar(0, 0, "X")
    tabuleiro.jogar(0, 1, "X")
    tabuleiro.jogar(0, 2, "X")

    assert tabuleiro.verificar_vitoria("X") is True


def test_detecta_empate():
    tabuleiro = Tabuleiro()
    jogadas = [
        (0, 0, "X"), (0, 1, "O"), (0, 2, "X"),
        (1, 0, "X"), (1, 1, "O"), (1, 2, "O"),
        (2, 0, "O"), (2, 1, "X"), (2, 2, "X"),
    ]

    for linha, coluna, token in jogadas:
        tabuleiro.jogar(linha, coluna, token)

    assert tabuleiro.verificar_empate() is True