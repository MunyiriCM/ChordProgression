#this is supposed to be a program which produces a chord progression for whatever Key that you want tom play in. It is a random progression
import random



#major scale chords

majorChords = {
    'C': ['C', 'Dm', 'Em', 'F', 'G', 'Am', 'Bdim'],
    'G': ['G', 'Am', 'Bm', 'C', 'D', 'Em', 'F#dim'],
    'D': ['D', 'Em', 'F#m', 'G', 'A', 'Bm', 'C#dim'],
    'A': ['A', 'Bm', 'C#m', 'D', 'E', 'F#m', 'G#dim'],
    'E': ['E', 'F#m', 'G#m', 'A', 'B', 'C#m', 'D#dim'],
    'B': ['B', 'C#m', 'D#m', 'E', 'F#', 'G#m', 'A#dim'],
    'F#': ['F#', 'G#m', 'A#m', 'B', 'C#', 'D#m', 'E#dim'],
    'F': ['F', 'Gm', 'Am', 'Bb', 'C', 'Dm', 'Edim'],
    'Bb': ['Bb', 'Cm', 'Dm', 'Eb', 'F', 'Gm', 'Adim'],
    'Eb': ['Eb', 'Fm', 'Gm', 'Ab', 'Bb', 'Cm', 'Ddim'],
    'Ab': ['Ab', 'Bbm', 'Cm', 'Db', 'Eb', 'Fm', 'Gdim'],
    'Db': ['Db', 'Ebm', 'Fm', 'Gb', 'Ab', 'Bbm', 'Cdim'],
    'Gb': ['Gb', 'Abm', 'Bbm', 'Cb', 'Db', 'Ebm', 'Fdim'],
    'Bbm': ['Bbm', 'Cdim', 'Db', 'Ebm', 'Fm', 'Gb', 'Ab'],
    'Em': ['Em', 'F#dim', 'G', 'Am', 'Bm', 'C', 'D'],
    'Am': ['Am', 'Bdim', 'C', 'Dm', 'Em', 'F', 'G'],
    'Dm': ['Dm', 'Edim', 'F', 'Gm', 'Am', 'Bb', 'C'],
    'Gm': ['Gm', 'Adim', 'Bb', 'Cm', 'Dm', 'Eb', 'F'],
    'Cm': ['Cm', 'Ddim', 'Eb', 'Fm', 'Gm', 'Ab', 'Bb']
}


def chord_prog(key, length=4):
    #This is a default argument, meaning the chord progression will have 4 chords by default, but the user can specify a different length if they want.
    if key not in majorChords:
        return "invalid Key. Try again : "+", ".join(majorChords.keys())
    # This checks if the user-inputted key is valid (i.e., it exists in the major_chords dictionary).

    chord=majorChords[key] #This retrieves the list of chords for the specified key from the major_chords dictionary
    progression=[]


#This is a loop that will run length times, where length is the number of chords the user wants in their progression
#The underscore (_) is used as a placeholder variable when we don't need to reference the value of the loop variable
    for _ in range(length):
        degree = random.randint(1, 7)#This generates a random integer between 1 and 7 (inclusive). Each number represents a "degree" of the musical scale.
        
        #Since the list chords is indexed starting at 0 in Python, we use degree - 1 to access the correct chord.
        progression.append(chord[degree - 1])

    return progression

# Input key from user
user_key = input("Enter the key (C, G, D, A, E, B, F#, F, Bb, Eb, Ab, Db, Gb, Bbm, Em, Am, Dm, Gm, Cm): ").upper()
progression_length = int(input("Enter the length of the progression: "))

progression = chord_prog(user_key, progression_length)
print("Generated chord progression in the key of", user_key, ":", progression)