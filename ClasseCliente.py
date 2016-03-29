# -*- coding: utf-8 -*-
#import java.util.Enumeration;
#import java.util.Vector;
from Filme import Filme
from Alocacao import Alocacao
import itertools

CRIANCAS = 2
REGULAR = 0
NOVA_RELEASE = 1

class ClasseCliente():
    _nome = None
    _alocacoes = []

    def __init__(self, nome):
        self._nome = nome
        self._alocacoes = []

    def addicionarAlocacao(self, arg): # art de tipo alocacao
        self._alocacoes.append(arg)

    def getNome(self):
        return self._nome

    def contarPontos(self):
        alocacoes = iter(self._alocacoes)
        pontosFrequenciaAlocacao = 0
        resultado = ''

        for aloc in alocacoes:
            #adicionar pontos de locador frequente
            pontosFrequenciaAlocacao = pontosFrequenciaAlocacao + 1
            #adicionar bonus para uma locação de dois dias para lançamentos
            if aloc.getFilme().getPrecoCodigo() == Filme.NOVA_RELEASE and aloc.getDiasAlocados()>1:
                pontosFrequenciaAlocacao = pontosFrequenciaAlocacao +1
             #mostrar informacoes para esta locacao
        resultado = resultado + 'Voce ganhou '+ str(pontosFrequenciaAlocacao)+' pontos de locacao.'
        return resultado

    def expresao(self):
        totalQuantidade = 0.0
        alocacoes = iter(self._alocacoes)
        resultado = 'Registro de Locação para : '+ self.getNome()+'\n'

        #while(alocacoes):
        for cada in alocacoes:
            estaQuantidade = 0.0
            estaQuantidade = float(cada.quantidadePara())
            resultado = resultado + ' '+cada.getFilme().getTitulo()+' '+ str(estaQuantidade)+'\n'
            totalQuantidade = estaQuantidade + totalQuantidade
        #adicionar rodape do relatorio
        resultado = resultado + "Quantia devida é "+ str(totalQuantidade)
        return resultado

if __name__ == '__main__':
    meuCliente = ClasseCliente('Ruben')
    print meuCliente.getNome()
    fil01 = Filme('Titanic',2)
    alo01 = Alocacao(fil01,5) #filme, dias locados
    alo02 = Alocacao(fil01,2) #filme, dias locados
    alo03 = Alocacao(fil01,1) #filme, dias locados

    meuCliente.addicionarAlocacao(alo01)
    meuCliente.addicionarAlocacao(alo02)
    meuCliente.addicionarAlocacao(alo03)

    print meuCliente.expresao()
    print meuCliente.contarPontos()
