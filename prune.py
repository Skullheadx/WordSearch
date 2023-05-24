import json

with open("words.json", 'r') as f:
    word_list = json.load(f)

print(max(word_list, key=len))
print(min(word_list, key=len))

pruned_word_list = dict()

for word in word_list:
    if len(word) >= 5 and "-" not in word:
        pruned_word_list[word] = 1


with open('pruned_words.json', 'w') as json_file:
    json.dump(pruned_word_list, json_file,indent=4)
