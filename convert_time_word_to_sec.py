import re

def time_to_seconds(time_str):
    h, m, s = map(int, time_str.split(':'))
    return h * 3600 + m * 60 + s

def process_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    new_lines = []
    time_pattern = re.compile(r'(\d{2}:\d{2}:\d{2})')

    count = 0 
    for line in lines:
        match = time_pattern.search(line)
        if match:
            count = count + 1
            time_str = match.group(1)
            seconds = time_to_seconds(time_str)
            new_seconds = "〈" + str(seconds) + "〉"
            # new_line = line.replace(time_str, str(seconds))
            new_line = line.replace(time_str, new_seconds)
            new_lines.append(" 《"+ str(count)  +"》☆ ")
            new_lines.append(new_line)
        else:
            new_lines.append(line)

    new_file_path = file_path.replace('.txt', '_TIME.txt')
    with open(new_file_path, 'w', encoding='utf-8') as new_file:
        new_file.writelines(new_lines)

    return new_file_path