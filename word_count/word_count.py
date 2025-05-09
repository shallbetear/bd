from collections import Counter


input_file = 'input.txt'
output_file = 'output.txt'


with open(input_file, 'r', encoding='utf-8') as f:
    text = f.read().lower()


words = text.split()


word_counts = Counter(words)


with open(output_file, 'w', encoding='utf-8') as f:
    for word, count in word_counts.items():
        f.write(f'{word}: {count}\n')
