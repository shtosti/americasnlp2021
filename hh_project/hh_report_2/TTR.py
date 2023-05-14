import os


directory_path = "/Users/shtosti/Dropbox/study/UZH/SS23/RBC_NLP/americasnlp2021-main/data/wixarika-spanish/dev_dicts"

# create a new directory to store the output
output_dir = os.path.join(directory_path, 'TTP_counts')
os.makedirs(output_dir, exist_ok=True)

for file_name in os.listdir(directory_path):
    if file_name.endswith('.txt'):
        with open(os.path.join(directory_path, file_name), 'r') as file:
            word_counts = []
            for line in file:
                word, count = line.strip().split()
                word_counts.append(int(count))
        
            total_tokens = sum(word_counts)
            num_types = len(word_counts)
            
            ttr = num_types / total_tokens
            
            # Print the TTR for each file
            print(f'{file_name} {ttr}')

            # save the terminal output to one file
            dict_file_name = os.path.join(output_dir, 'TTR_counts.txt')
            with open(dict_file_name, 'a') as file: # a for append
                file.write(f'{file_name} {ttr}\n')
