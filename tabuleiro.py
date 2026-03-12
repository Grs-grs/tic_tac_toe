class Tabuleiro():
    def __init__(self):
        self.grid = [
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "],
        ]

    def tabuleiro_get(self) -> str:
        resultado = ""
        for linha in self.grid:
            resultado += " | ".join(linha) + "\n"
        return resultado
    
    def validador_de_posicao(self, linha : int, coluna : int) -> bool:
        if (0 <= linha < 3) and (0 <= coluna < 3) and (self.grid[linha][coluna] == " "):
            return True
        else:
            return False

    def jogar(self, linha:int, coluna : int, token:str):
        if self.validador_de_posicao(linha,coluna) == False:
            raise ValueError("Jogada inválida")

        self.grid[linha][coluna] = token

    def verificar_vitoria(self, token: str) -> bool: 
        linhas = self.grid
        colunas = []
        
        for i in range(3):
            coluna = [self.grid[0][i], self.grid[1][i], self.grid[2][i]]
            colunas.append(coluna)

        diagonal_1 = [self.grid[0][0],self.grid[1][1], self.grid[2][2]]
        diagonal_2 = [self.grid[0][2], self.grid[1][1], self.grid[2][0]]
        combinacoes = linhas + colunas + [diagonal_1, diagonal_2]

        for combinacao in combinacoes:
            venceu = True
            for casa in combinacao:
                if casa != token:
                    venceu = False
                    break
            if venceu:
                return True
        return False

    def verificar_empate(self) -> bool:
        for linha in range(3):
            for coluna in range(3):
                if self.grid[linha][coluna] == " ":
                    return False
        return True

    def tabuleiro_set(self, linha : int, coluna : int, token : str):
        self.grid[linha][coluna] = token
        return None