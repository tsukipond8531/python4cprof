---
title: Visão geral do Python para professores que usam C
colorlinks: true
geometry:
- margin=2cm
- nohead
papersize: a4
fontsize: 12
lang: pt-BR
numbersections: true
---

# Introdução

Neste texto apresentamos uma visão geral da linguagem Python para professores que vão ministrar algoritmos e estrutura de dados em Python e que têm experiência com o ensino usando C. O objetivo é esclarecer alguns pontos e mostrar como as construções algorítmicas de C podem ser expressas em Python. Note que o objetivo não é apresentar Python de forma profunda e nem descrever uma metodologia de ensino de algoritmos e estruturas de dados.

Começamos com algumas diferenças entre as duas linguagens, depois discutimos as principais construções do Python, em seguida mostramos a implementação de alguns algoritmos e estruturas de dados e por fim apresentamos algumas convenções de código para Python e indicamos referências.


# Diferenças entre Python e C

As linguagens Python e C têm muitos aspectos distintos (pois são comumente usadas em situações diferentes). Entre algumas diferenças destacamos

- Forma geral da sintaxe
- Forma de execução
- Sistema de tipos
- Passagem de parâmeros
- Gerência de memória
- Biblioteca padrão

Para exemplificar algumas dessas diferenças vamos utilizar os seguintes exemplos.

Código em C

```c
#include <stdio.h>

/*
 * Devolve a quantidade de items em valores que estão no intervalo [min, max].
 *
 * n é quantidade de items em valores que é analisada.
 */
int conta_no_intervalo(int* valores, int n, int min, int max)
{
    // O correto seria declarar n, i, quant e o retorno da função como size_t.
    // Veja https://stackoverflow.com/q/66527638/5189607
    int quant = 0;
    for (int i = 0; i < n; i++) {
        if (min <= valores[i] && valores[i] <= max)
            quant++;
    }
    return quant;
}

int main(int argc, char* argv[])
{
    printf("Este programa conta a quantidade de valores em um determinado intervalo.\n");

    int n;
    printf("Digite a quantidade de valores: ");
    if (scanf("%d", &n) != 1 || n <= 0) {
        printf("Valor inválido.\n");
        return 1;
    }

    // Alocação explícita no heap
    // int* valores = (int *) malloc(n * sizeof(int));
    // Alocação dinâmica implícita na pilha
    int valores[n];
    // O retorno de scanf não é verificado nas
    // próximas chamadas para simplificar o código.
    printf("Digite %d separados por espaço.\n", n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &valores[i]);
    }

    int min;
    printf("Digite o limite inferior do intervalo: ");
    scanf("%d", &min);

    int max;
    printf("Digite o limite superior do intervalo: ");
    scanf("%d", &max);

    printf("Existe(m) %d valor(es) no intervalo.\n", conta_no_intervalo(valores, n, min, max));

    // Desalocação explícita no caso de alocação no heap
    // free(valores);
}
```

Código em Python

```python
def conta_no_intervalo(valores: list[int], min: int, max: int) -> int:
    '''Devolve a quantidade de items em valores que estão no intervalo [min, max].
    Exemplo
    >>> conta_no_intervalo([2, 5, 1, 4, 6, 8], 2, 6)
    4
    '''
    # poderia ser
    # quant: int = 0
    quant = 0
    for valor in valores:
        # poderia ser
        # min <= valor <= max
        if min <= valor and valor <= max:
            quant += 1
    return quant


def main():
    print('Este programa conta a quantidade de valores em um determinado intervalo.')
    s = input('Digite os valores separados por espaço: ')
    valores = []
    for valor in s.split():
        valores.append(int(valor))
    min = int(input('Digite o limite inferior do intervalo: '))
    max = int(input('Digite o limite superior do intervalo: '))

    print('Existe(m)', conta_no_intervalo(valores, min, max), 'valor(es) no intervalo.')


if __name__ == "__main__":
    main()
```


## Formal geral da sintaxe

