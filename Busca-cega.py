# exemplo mais simples de busca: busca cega
# busca em arvore do tipo FIFO, retorna sempre a solução ótima
# o algoritmo abaixo resolve o quebra cabeça de 8 peças

class NODO:
    def __init__(self, estado, pai, acao):
        self.estado = estado
        self.pai = pai
        self.acao = acao
    
def testeObjetivo(tabuleiro):
    return (tabuleiro == [[1, 2, 3], [4, 5, 6], [7, 8, 0]])

def moveBaixo(problema, borda, linha, coluna):
    aux = NODO([row[:] for row in problema.estado], problema, "b")
    aux.estado[linha][coluna] = problema.estado[linha+1][coluna]
    aux.estado[linha+1][coluna] = problema.estado[linha][coluna]
    borda.append(aux)

def moveCima(problema, borda, linha, coluna):
    aux = NODO([row[:] for row in problema.estado], problema, "c")
    aux.estado[linha][coluna] = problema.estado[linha-1][coluna]
    aux.estado[linha-1][coluna] = problema.estado[linha][coluna]
    borda.append(aux)

def moveDireita(problema, borda, linha, coluna):
    aux = NODO([row[:] for row in problema.estado], problema, "d")
    aux.estado[linha][coluna] = problema.estado[linha][coluna+1]
    aux.estado[linha][coluna+1] = problema.estado[linha][coluna]
    borda.append(aux)

def moveEsquerda(problema, borda, linha, coluna):
    aux = NODO([row[:] for row in problema.estado], problema, "e")
    aux.estado[linha][coluna] = problema.estado[linha][coluna-1]
    aux.estado[linha][coluna-1] = problema.estado[linha][coluna]
    borda.append(aux)

def funcaoSucessora(problema, borda):
    for linha in range(3):
        for coluna in range(3):
            if(problema.estado[linha][coluna] == 0):
                if(linha == 0 and coluna == 0):
                    if(not(problema.acao == 'c')):
                        moveBaixo(problema, borda, linha, coluna)
                    if(not(problema.acao == 'e')):
                        moveDireita(problema, borda, linha, coluna)
                if(linha == 0 and coluna == 1):
                    if(not(problema.acao == 'd')):
                        moveEsquerda(problema, borda, linha, coluna)
                    if(not(problema.acao == 'c')):
                        moveBaixo(problema, borda, linha, coluna)
                    if(not(problema.acao == 'e')):
                        moveDireita(problema, borda, linha, coluna)
                if(linha == 0 and coluna == 2):
                    if(not(problema.acao == 'd')):
                        moveEsquerda(problema, borda, linha, coluna)
                    if(not(problema.acao == 'c')):
                        moveBaixo(problema, borda, linha, coluna)
                if(linha == 1 and coluna == 0):
                    if(not(problema.acao == 'b')):
                        moveCima(problema, borda, linha, coluna)
                    if(not(problema.acao == 'e')):
                        moveDireita(problema, borda, linha, coluna)
                    if(not(problema.acao == 'c')):
                        moveBaixo(problema, borda, linha, coluna)
                if(linha == 1 and coluna == 1):
                    if(not(problema.acao == 'd')):
                        moveEsquerda(problema, borda, linha, coluna)
                    if(not(problema.acao == 'c')):
                        moveBaixo(problema, borda, linha, coluna)
                    if(not(problema.acao == 'e')):
                        moveDireita(problema, borda, linha, coluna)
                    if(not(problema.acao == 'b')):
                        moveCima(problema, borda, linha, coluna)
                if(linha == 1 and coluna == 2):
                    if(not(problema.acao == 'b')):
                        moveCima(problema, borda, linha, coluna)
                    if(not(problema.acao == 'd')):
                        moveEsquerda(problema, borda, linha, coluna)
                    if(not(problema.acao == 'c')):
                        moveBaixo(problema, borda, linha, coluna)
                if(linha == 2 and coluna == 0):
                    if(not(problema.acao == 'b')):
                        moveCima(problema, borda, linha, coluna)
                    if(not(problema.acao == 'e')):
                        moveDireita(problema, borda, linha, coluna)
                if(linha == 2 and coluna == 1):
                    if(not(problema.acao == 'd')):
                        moveEsquerda(problema, borda, linha, coluna)
                    if(not(problema.acao == 'b')):
                        moveCima(problema, borda, linha, coluna)
                    if(not(problema.acao == 'e')):
                        moveDireita(problema, borda, linha, coluna)
                if(linha == 2 and coluna == 2):
                    if(not(problema.acao == 'd')):
                        moveEsquerda(problema, borda, linha, coluna)
                    if(not(problema.acao == 'b')):
                        moveCima(problema, borda, linha, coluna)
                break

def retornaSolucao(tabuleiro):
    solucao = []

    while(tabuleiro):
        solucao.insert(0, tabuleiro)
        tabuleiro = tabuleiro.pai
    
    while(len(solucao)):
        aux = solucao.pop()
        print(aux.estado[0])
        print(aux.estado[1])
        print(aux.estado[2])
        print("_________________")

def buscaEmArvore(problema):
    borda = [problema]
    
    while(len(borda) != 0):
        tabuleiro = borda.pop(0)
        if(testeObjetivo(tabuleiro.estado)): 
            retornaSolucao(tabuleiro)
            exit(0)
        funcaoSucessora(tabuleiro, borda)
        print(str(len(borda))+' iterações')

problema = NODO([[5,3,6],[0,1,8],[2,4,7]], None, '')
buscaEmArvore(problema)
