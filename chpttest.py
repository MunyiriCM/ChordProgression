import random

# Define major scale degrees and their corresponding chords
major_chords = {
    'C': ['C', 'Dm', 'Em', 'F', 'G', 'Am', 'Bdim'],
    'G': ['G', 'Am', 'Bm', 'C', 'D', 'Em', 'F#dim'],
    'D': ['D', 'Em', 'F#m', 'G', 'A', 'Bm', 'C#dim'],
    'A': ['A', 'Bm', 'C#m', 'D', 'E', 'F#m', 'G#dim'],
    'E': ['E', 'F#m', 'G#m', 'A', 'B', 'C#m', 'D#dim'],
    'B': ['B', 'C#m', 'D#m', 'E', 'F#', 'G#m', 'A#dim'],
    'F#': ['F#', 'G#m', 'A#m', 'B', 'C#', 'D#m', 'E#dim'],
    'F': ['F', 'Gm', 'Am', 'Bb', 'C', 'Dm', 'Edim']
}

# Function to generate a chord progression
def generate_progression(key, length=4):
    if key not in major_chords:
        return "Invalid key. Choose from: " + ", ".join(major_chords.keys())
    
    chords = major_chords[key]
    progression = []
    
    for _ in range(length):
        degree = random.randint(1, 7)  # Select a random degree between 1 and 7
        progression.append(chords[degree - 1])
    
    return progression

# Input key from user
user_key = input("Enter the key (C, G, D, A, E, B, F#, F): ").upper()
progression_length = int(input("Enter the length of the progression: "))

# Generate and print progression
progression = generate_progression(user_key, progression_length)
print("Generated chord progression in the key of", user_key, ":", progression)
