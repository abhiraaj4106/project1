import random

# QKD simulation using the BB84 protocol

# Step 1: Generate bases (basis) and quantum bits (qubits)
def generate_qubits(length):
    bases = [random.choice([0, 1]) for _ in range(length)]
    qubits = [random.choice([0, 1]) for _ in range(length)]
    return bases, qubits

# Step 2: patient generates her quantum bits and bases
def patient_send_qubits(length):
    bases, qubits = generate_qubits(length)
    return bases, qubits

# Step 3: server measures with his bases
def server_receive_qubits(patient_bases, patient_qubits):
    server_bases = [random.choice([0, 1]) for _ in range(len(patient_bases))]
    key = []
    for i in range(len(patient_bases)):
        if patient_bases[i] == server_bases[i]:
            key.append(patient_qubits[i])  # Part of the key
    return server_bases, key

# Step 4: patient and server compare bases to modify the key
def compare_bases(patient_bases, server_bases):
    return [i for i in range(len(patient_bases)) if patient_bases[i] == server_bases[i]]

# Start simulation
key_length = 10  # Length of the key

# patient (Device) generates and sends her key
patient_bases, patient_qubits = patient_send_qubits(key_length)

# server (Cloud) measures with his bases
server_bases, server_key = server_receive_qubits(patient_bases, patient_qubits)

# Both parties compare their bases
matching_bases = compare_bases(patient_bases, server_bases)

# Final shared key
shared_key = [patient_qubits[i] for i in matching_bases]

print("patient's bases:", patient_bases)
print("server's bases:   ", server_bases)
print("Shared key:    ", shared_key)
