# Gerador de Sequência Fibonacci:
# Crie um programa que gere os primeiros N números da sequência Fibonacci, onde cada número é a soma dos dois anteriores. Utilize um laço de repetição for para gerar os números.

# Função para gerar os primeiros N números da sequência Fibonacci
def fibonacci(n):
    # Inicializa a sequência Fibonacci com os dois primeiros números (0 e 1)
    fibonacci_seq = [0, 1]
    
    # Utiliza um laço de repetição for para gerar os próximos números da sequência
    for i in range(2, n):
        # Calcula o próximo número da sequência como a soma dos dois números anteriores
        proximo_numero = fibonacci_seq[i - 1] + fibonacci_seq[i - 2]
        fibonacci_seq.append(proximo_numero)
    
    return fibonacci_seq

# Solicita ao usuário o número de termos da sequência Fibonacci desejados
N = int(input("Digite o número de termos da sequência Fibonacci desejados: "))

# Chama a função fibonacci para gerar os primeiros N números da sequência
sequencia_fibonacci = fibonacci(N)

# Imprime os N números da sequência Fibonacci
print(f"Os primeiros {N} números da sequência Fibonacci são:")
for numero in sequencia_fibonacci:
    print(numero, end=" ")

#Neste código, a função fibonacci(n) gera os primeiros N números da sequência Fibonacci utilizando um laço de repetição for para calcular cada número como a soma dos dois números anteriores. Em seguida, é solicitado ao usuário o número de termos desejados e a função é chamada para gerar a sequência. Os números são então impressos na saída padrão.
