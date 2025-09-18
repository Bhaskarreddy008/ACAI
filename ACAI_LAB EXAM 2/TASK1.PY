from collections import Counter

def top_3_words(text):
    # Normalize to lowercase and split on spaces
    words = text.lower().split()
    # Count word frequencies
    freq = Counter(words)
    # Sort by frequency descending, then lexicographically
    sorted_words = sorted(freq.items(), key=lambda x: (-x[1], x[0]))
    # Return top 3
    return sorted_words[:3]

# input 
input_text = "to be or not to be that is the question be question"
print(top_3_words(input_text))