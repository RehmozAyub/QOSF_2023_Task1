# I am doing this task in PennyLane
# Importing relevant libraries

import numpy as np
import pennylane as qml
from scipy.optimize import minimize
from sympy import sieve

# First, we define the quantum device with 2 qubits (one for each prime number for the sum)
dev = qml.device("default.qubit", wires=2)

# Defining the QNode
@qml.qnode(dev)

# 'params' is the angles of rotation
def quantum_circuits(params, target):
    qml.RY(params[0], wires=0)
    qml.RY(params[1], wires=1)
    qml.CNOT(wires=[0,1])
    expval_0 = qml.expval(qml.PauliZ(0))
    expval_1 = qml.expval(qml.PauliZ(1))
    return expval_0, expval_1

def find_primes(number_1, prime_list):
    min_cost = float("inf")
    min_params = None
    
    # Nested loop to iterate through all possibilities and a != b for not selecting the same prime numbers 
    for a in range(len(prime_list)):
        for b in range(len(prime_list)):
            if a != b:
                params = [0.0, 0.0]
                
                