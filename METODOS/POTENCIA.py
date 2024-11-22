import numpy as np

def metodo_potencia(A):
    n = len(A)
    x = np.zeros(n, dtype=np.float64)
    print("\nIngrese el vector inicial:")
    for i in range(n):
        while True:
            try:
                x[i] = float(input())
                break
            except ValueError:
                print("Error: Ingrese solo números.")
    
    x = x / np.linalg.norm(x)
    
    tolerancia = float(input("\nTolerancia: "))
    max_iter = 1000
    lambda_prev = 0
    
    np.set_printoptions(precision=6, suppress=True, floatmode='fixed')
    
    print("\nIteraciones:")
    for k in range(max_iter):
        y = np.dot(A, x)
        lambda_k = np.max(np.abs(y))
        x = y / lambda_k
        error = abs(lambda_k - lambda_prev)
        
        print(f"Iteración {k+1}:")
        print(f"λ = {lambda_k:.6f}")
        print("Vector propio:")
        print(x)
        print(f"Error = {error:.6f}")
        
        if error < tolerancia:
            break
            
        lambda_prev = lambda_k
    
    print("\n---------------------------------")
    print("\nResultados finales:")
    print("Vector propio:")
    print(x)
    print("\nValor propio:")
    print(f"{lambda_k:.15f}")

def metodo_potenciaInversa(A):
    n = len(A)
    x = np.zeros(n, dtype=np.float64)
    print("\nIngrese el vector inicial para potencia inversa:")
    for i in range(n):
        while True:
            try:
                x[i] = float(input())
                break
            except ValueError:
                print("Error: Ingrese solo números.")
    
    x = x / np.linalg.norm(x)
    tolerancia = float(input("\nTolerancia: "))
    max_iter = 1000
    lambda_prev = 0
    
    A_inv = np.linalg.inv(A)
    np.set_printoptions(precision=6, suppress=True, floatmode='fixed')
    
    print("\nIteraciones:")
    for k in range(max_iter):
        y = np.dot(A_inv, x)
        lambda_k = np.max(np.abs(y))
        x = y / lambda_k
        error = abs(lambda_k - lambda_prev)
        
        print(f"Iteración {k+1}:")
        print(f"λ = {1/lambda_k:.6f}")
        print("Vector propio:")
        print(x)
        print(f"Error = {error:.6f}")
        
        if error < tolerancia:
            break
            
        lambda_prev = lambda_k
    
    print("\n---------------------------------")
    print("\nResultados finales:")
    print("Vector propio:")
    print(x)
    print("\nValor propio:")
    print(f"{1/lambda_k:.15f}")

if __name__ == "__main__":
    # Leer matriz
    n = int(input("Dimensión de la matriz: "))
    print(f"Ingrese los elementos de la matriz A ({n}x{n}):")
    A = np.zeros((n,n), dtype=np.float64)
    for i in range(n):
        while True:
            try:
                fila = input().split()
                if len(fila) != n:
                    print(f"Error: Debe ingresar {n} números para la fila {i+1}.")
                    continue
                for j in range(n):
                    A[i][j] = float(fila[j])
                break
            except ValueError:
                print("Error: Ingrese solo números.")
    
    # Menú de selección
    print("\nSeleccione una opción:")
    print("1. Calcular valor propio de mayor magnitud")
    print("2. Calcular valor propio de menor magnitud")
    print("3. Calcular ambos valores propios")
    
    opcion = input("Opción: ")
    
    if opcion == "1":
        metodo_potencia(A)
    elif opcion == "2":
        metodo_potenciaInversa(A)
    elif opcion == "3":
        print("\nCalculando valor propio de mayor magnitud:")
        metodo_potencia(A)
        print("\nCalculando valor propio de menor magnitud:")
        metodo_potenciaInversa(A)
    else:
        print("Opción inválida")
