class ListaInvertida:
    def __init__(self):
        self.data = []
        self.lista_invertida = {}
        self.diretorios = ['nome', 'idade', 'time']

    def insersao(self, valores):
        self.data.append(valores)
        self.monta_lista_invertida()

    def monta_lista_invertida(self):
        for diretorio in self.diretorios:
            self.lista_invertida[diretorio] = {}
            for diretorio2 in self.diretorios:
                if diretorio != diretorio2:
                    lista_de_diretorios = [diretorio, diretorio2]
                    lista_de_diretorios.sort()
                    self.lista_invertida["_".join(lista_de_diretorios)] = {}
        for index, linha in enumerate(self.data):
            for diretorio, valor in linha.items():
                if valor in self.lista_invertida[diretorio]:
                    self.lista_invertida[diretorio][valor].append(index)
                else:
                    self.lista_invertida[diretorio][valor] = [index]
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
        listas = [lista1, lista2]
        return sorted(listas, key=lambda x: x[0])

    def montar_dict_com_todos_os_valor_de_cada_diretorio(self):
        todos_os_valor_de_cada_diretorio = {diretorio: [] for diretorio in self.diretorios}
        for linha in self.data:
            for chave, valor in linha.items():
                todos_os_valor_de_cada_diretorio[chave].append(valor)
        return todos_os_valor_de_cada_diretorio

    def insersao_com_perguntas(self):
        dict_a_ser_adicionado = {}
        for diretorio in self.diretorios:
            valor = input(f'digite o(a) {diretorio}: ')
            dict_a_ser_adicionado[diretorio] = valor
        self.insersao(dict_a_ser_adicionado)

    @staticmethod
    def escolha_inexistente():
        print('Essa escolha não existe')

    def carga_de_dados(self):
        self.insersao({'nome': "Theo", "idade": "21", "time": "Figueirense"})
        self.insersao({'nome': "Loren", "idade": "20", "time": "Figueirense"})
        self.insersao({'nome': "Loren", "idade": "40", "time": "Figueirense"})
        self.insersao({'nome': "Ninguem", "idade": "40", "time": "Avai"})
        self.insersao({'nome': "Pedro", "idade": "21", "time": "Figueirense"})

    def busca_simples(self):
        print('Colunas:')
        for diretorio in self.diretorios:
            print(diretorio)
        diretorio_desejado = input('Fazer a busca em qual coluna?')
        valor_desejado = input('Qual valor será buscado?')
        retorno_busca = self.lista_invertida[diretorio_desejado].get(valor_desejado)
        if not retorno_busca:
            print('Não existe nenhuma ocorrencia desse valor')
        else:
            for linha in retorno_busca:
                # TODO: deixar print bonito
                print(self.data[linha])

    def busca_complexa(self):
        print('Colunas:')
        for diretorio in self.diretorios:
            print(diretorio)
        diretorio_desejado1 = input('Qual será a coluna 1 da busca?')
        valor_desejado1 = input('Qual o valor do item 1?')
        diretorio_desejado2 = input('Qual será a coluna 2 da busca?')
        valor_desejado2 = input('Qual o valor do item 2?')
        lista_de_diretorios_e_seus_valores_ordenada = \
            self.ordena_duas_listas_pelo_primeiro_item_da_lista(
                [diretorio_desejado1, valor_desejado1], [diretorio_desejado2, valor_desejado2]
            )
        diretorios_ordenados = \
            lista_de_diretorios_e_seus_valores_ordenada[0][0] + "_" + lista_de_diretorios_e_seus_valores_ordenada[1][0]
        valores_ordenados = \
            lista_de_diretorios_e_seus_valores_ordenada[0][1] + "_" + lista_de_diretorios_e_seus_valores_ordenada[1][1]
        retorno_busca = self.lista_invertida[diretorios_ordenados].get(valores_ordenados)
        if not retorno_busca:
            print('Não existe nenhuma ocorrencia desse valor')
        else:
            for linha in retorno_busca:
                # TODO: deixar print bonito
                print(self.data[linha])

    def mostrar_todos_elementos(self):
        # TODO: implementar um mostrar tudo bonito
        return self.data

    def remover_elemento_por_index(self):
        # TODO: implementar método q remove um elemento da lista pelo index, lembrar q
        #  tem q rodar o self.monta_lista_invertida() depois da remoção
        return True

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
            "6 - mostrar todos os elementos\n"
            "escolha:"
        )
        metodo_escolhido = opcoes.get(escolha, self.escolha_inexistente)
        print('\n')
        metodo_escolhido()
