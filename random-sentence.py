# Random Sentence Generator

# Description:
# Generate a random sentence by combining random words from the given lists.
# nouns = ["cat", "dog", "house", "car", "tree"]
# verbs = ["runs", "jumps", "sleeps", "drives", "eats"]
# adjectives = ["big", "small", "fast", "slow", "green"]
# adverbs = ["quickly", "quietly", "happily", "slowly", "loudly"]'''






import random
nouns = ["cat", "dog", "house", "car", "tree"]
verbs = ["runs", "jumps", "sleeps", "drives", "eats"]
adjectives = ["big", "small", "fast", "slow", "green"]
adverbs = ["quickly", "quietly", "happily", "slowly", "loudly"]
print(F"Random sentence:{nouns[random.randint(0,len(nouns)-1)]} {verbs[random.randint(0,len(verbs)-1)]} {adjectives[random.randint(0,len(adjectives)-1)]} {adverbs[random.randint(0,len(adverbs)-1)]}")

