def contar_divisores_multiplo_3(n):
    contador = 0
    
    for i in range(1, n + 1):
        if n % i == 0 and i % 3 == 0:  
            contador += 1
    
    
    if contador > 0:
        print(f"Quantidade de divisores divisivos por 3: {contador}")
    else:
        print("O número não possui divisores múltiplos de 3")


n = int(input())


contar_divisores_multiplo_3(n)



2




def soma_positivos_no_intervalo(a, b):
    
    inicio = min(a, b)
    fim = max(a, b)
    
    soma = 0
    
   
    for i in range(inicio, fim + 1):
        if i > 0:
            soma += i
    
    return soma


a, b = map(int, input().split())


print(soma_positivos_no_intervalo(a, b))