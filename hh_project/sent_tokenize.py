

import os
import nltk
from nltk.tokenize import sent_tokenize

# specify directory path in terminal
directory_path = input("Enter the path to the directory: ")  # get the path to the directory from terminal
file_name = input("Enter the name of the file: ")  # get the name of the file from terminal

print(f"Directory path: {directory_path}")
print(f"File name: {file_name}")

# open the text file and tokenize it by sentence
with open(os.path.join(directory_path, file_name), 'r') as file:
    content = file.read()

sentences = sent_tokenize(content)

# print the tokenized sentences
for sentence in sentences:
    print(sentence)

# save the tokenized sentences to a file
output_dir = os.path.join(directory_path, 'train_sent_tokenized')
os.makedirs(output_dir, exist_ok=True)

# save the tokenized sentences to a file, with the name of the original file + _sent_tokenized
output_file_name = os.path.join(output_dir, file_name + '_sent_tokenized.txt')
with open(output_file_name, 'w') as output_file:
    for sentence in sentences:
        output_file.write(f'{sentence}\n')
