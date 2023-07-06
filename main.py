# TODO: Create a letter using starting_letter.txt
# TODO: Create a letter using starting_letter.txt

with open('Input/Names/invited_names.txt', mode='r') as names:
    names_list = names.readlines()
for name in names_list:
    new_name = name.strip().replace('\n', '')
    with open(f'Output/ReadyToSend/letter for {name}.txt', mode='a') as new_file, open("Input/Letters/starting_letter.txt", mode='r') as start_file:
        for line in start_file:
            new_line = line.replace('[name],', f'{name},')
            new_file.write(new_line)
