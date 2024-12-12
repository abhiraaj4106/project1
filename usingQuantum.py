import random

# QKD के लिए BB84 प्रोटोकॉल का सिमुलेशन

# स्टेप 1: बेसिस (basis) और क्वांटम बिट्स (qubits) जेनरेट करना
def generate_qubits(length):
    # 0: Rectilinear basis, 1: Diagonal basis
    bases = [random.choice([0, 1]) for _ in range(length)]
    # Qubits: 0 or 1 values
    qubits = [random.choice([0, 1]) for _ in range(length)]
    return bases, qubits

# स्टेप 2: Alice (डिवाइस) अपने क्वांटम बिट्स और बेसिस जेनरेट करता है
def alice_send_qubits(length):
    bases, qubits = generate_qubits(length)
    return bases, qubits

# स्टेप 3: Bob (क्लाउड) अपने बेसिस के साथ माप करता है
def bob_receive_qubits(alice_bases, alice_qubits):
    bob_bases = [random.choice([0, 1]) for _ in range(len(alice_bases))]
    # Bob सिर्फ उन्हीं क्वांटम बिट्स को रखता है जो उसकी बेसिस से मैच होते हैं
    key = []
    for i in range(len(alice_bases)):
        if alice_bases[i] == bob_bases[i]:
            key.append(alice_qubits[i])  # कुंजी (key) का हिस्सा बनाते हैं
    return bob_bases, key

# स्टेप 4: Alice और Bob मिलकर जोड़ी गए बेसिस के अनुसार कुंजी को संशोधित करते हैं
def compare_bases(alice_bases, bob_bases):
    return [i for i in range(len(alice_bases)) if alice_bases[i] == bob_bases[i]]

# सिमुलेशन प्रारंभ
key_length = 10  # कुंजी का लंबाई

# Alice (डिवाइस) अपनी कुंजी बनाता है और भेजता है
alice_bases, alice_qubits = alice_send_qubits(key_length)

# Bob (क्लाउड) अपने आधार से माप करता है
bob_bases, bob_key = bob_receive_qubits(alice_bases, alice_qubits)

# दोनों पक्ष सहमत बेसिस की तुलना करते हैं
matching_bases = compare_bases(alice_bases, bob_bases)

# अंतिम साझा की गई कुंजी
shared_key = [alice_qubits[i] for i in matching_bases]

print("Alice's bases:", alice_bases)
print("Bob's bases:   ", bob_bases)
print("Shared key:    ", shared_key)
