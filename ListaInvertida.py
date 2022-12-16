class ListaInvertida:
    def __init__(self):
        # Inicializa os atributos 'data', 'lista_invertida' e 'diretorios'
        self.data = []
        self.lista_invertida = {}
        self.diretorios = ['nome', 'idade', 'time']

    def insersao(self, valores):
        # Adiciona o dicionário 'valores' na lista 'data' e chama o método 'monta_lista_invertida'
        self.data.append(valores)
        self.monta_lista_invertida()

    def monta_lista_invertida(self):
        """
        Percorre os valores de 'diretorios' e cria chaves no dicionário 'lista_invertida' para cada valor.
        Depois, percorre novamente 'diretorios' para criar as chaves no dicionário 'lista_invertida' para combinações de valores distintos.
        Por exemplo, se 'diretorios' for ['nome', 'idade', 'time'], serão criadas as chaves 'nome_idade', 'nome_time' e 'idade_time'.
        Depois, percorre cada linha em 'data' e cria ou atualiza as chaves em 'lista_invertida' com o índice da linha em 'data'.
        """
        # Percorre os valores de 'diretorios' e cria chaves no dicionário 'lista_invertida' para cada valor

        for diretorio in self.diretorios:
            self.lista_invertida[diretorio] = {}
            # Cria chaves no dicionário 'lista_invertida' para combinações de valores distintos em 'diretorios'
            for diretorio2 in self.diretorios:
                if diretorio != diretorio2:
                    lista_de_diretorios = [diretorio, diretorio2]
                    lista_de_diretorios.sort()
                    self.lista_invertida["_".join(lista_de_diretorios)] = {}
        # Percorre cada linha em 'data' e cria ou atualiza as chaves em 'lista_invertida' com o índice da linha em 'data'
        for index, linha in enumerate(self.data):
            for diretorio, valor in linha.items():
                if valor in self.lista_invertida[diretorio]:
                    self.lista_invertida[diretorio][valor].append(index)
                else:
                    self.lista_invertida[diretorio][valor] = [index]
                # Cria chaves no dicionário 'lista_invertida' para combinações de valores de diferentes chaves em 'linha'
                for diretorio2, valor2 in linha.items():
                    if diretorio != diretorio2:
                        lista_de_diretorios_e_seus_valores_ordenada = \
                            self.ordena_duas_listas_pelo_primeiro_item_da_lista([diretorio, valor],
                                                                                [diretorio2, valor2])
                        diretorios_ordenados = lista_de_diretorios_e_seus_valores_ordenada[0][0] + "_" + \
                                               lista_de_diretorios_e_seus_valores_ordenada[1][0]
                        valores_ordenados = lista_de_diretorios_e_seus_valores_ordenada[0][1] + "_" + \
                                            lista_de_diretorios_e_seus_valores_ordenada[1][1]
                        if valores_ordenados in self.lista_invertida[diretorios_ordenados]:
                            if index not in self.lista_invertida[diretorios_ordenados][valores_ordenados]:
                                self.lista_invertida[diretorios_ordenados][valores_ordenados].append(index)
                        else:
                            self.lista_invertida[diretorios_ordenados][valores_ordenados] = [index]

    @staticmethod
    def ordena_duas_listas_pelo_primeiro_item_da_lista(lista1, lista2):
        """
        Recebe duas listas e as ordena pelo primeiro item de cada uma.
        :param lista1: uma lista
        :param lista2: outra lista
        :return: as duas listas ordenadas pela primeira posição de cada uma
        """
        listas = [lista1, lista2]
        return sorted(listas, key=lambda x: x[0])

    def montar_dict_com_todos_os_valor_de_cada_diretorio(self):
        """
        Cria um dicionário com a lista de todos os valores de cada chave em 'diretorios'.
        :return: dicionário com a lista de todos os valores de cada chave em 'diretorios'
        """
        todos_os_valor_de_cada_diretorio = {diretorio: [] for diretorio in self.diretorios}
        # Percorre cada linha em 'data' e adiciona o valor de cada chave em 'todos_os_valor_de_cada_diretorio'
        for linha in self.data:
            for chave, valor in linha.items():
                todos_os_valor_de_cada_diretorio[chave].append(valor)
        return todos_os_valor_de_cada_diretorio

    def insersao_com_perguntas(self):
        """
        Solicita ao usuário o valor de cada chave em 'diretorios' e adiciona o dicionário com os valores a 'data'.
        Depois, chama o método 'monta_lista_invertida' para atualizar o dicionário 'lista_invertida'.
        """
        dict_a_ser_adicionado = {}
        # Solicita o valor de cada chave em 'diretorios' ao usuário e armazena os valores em 'dict_a_ser_adicionado'
        for diretorio in self.diretorios:
            valor = input(f'digite o(a) {diretorio}: ')
            dict_a_ser_adicionado[diretorio] = valor
        # Adiciona o dicionário 'dict_a_ser_adicionado' na lista 'data' e chama o método 'monta_lista_invertida'
        self.insersao(dict_a_ser_adicionado)

    @staticmethod
    def escolha_inexistente():
        """
        Exibe a mensagem 'opção inexistente' e chama o método 'menu'.
        """
        print('Essa escolha não existe')

    def carga_de_dados(self):
        self.insersao({'nome': "Theo", "idade": "21", "time": "Figueirense"})
        self.insersao({'nome': "Loren", "idade": "20", "time": "Figueirense"})
        self.insersao({'nome': "Loren", "idade": "40", "time": "Figueirense"})
        self.insersao({'nome': "Ninguem", "idade": "40", "time": "Avai"})
        self.insersao({'nome': "Pedro", "idade": "21", "time": "Figueirense"})

    def busca_simples(self):
        if len(self.data) < 1:
            print('Nenhum usuário na lista')
            print('Faça uma carga de dados ou adicione um elemento para realizar uma busca')
        else:
            print('Colunas:')
            for diretorio in self.diretorios:
                print(diretorio)
            print('\n')
            diretorio_desejado = input('Fazer a busca em qual coluna? ')
            valor_desejado = input('Qual valor será buscado? ')
            try:
                retorno_busca = self.lista_invertida[diretorio_desejado].get(valor_desejado)
                n_objeto = 0
                for linha in retorno_busca:
                    n_objeto += 1
                    print('\n')
                    print(f'Pessoa {n_objeto}')
                    for key in self.data[linha].keys():
                        print(f'{key}: {self.data[linha][key]}')
            except KeyError:
                print('\n')
                print('Não existe nenhuma ocorrencia desse valor')
                print('Confira se escreveu a coluna e o nome da pessoa corretamente')

    def busca_complexa(self):
        if len(self.data) < 1:
            print('Nenhum usuário na lista')
            print('Faça uma carga de dados ou adicione um elemento para realizar uma busca')
        else:
            print('Colunas:')
            print('\n')
            for diretorio in self.diretorios:
                print(diretorio)
            print('\n')
            diretorio_desejado1 = input('Qual será a coluna 1 da busca? ')
            valor_desejado1 = input('Qual o valor do item 1? ')
            diretorio_desejado2 = input('Qual será a coluna 2 da busca? ')
            valor_desejado2 = input('Qual o valor do item 2? ')
            try:
                lista_de_diretorios_e_seus_valores_ordenada = \
                    self.ordena_duas_listas_pelo_primeiro_item_da_lista(
                        [diretorio_desejado1, valor_desejado1], [diretorio_desejado2, valor_desejado2]
                    )
                diretorios_ordenados = \
                    lista_de_diretorios_e_seus_valores_ordenada[0][0] + "_" + lista_de_diretorios_e_seus_valores_ordenada[1][0]
                valores_ordenados = \
                    lista_de_diretorios_e_seus_valores_ordenada[0][1] + "_" + lista_de_diretorios_e_seus_valores_ordenada[1][1]
                retorno_busca = self.lista_invertida[diretorios_ordenados].get(valores_ordenados)
                n_objeto = 0
                for linha in retorno_busca:
                    n_objeto += 1
                    print('\n')
                    print(f'Pessoa {n_objeto}')
                    for key in self.data[linha].keys():
                        print(f'{key}: {self.data[linha][key]}')
            except KeyError:
                print('\n')
                print('Não existe nenhuma ocorrencia desse valor')
                print('Confira se escreveu as coluna e os nomes das pessoas corretamente')

    def mostrar_todos_elementos(self):
        n_objeto = 0
        for d in self.data:
            n_objeto += 1
            print('\n')
            print(f'Pessoa {n_objeto}')
            for key in d:
                print(f'{key}: {d[key]}')
        if len(self.data) < 1:
            print('Nenhum usuário na lista')
            print('Faça uma carga de dados ou adicione um elemento')

    def remover_elemento_por_index(self):
        try:
            index = int(input('Index da Pessoa que deseja excluir: '))
            pessoa = self.data[index]
            nome_pessoa = pessoa.get('nome')
            self.data.pop(index)
            print(f'Você excluiu o/a {nome_pessoa}')
            return self.monta_lista_invertida()
        except IndexError:
            print('Nenhuma pessoa está registrada com esse index')

    def menu(self):
        opcoes = {
            "1": self.insersao_com_perguntas,
            "2": self.carga_de_dados,
            "3": self.busca_simples,
            "4": self.busca_complexa,
            "5": self.mostrar_todos_elementos,
            "6": self.remover_elemento_por_index,

        }
        escolha = input(
            "\n1 - adicionar um elemento\n"
            "2 - carga de dados\n"
            "3 - busca simples\n"
            "4 - busca complexa\n"
            "5 - mostrar todos os elementos\n"
            "6 - excluir pessoa pelo index\n"
            "escolha:"
        )
        metodo_escolhido = opcoes.get(escolha, self.escolha_inexistente)
        print('\n')
        metodo_escolhido()
