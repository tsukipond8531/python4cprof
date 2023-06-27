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
    for (int i = 0; i < n; i++) { // as chaves poderiam ser omitidas nesse caso
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

    // Alocação dinâmica implícita na pilha
    int valores[n];
    // Ou alocação explícita no heap
    // int* valores = (int *) malloc(n * sizeof(int));

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
