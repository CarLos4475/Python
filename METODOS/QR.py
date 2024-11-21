
import numpy as np

def qr_algorithm():
    n = int(input("Dimensión de la matriz: "))
    print(f"Ingrese los elementos de la matriz A ({n}x{n}):")
    A = np.zeros((n,n))
    for i in range(n):
        while True:
            try:
                row = input().split()
                if len(row) != n:
                    print(f"Error: Debe ingresar {n} números para la fila {i+1}.")
                    continue
                for j in range(n):
                    A[i][j] = float(row[j])
                break
            except ValueError:
                print("Error: Ingrese solo números.")
    
    iterations = int(input("Número de iteraciones: "))
    
    for k in range(iterations):
        Q = np.eye(n)
        R = A.copy()
        
        # Find maximum element BELOW diagonal
        max_val = 0
        max_i = max_j = 0
        for i in range(1, n):            
            for j in range(i):           
                if abs(R[i,j]) > abs(max_val):
                    max_val = R[i,j]
                    max_i = i
                    max_j = j
        
        # Calculate rotation parameters
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
        
        A = R.copy()  # Update A for next iteration
    
    print("\nMatriz R final:")
    np.set_printoptions(precision=4, suppress=True)
    print(R)
    print("\nValores propios (elementos de la diagonal):")
    for i in range(n-1, -1, -1):
        print(f"λ{n-i} = {A[i,i]:.4f}")

if __name__ == "__main__":
    qr_algorithm()