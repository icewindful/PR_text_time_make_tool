# import re
import os


def convet_txt_type_function(select_file_name):
    file_name = select_file_name 
    print(file_name)

    split_tup = os.path.splitext(select_file_name)

    # first_file_name = split_tup[0]
    file_type = split_tup[1]

    print(file_type)

    if file_type == ".txt" :
        with open(file_name, 'r', encoding='utf-8') as file: 
            lines = file.readlines()

        #updated_lines = [line.replace(';', ':') for line in lines]

        final_lines = []
        for line in lines:
            if ' - ' in line:
                print(line)
                if ';' in line:
                    start_time, rest = line.split(' - ', 1)
                    start_time = f"{start_time} - {rest}"
                    start_time = start_time[:8].replace(';', ':') # for first eight
                    final_lines.append(f"{start_time[:8]} ")
                else:
                    final_lines.append(line.replace(';', ':'))    
            else:
                final_lines.append(line.replace(';', ':'))

        # Save the modified content back to the original file

        # Save to a new file with 'EDIT' in the filename
        # output_file_path = input_file_path.replace('.txt', 'EDIT.txt')
        output_file_path = file_name.replace('.txt', 'EDIT.txt') 

        with open(output_file_path, 'w', encoding='utf-8') as file:
            file.writelines(final_lines)

        output_file_path
    else:
        print("this file type cann't read it")