A sintaxe do C é baseada em blocos delimitados por chaves (`{}`{.c}), a indentação do código não influencia a semântica. As chaves são opcionais nas instruções de controle quando apenas uma sentença é especificada. Na definição de estruturas e funções as chaves são sempre necessárias. As expressões/sentenças das instruções de controle devem ser especificadas entre parênteses. Os operadores lógicos são especificados com símbolos (`!`{.c}, `||`{.c}, `&&`{.c}).

Os blocos em Python inciam com ":" e são delimitados pela indentação. As expressões/sentenças das instruções de controle não precisam ser especificadas entre parênteses. Os operados lógicos são especificados com as palavras chaves `not`{.python}, `or`{.python} e `and`{.python}.

Em Python os operadores relacionais pode ser encadeados, dessa forma é possível escrever `a < b < c`{.python} ao invés de `a < b and b < c`{.python}.

Em C os tipos das variáveis são especificadas antes do nome da variável. Já em Python, os tipos são especificados após o nome da variável, pela sintaxe `: tipo`{.python}. As especificação do tipo em C é obrigatória, em Python é opcional. Aspectos da semântica de tipos são discutidas em outra seção.

Python utiliza a palavra chave `def`{.python} pra definições de funções e o tipo de retorna da função é especificado com `-> tipo`{.python}

Em Python não existe operadores de pós e pré incremento/decremento, mas existem os operadores de atribuição com incremento/decremento (entre outros).

Strings em Python podem ser especificadas com aspas (`"`{.python}) ou apóstrofo (`'`{.python}).

Em C existem dois tipos de comentário, o de linha (`//`{.c}) e o de bloco (`/* */`{.c}). Python também tem dois tipos de comentário, o de linha (`#`{.python}) e o de documentação (`''' '''`{.python}), que deve aparecer apenas como primeiro item de uma definição.


## Forma de execução

C é usado comumente como um linguagem compilada. Isso implica que para testar qualquer trecho de código em C é necessário escrever um programa completo (com função `main`), compilar e depois executar o programa. Além disso, para exibir o valor de uma variável é necessário chamar uma função como `print` explicitamente (também é possível consultar os valores das variáveis usando um depurador).

Já o Python é usado comumente como uma linguagem interpretada de duas maneira, a primeira é especificando o nome de um arquivo `.py`, nesse caso o código do arquivo é executado diretamente (compilado para código de uma máquina virtual e depois executado).

A segunda maneira é sem especificar um arquivo, nesse caso é iniciado um modo interativo para avaliação de trechos de código (REPL - _Read, Eval, Print and Loop_). O _prompt_ padrão é identificado com `>>>`. O usuário digita um trecho de código, que é executado e o resultado é exibido em seguida. Por exemplo

```python
>>> 'Resposta ' + str(2 + 10 * 4)
'Resposta 42'
```

O modo interativo é uma ferramente muito valioso, pois permite a rápida exploração do funcionamento de trechos de código, mas é importante instruir o aluno a usar esse modo apenas para exploração e não desenvolvimento do código final (a escrita do programa deve ser feita seguindo o processo de projeto de programas).

Não é necessário uma função `main` em Python, mas é uma boa prática criar uma e chamá-la explicitamente (como no exemplo).

O Python tem alguns mecanismos para escrita e execução de testes, o mais simples é o `doctest`. Os exemplos escritos na documentação podem ser executados e verificados de forma automática. Por exemplo, se a função `conta_no_intervalo` está em um arquivo chamado `x.py`, os exemplos podem ser verificados com o comando `python -m doctest -v x.py`.


## Sistema de tipos

C é comumente classificada como estaticamente tipada, isto é, os tipos são vinculados as variáveis em tempo de compilação (note que `void*`{.c} é um escape para essa regra que é amplamente utilizado pelas funções da biblioteca padrão, entre elas `malloc/free`{.c}). Os compiladores de C detectam muitos erros de tipo durante a compilação, no entanto, C permite a conversão implícita entre muitos tipos de dados, o que pode ser confuso para o aluno iniciante (por exemplo, `double`{.c} e `float`{.c} para `int`{.c}, arranjos para ponteiros, etc).

Historicamente Python tem sido classificada como dinamicamente tipada, isto é, os tipos são vinculados em tempo de execução aos valores e não as variáveis. Isso implica, por exemplo, que uma mesma variável pode em momentos distintos armazenar valores de tipos distintos. Python tem algumas conversões implícitas de valores (como `int`{.python} para `float`{.python}).

