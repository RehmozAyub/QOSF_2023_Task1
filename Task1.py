# I am doing this task in PennyLane

import pennylane as qml
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
                params[0] = 2.0 * (a / len(prime_list)) - 1
                params[1] = 2.0 * (b / len(prime_list)) - 1
                
                expval_0, expval_1 = quantum_circuits(params, number_1)
                cost = abs(number_1 - (expval_0 + expval_1))
                
                if cost < min_cost:
                    min_cost = cost
                    min_params = params
    
    # Now, we extract the prime number from the optimized angles
    a = int((min_params[0] + 1.0) * len(prime_list)/ 2.0)
    b = int((min_params[1] + 1.0) * len(prime_list)/ 2.0)
    
    number_a = prime_list[a]
    number_b = prime_list[b]
    
    return f"{number_a},{number_b}"

# An example to show how it's used (for some reason, I cannot make it work for all ranges and number_1 variable but it solves the task 1 example problem)
prime_list = list(sieve.primerange(2, 20))
number_1 = 18
A = find_primes(number_1, prime_list)
print(A)