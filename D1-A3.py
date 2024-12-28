from collections import Counter
def replace_missing_spaces(string):
    freq = Counter(string.replace(" ", ""))
    least_frequent = min(freq, key=freq.get)
    return string.replace(" ", least_frequent)
text = "a b c d e a"
print("Modified String:", replace_missing_spaces(text))
