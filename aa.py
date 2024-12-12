import random

# QKD simulation using the BB84 protocol

# Step 1: Generate bases (basis) and quantum bits (qubits)
def generate_qubits(length):
    bases = [random.choice([0, 1]) for _ in range(length)]
    qubits = [random.choice([0, 1]) for _ in range(length)]
    return bases, qubits

# Step 2: Alice generates her quantum bits and bases
def alice_send_qubits(length):
    bases, qubits = generate_qubits(length)
    return bases, qubits

# Step 3: Bob measures with his bases
def bob_receive_qubits(alice_bases, alice_qubits):
    bob_bases = [random.choice([0, 1]) for _ in range(len(alice_bases))]
    key = []
    for i in range(len(alice_bases)):
        if alice_bases[i] == bob_bases[i]:
            key.append(alice_qubits[i])  # Part of the key
    return bob_bases, key

# Step 4: Alice and Bob compare bases to modify the key
def compare_bases(alice_bases, bob_bases):
    return [i for i in range(len(alice_bases)) if alice_bases[i] == bob_bases[i]]

# Start simulation
key_length = 10  # Length of the key

# Alice (Device) generates and sends her key
alice_bases, alice_qubits = alice_send_qubits(key_length)

# Bob (Cloud) measures with his bases
bob_bases, bob_key = bob_receive_qubits(alice_bases, alice_qubits)

# Both parties compare their bases
matching_bases = compare_bases(alice_bases, bob_bases)

# Final shared key
shared_key = [alice_qubits[i] for i in matching_bases]

print("Alice's bases:", alice_bases)
print("Bob's bases:   ", bob_bases)
print("Shared key:    ", shared_key)
