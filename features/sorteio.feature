#language: pt

  Funcionalidade: Sorteio

    @sorteio
    Cenario: Sortear número e verificar se acertou
      Dado que acesso o programa
      Quando sorteio um número 3 à 5
      Então verifico se o resultado é igual 5

    @sorteio2
    Cenario: Sortear dois números e verificar se acertou
      Dado  que acesso o programa
      Quando sorteio o primeiro número de 1 a 3
      E outro número de 4 a 6
      Então verifico se o primeiro resultado é igual a 3
      E o segundo é igual 5