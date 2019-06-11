def main():
    recursos_disponiveis = [4, 2, 1, 1]
    recursos_alocados = [['c1', 2, 1, 0, 1],
                         ['c2', 0, 1, 1, 0],
                         ['c3', 1, 0, 1, 0],
                         ['c4', 1, 0, 0, 1],
                         ['c5', 0, 1, 1, 0]]
    recursos_necessarios = [['c1', 4, 2, 0, 1],
                            ['c2', 3, 2, 1, 3],
                            ['c3', 4, 1, 2, 1],
                            ['c4', 2, 2, 1, 0],
                            ['c5', 3, 2, 1, 4]]
    verifica(recursos_disponiveis, recursos_alocados, recursos_necessarios)


def verifica(recursos_disponiveis, recursos_alocados, recursos_necessarios):
    while True:
        qtd = len(recursos_alocados)
        processos_alocados_terminados = []
        processos_rec_nescesario_terminados = []
        for j in range(len(recursos_alocados)):
            processo_rec_alocado = recursos_alocados[j]
            processo_rec_necessario = recursos_necessarios[j]
            cont = 0
            novos_recursos_disponiveis = []
            for i in range(1, len(processo_rec_alocado)):
                # if processo_rec_necessario[i] - processo_rec_alocado[i] <= recursos_disponiveis[i - 1]:
                if processo_rec_alocado[i] + recursos_disponiveis[i - 1] >= processo_rec_necessario[i]:
                    cont += 1
                    novos_recursos_disponiveis.append(recursos_disponiveis[i - 1] + processo_rec_alocado[i])
            if cont == len(recursos_disponiveis):
                recursos_disponiveis = novos_recursos_disponiveis
                processos_alocados_terminados.append(processo_rec_alocado)
                processos_rec_nescesario_terminados.append(processo_rec_necessario)
                print("O Processo", processo_rec_alocado[0], "terminou com sucesso")

        for k in range(len(processos_alocados_terminados)):
            recursos_alocados.remove(processos_alocados_terminados[k])
            recursos_necessarios.remove(processos_rec_nescesario_terminados[k])
        if len(recursos_alocados) == qtd or len(recursos_alocados) == 0:
            if len(recursos_alocados) == 0:
                print("Terminou com sucesso todos os processos")
            else:
                for i in range(len(recursos_alocados)):
                    print("O processo", recursos_alocados[i][0], "esta em Deadlock")
            break


if __name__ == '__main__':
    main()
