# QOSF_2023_Task1

This code addresses the task of finding two prime numbers from a given list whose sum equals a specified 'number_1'. The solution involves leveraging quantum computing with PennyLane and a brute-force optimization algorithm to minimize a cost function.

**Key Components:**

1. **Quantum Circuit**: The code defines a quantum circuit using PennyLane. It employs two quantum gates: RY (Y-axis rotation) gates and a CNOT (controlled-not) gate.

   - **RY Gates**: These gates introduce rotations to the quantum states of two qubits, each representing a prime number from the list. The specific angles of the RY gates are optimized to encode information about prime numbers into the quantum state.

   - **CNOT Gate**: This gate entangles the quantum states of the two qubits. It is crucial for performing operations that involve interactions between the qubits.

2. **Cost Function**: The optimization process relies on a cost function. The cost is defined as the absolute difference between the specified 'number_1' and the sum of the expected values (or measurements) of the two qubits. This cost quantifies how close the sum of the prime numbers encoded in the qubits is to 'number_1'.

3. **Brute-Force Optimization**: The code employs a brute-force optimization strategy, iterating through all possible combinations of prime numbers from the list. It systematically adjusts the rotation angles of the RY gates to find the angles that minimize the cost function.

4. **Output**: Once the optimization process converges, the code extracts the prime numbers corresponding to the optimized angles of the RY gates. These prime numbers are the solution to the problem, as their sum equals 'number_1'.

**Example Usage**: The code demonstrates its functionality using an example with a predefined list of prime numbers and a target 'number_1'. After optimization, it prints the two prime numbers whose sum matches the target.

While the brute-force approach works for small ranges and targets, it may become less efficient for larger numbers or lists. Consider exploring more efficient optimization algorithms if scalability is a concern.


Note: The depth was added into the explanation by passing my original explanation into ChatGPT and asking to make it more detailed. I am happy with the results.
