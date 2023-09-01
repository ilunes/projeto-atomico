import time

tabela = {
    'H': {'q_ligacao_max': 1, 'quantidade': 5},
    'He': {'q_ligacao_max': 2, 'quantidade': 0},
    'C': {'q_ligacao_max': 4, 'quantidade': 0}
}

if __name__ == '__main__':

    start_time = time.time()

    moleculas = []
    elementos_molecula = []

    for elemento_tabela in tabela:
        #print(elemento_tabela)
        for quantidade in range(tabela[elemento_tabela]['quantidade']):
            elementos_molecula.append(elemento_tabela + '_' + str(quantidade))

    print(elementos_molecula)

    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Tempo de execução: {execution_time} segundos")
