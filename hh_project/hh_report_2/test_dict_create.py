
import os
import string

# set the path to the directory containing the text files
directory_path = '/Users/shtosti/Dropbox/study/UZH/SS23/RBC_NLP/americasnlp2021-main/test_data/'

# create a new directory to store the output dict files
output_dir = os.path.join(directory_path, 'test_dicts')
os.makedirs(output_dir, exist_ok=True)

# iterate over all text files in the directory
for file_name in os.listdir(directory_path):
    if file_name.endswith('.txt'):
        # open the text file and count the words
        with open(os.path.join(directory_path, file_name), 'r') as file:
            word_counts = {}
            for line in file:
                line_tokens = line.translate(str.maketrans('', '', string.punctuation)).split()
                for word in line_tokens:
                    if word not in word_counts:
                        word_counts[word] = 0
                        word_counts[word] += 1
                    else:
                        word_counts[word] += 1

        # save the dictionary to a file, sorted by value
        dict_file_name = os.path.join(output_dir, 'test_dict.' + file_name)
        with open(dict_file_name, 'w') as file:
            for key, value in sorted(word_counts.items(), key=lambda item: item[1], reverse=True):
                file.write(f'{key} {value}\n')
