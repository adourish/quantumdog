


import cirq

# Define the qubits
qubits = [cirq.GridQubit(k, 0) for k in range(3)]

# Define the gates
gates = [cirq.H(qubits[0]), cirq.CNOT(qubits[0], qubits[1]), cirq.CNOT(qubits[1], qubits[2]), cirq.measure(*qubits, key='result')]

# Create a circuit
circuit = cirq.Circuit()

# Append gates to the circuit
circuit.append(gates)

print(circuit)

simulator = cirq.Simulator()
result = simulator.run(circuit)

print(result)