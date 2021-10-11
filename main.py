import math
import numpy as np

def cylinder_area(r:float,h:float):
    
    if ( r <= 0 or h <= 0 ):
        print("Invalid values") 
        return None
    else:
        return math.pi * r * r * h
    
    """Obliczenie pola powierzchni walca. 
    Szczegółowy opis w zadaniu 1.
    
    Parameters:
    r (float): promień podstawy walca 
    h (float): wysokosć walca
    
    Returns:
    float: pole powierzchni walca 
    """

def fib(n:int):
    result = [1, 1]
    for i in range(n-2):
        result.append(result[i] + result[(i + 1)])

    return np.array(result)

    """Obliczenie pierwszych n wyrazów ciągu Fibonnaciego. 
    Szczegółowy opis w zadaniu 3.
    
    Parameters:
    n (int): liczba określająca ilość wyrazów ciągu do obliczenia 
    
    Returns:
    np.ndarray: wektor n pierwszych wyrazów ciągu Fibonnaciego.
    """

def matrix_calculations(a:float):
    M = np.array([[a, 1, -a], [0, 1, 1], [-a, a, 1]])
    return np.linalg.inv(M), np.transpose(M), np.linalg.det(M)

    """Funkcja zwraca wartości obliczeń na macierzy stworzonej 
    na podstawie parametru a.  
    Szczegółowy opis w zadaniu 4.
    
    Parameters:
    a (float): wartość liczbowa 
    
    Returns:
    touple: krotka zawierająca wyniki obliczeń 
    (Minv, Mt, Mdet) - opis parametrów w zadaniu 4.
    """

def custom_matrix(m:int, n:int):
    if m > n:
        return np.full((m, n), m)
    elif n > m:
        return np.full((m, n), n)

    return None
    
    """Funkcja zwraca macierz o wymiarze mxn zgodnie 
    z opisem zadania 7.  
    
    Parameters:
    m (int): ilość wierszy macierzy
    n (int): ilość kolumn macierzy  
    
    Returns:
    np.ndarray: macierz zgodna z opisem z zadania 7.
    """