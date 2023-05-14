import os

directory_path = "/Users/shtosti/Dropbox/study/UZH/SS23/RBC_NLP/americasnlp2021-main/data/wixarika-spanish/dev_dicts"

# create a new directory to store the output dict files
output_dir = os.path.join(directory_path, 'dev_dict_counts')
os.makedirs(output_dir, exist_ok=True)


for file_name in os.listdir(directory_path):
    if file_name.endswith('.txt'):
        # open the text file and count the lines aka vocab size
        with open(os.path.join(directory_path, file_name), 'r') as file:
            vocab_size = 0
            for line in file:
                vocab_size += 1


        # save the terminal output to one file
        dict_file_name = os.path.join(output_dir, 'dev_dict_counts.txt')
        with open(dict_file_name, 'a') as file:
            file.write(f'{file_name} {vocab_size}\n')