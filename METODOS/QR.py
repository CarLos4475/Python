import numpy as np

def algoritmo_qr():
    n = int(input("Dimensión de la matriz: "))
    print(f"Ingrese los elementos de la matriz A ({n}x{n}):")
    A = np.zeros((n,n))
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
    
    # Preguntar por transformación Householder
    opcion = input("\n¿Desea usar la transformación de Householder? (s/n): ").lower()
    if opcion == 's':
        A = TransformacionHouseholder(A)
        print("\nMatriz después de la transformación de Householder:")
        print(A)
    
    iteraciones = int(input("\nNúmero de iteraciones: "))
    
    for k in range(iteraciones):
        Q = np.eye(n)
        R = A.copy()
        
        max_val = 0
        max_i = max_j = 0
        for i in range(1, n):            
            for j in range(i):           
                if abs(R[i,j]) > abs(max_val):
                    max_val = R[i,j]
                    max_i = i
                    max_j = j
        
        if abs(max_val) > 1e-10:
            i, j = max_i, max_j          
            r = np.sqrt(R[j,j]**2 + R[i,j]**2)
            cos_theta = R[j,j]/r
            sin_theta = R[i,j]/r
            
            Q = np.eye(n)
            Q[i,i] = cos_theta
            Q[j,j] = cos_theta
            Q[i,j] = sin_theta  
            Q[j,i] = -sin_theta
            
            R = np.dot(np.dot(Q.T, R), Q)
        
        A = R.copy()
    
    print("\nMatriz R final:")
    np.set_printoptions(precision=5, suppress=True, floatmode='fixed')
    print(R)
    print("\nValores propios (elementos de la diagonal):")
    for i in range(n-1, -1, -1):
        print(f"λ{n-i} = {A[i,i]:.4f}")

def TransformacionHouseholder(A):
    n = len(A)
    A = np.array(A, dtype=float)
    
    traza_inicial = np.trace(A)
    print(f"Traza inicial: {traza_inicial:.4f}")
    
    H = A.copy()
    max_iter = 100
    tol = 1e-10
    
    for iter in range(max_iter):
        for k in range(n-2):
            suma = 0
            for j in range(k+1, n):
                suma += H[j,k]**2
            G = np.sign(H[k+1,k]) * np.sqrt(suma)
            
            r = np.sqrt(0.5*G**2 + 0.5*H[k+1,k]*G)
            
            if r != 0:
                w = np.zeros(n)
                w[k] = 0
                w[k+1] = (H[k+1,k] + G)/(2*r)
                for i in range(k+2, n):
                    w[i] = H[i,k]/(2*r)
                
                P = np.eye(n) - 2*np.outer(w, w)
                H = np.dot(np.dot(P, H), P)
        
        es_tridiagonal = True
        for i in range(n):
            for j in range(n):
                if abs(i-j) > 1 and abs(H[i,j]) > tol:
                    es_tridiagonal = False
                    break
        
        if es_tridiagonal:
            break
    
    H[abs(H) < tol] = 0
    
    traza_final = np.trace(H)
    print(f"Traza final: {traza_final:.4f}")
    
    np.set_printoptions(precision=5, suppress=True, floatmode='fixed')
    return H

if __name__ == "__main__":

    algoritmo_qr()