O Python 2 não suporta especificação dos tipos para variáveis e funções. A partir do Python 3.0, o suporte para especificação de tipos foi adiciona e a partir da versão 3.5 (lançada em 2015), esse suporte foi aprimorado (e continua sendo).

O interpretador padrão do Python (o que é baixado de <https://python.org>), ignora todas as anotações de tipos, mas existem ferramentes que podem utilizar essas anotações para fazer verificações estáticas no código. Uma dessas ferramentes é o [mypy](https://mypy-lang.org/). O `mypy` faz uma verificação estática dos tipos e indica os erros se forem encontrados. Por exemplo, no código a seguir, declaramos `n` como inteiro mas estamos atribuindo um ponto flutuante, o que o `mypy` identifica como erro.

```python
n: int = 10.2
```

Dessa forma, usando o `mypy`, podemos desenvolver os programas em Python como se eles fossem estaticamente tipados, mesmo que de fato as anotações de tipo não alterem a forma como o programa é executado. O sistema de tipos do `mypy` é muito poderoso e permite expressar muitas restrições estaticamente. Vamos discutir mais sobre esse aspecto na seção de Exemplos.

Outro aspecto diferente entre as duas linguagem é que em C todos os tipos são "tipos valores" enquanto que em Python os tipos são "tipos referências" (<https://en.wikipedia.org/wiki/Value_type_and_reference_type>).

O principal efeito dessa diferença é visto na atribuição e na passagem de parâmetros. Discutimos essa questão na próxima seção.


## Passagem de parâmetros

Como em C "tudo é um valor", todas as atribuições e passagem de parâmetros são feitas por cópia (não tem referência!). No entanto, o uso de ponteiros permite contornar essa limitação, pois a cópia de um ponteiro em uma atribuição ou passagem de parâmetro acaba tendo o mesmo efeito de referências múltiplas para o mesmo valor.

Já em Python como "tudo é uma referência", todas as atribuições e passagem de parâmetros são feitas por referência. No exemplo a seguir, quanto `x` é atribuído para `y`, `y` passa a referenciar o mesmo valor referenciado por `x`. Em seguida, quando um novo valor é atribuído para `x`, `x` passa a referenciar esse novo valor e `y` não é alterado.

```python
x = 10
y = x
x = 2
```

Considere agora o seguinte exemplo

```python
x = [1, 4]
y = x
x.append(6)
```

Após a atribuição `y = x`{.python}, `x`{.python} e `y`{.python} referenciam a mesma lista, dessa forma, a alteração da lista por `x.append(6)`{.python} é refletida em `y` pois `x` e `y` referenciam a mesma lista.

Os tipos em Python podem ser mutáveis ou imutáveis. Os tipos numéricos, strings, entre outros, são imutáveis, ou seja, dado uma referência para um número, não é possível alterar esse número. Já as listas e outros tipos são mutáveis (é possível alterar a lista). Uma consequência disso é que se um valor de tipo imutável é passado como parâmetro, não é possível devolver um resultado alterando esse valor (pois o tipo é imutável). Outra consequência é que para passar parâmetros de tipos mutáveis por cópia, é preciso fazer a cópia explicitamente.

Suponha que tivéssemos que implementar um TAD de dicionário (arranjo associativo de string para inteiro) e estivéssemos implementando a função de busca pela chave. Os argumentos de entrada seriam o dicionário e a chave e a saída uma indicação se o elemento com a chave foi encontrada e o próprio elemento encontrado. Em C, se a função retornasse um `bool`{.c} indicando o resultado da busca, poderíamos utilizar um argumento do tipo ponteiro para inteiro para indicar o elemento encontrado. A assinatura da função seria algo como

```c
/* Devolve true se chave está presente em dic, false caso contrário.
 * Se a chave estiver presente, o valor associado com a chave é
 * armazenado em valor.
 */
bool busca_chave(Dicionario *dic, char* chave, int* valor);
```

Em Python não é possível fazer desse jeito. Considere uma função com a assinatura

```python
def busca_chave(dic: Dicionario, chave: str, valor: int) -> bool
```

Se um inteiro é atribuído para `valor` no corpo de `busca_chave`, `valor` passa a referenciar um novo valor, o valor referenciado anteriormente permanece inalterado (números são imutáveis). Discutimos uma forma de resolver essa situação na seção Exemplos.


## Gerência de memória

Os objetos em C podem ser alocados na pilha ou no heap. A alocação/desalocação dos objetos na pilha é feita automaticamente pelo ambiente de execução. Já a alocação/desalocação de objetos do heap deve ser feita de forma explícita pelo programador.

Em Python todos os objetos são alocados implicitamente do heap. A desalocação é feita de forma automática usando uma combinação de contagem de referências e coleta de lixo. Dessa forma, dois erros bastante comuns em C, a tentativa de desalocação de memória já desalocada e a tentativa de uso de memória já desalocada, não podem acontecer em Python.


## Biblioteca padrão

A biblioteca padrão de C é pequena quando comparada com outras linguagens. Ela inclui diversas funções para comunicação com o sistema operacional, alguns funções para strings e números e poucas funções algorítmicas e de estruturas de dados.

Por outro lado, o Python tem uma biblioteca padrão bastante extensa, que é um dos motivos pelos quais o Python é bastante utilizado. No entanto, também pode ser motivo de preocupação para alguns professores, pois existe a possibilidade dos alunos usar as funcionalidade prontas e deixar de implementar funcionalidades que são importante para o aprendizado. Mas isso não precisa ser dessa forma, o professor pode deixar claro o que pode ou não ser usado e o que é importante implementar.

Nas próximas duas seção mostramos um subconjunto do Python e como esse subconjunto pode ser usado na implementação de alguns algoritmos e estruturas de dados.


# O básico de Python

O Python é uma linguagem extensa e tem uma biblioteca padrão extensa. O sistema de tipos do `mypy` e bastante poderoso e também extenso. Dessa forma, para evitar que os alunos se percam na linguagem e deixem de focar nos fundamentos, é importante delimitar um subconjunto das construções da linguagem para ser utilizado pelos alunos.

Apresentamos a seguir um subconjunto suficiente para escrever qualquer algoritmo e estruturas de dados. Note que o código escrito nesse subconjunto pode ficar um pouco mais extenso e não ser considerado pythônico (código idiomático em Python).


## Estruturas de controle

As principais estruturas de controle do Python são `if`{.python}, `for`{.python}, `while`{.python} e o `assert`{.python} (o Python 3.10 introduziu a construção `match/case`{.python}, que é de certa forma um `switch/case`{.c} similar ao do C, mas mais geral).

Assim como no `if`{.c} do C, a cláusula `else`{.python} do `if`{.python} do Python é opcional. Para evitar o aumento de níveis na indentação de `if`{.python}s aninhamos, o Python permite a união de um `else`{.python} seguido de `if`{.python} com a palavra chave `elif`{.python}. O exemplo a seguir mostra o uso do `if`{.python}.

```python
def sinal(n: int) -> str:
    '''Devolve o sinal de n.

    Exemplos
    >>> sinal(3)
    'positivo'
    >>> sinal(0)
    'neutro'
    >>> sinal(-1)
    'negativo'
    '''
    if n > 0:
        return 'positivo'
    else:
        if n < 0:
            return 'negativo'
        else:
            return 'neutro'
    # ou usando o elif
    # if n > 0:
    #    return 'positivo'
    # elif n < 0:
    #     return 'negativo'
    # else:
    #     return 'neutro'
```

O `for`{.c} clássico do C não existe em Python. Em Python o `for`{.python} é usado para fazer iteração pelos elementos de uma estrutura de dados. A outra forma de iteração do Python é o `while`{.python}. O exemplo a seguir mostra o uso do `for`{.python} e do `while`{.python}.

```python
def ordena(nomes: list[str]) -> list[str]:
    '''
    Cria uma nova lista com os mesmos elementos de nomes mas de forma ordenada.

    Exemplo
    >>> ordena(['Paulo', 'Ana', 'Maria', 'João'])
    ['Ana', 'João', 'Maria', 'Paulo']
    '''
    r = []
    for nome in nomes:
        r.append(nome)
        i = len(r) - 1
        # r[i] é o nome que foi inserido
        # troca r[i] com r[i - 1] até que ele fique na posição adequada
        while i > 0 and r[i - 1] > r[i]:
            tmp = r[i - 1]
            r[i - 1] = r[i]
            r[i] = tmp
            # ou usando atribuição múltipla
            # r[i - 1], r[i] = r[i], r[i - 1]
            i -= 1
    return r
```

Quando for necessário o índice dos elementos em uma iteração, podemos usar o `while`{.python} ou o `for`{.python} combinado com a função [`range`](https://docs.python.org/3/library/stdtypes.html#typesseq-range).

```python
def indice_maximo(valores: list[float]) -> int:
    '''Encontra o índice do valor máximo em valores.

    Requer que valores não seja vazio.

    Exemplos
    >>> indice_maximo([2, 1, 4, -2])
    2
    >>> indice_maximo([-1, -4, -1])
    0
    '''
    assert len(valores) != 0, "valores não pode ser vazio"
    imax = 0
    for i in range(1, len(valores)):
        if valores[imax] < valores[i]:
            imax = i
    return imax
```


No exemplo anterior usamos uma outra estrutura de controle, o `assert`{.python}. O `assert`{.python} pode ser usado com uma ou duas expressões. O Python avalia a primeira expressão, se o resultador for `True`{.python}, a execução continua para a próxima linha, caso contrário, uma exceção é gerada com uma mensagem padrão ou com o resultado da segunda expressão do `assert`{.python} (se existir).


## Tipos de dados

Em C existem diversos tipos numéricos, em Python são apenas dois: `int`{.python} e `float`{.python}. O tipo `int`{.python} representa inteiros de tamanho arbitrário enquanto `float`{.python} números de pontos flutuantes no padrão IEEE 754 binary64 (mesmo que o `double`{.c} em C).


## Entrada e saída

Python não tem funções para fazer entrada de dados formatada. A principal função de entrada em Python é `input` que recebe um argumento (mensagem a ser exibida) e retorna uma linha lida (string) da entrada padrão. A string lida pode ser convertida para outro tipo posteriormente, no exemplo, a função `int` converte a string para um inteiro (uma exceção é gerada se a conversão não puder ser feita).

Python tem diversas funções de saída (incluindo saída formatada), a mais comum é o `print`. A função `print` recebe um número variado de argumentos (de qualquer tipo), converte cada argumento para uma string com a função `str` e exibe os valores separando-os por espaço e adicionando um final de linha (esse comportamento pode ser alterado).



## Tipos abstratos de dados



# Exemplos


# Convenções de código

Essas são algumas convenções para escrita de código em Python (de acordo com <https://peps.python.org/pep-0008/>):

- Indentação usando 4 espaços;

- Não utilizar tabulações;

- Nomes de tipos da forma `CapitalizedWords`;

- Nomes de funções e variáveis da forma `lower_case_with_underscores`;

- Constantes da forma `UPPER_CASE_WITH_UNDERSCORES`;

- Um `import`{.python} por linha;

- Evite espaçamentos extras (`spam(ham[1], {eggs: 2})`{.python} ao invés de `spam( ham[ 1 ], { eggs: 2 } )`{.python});

- Sempre use espaços entre operadores (`c += (a + b) * (a - b)`{.python} ao invés de `c+=(a+b)*(a-b)`{.python})


# Referências

Ensino de programação

- [A Data-Centric Introduction to Computing](https://dcic-world.org/)

- [How to Design Programs](https://htdp.org/) ([vídeos](https://www.youtube.com/@systematicprogramdesign7962/playlists))

- [SICP in Python](https://wizardforcel.gitbooks.io/sicp-in-python/content/) ([vídeos](https://inst.eecs.berkeley.edu/~cs61a/fa22/))

- [Think Python 2e](https://greenteapress.com/wp/think-python-2e/)

Estrutura de dados

- [Open data structures](https://opendatastructures.org/ods-python.pdf) (em pseudo código que foi gerado automaticamente a partir do código Python)

Linguagem Python

- [Dive into Python 3](https://diveintopython3.net/)

