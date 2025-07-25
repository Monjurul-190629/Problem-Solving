def encode(strs):
    # Encode each string as: length#string
    return ''.join(f"{len(s)}#{s}" for s in strs)

def decode(s):
    res = []
    i = 0
    while i < len(s):
        # Find where the length ends (position of #)
        j = i
        while s[j] != '#':
            j += 1
        length = int(s[i:j])           # Extract length
        word = s[j + 1: j + 1 + length]  # Extract word using the length
        res.append(word)
        i = j + 1 + length             # Move to next word
    return res
