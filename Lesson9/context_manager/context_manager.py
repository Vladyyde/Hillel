
with open('month.txt', 'r') as file:
    content = file.read()

words = content.split()
word_count = len(words)

with open('month_reversed.txt', 'w') as file:
    reversed_words = ' '.join(reversed(words))
    file.write(reversed_words)

print(f'Word in list {word_count}')
print('reverssed file month rever.txt')
