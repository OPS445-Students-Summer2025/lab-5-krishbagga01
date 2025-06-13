#!/usr/bin/env python3
# Author ID: 148191232

def read_file_string(file_name):
    try:
        with open(file_name, 'r') as f:
            return f.read()
    except:
        return ''

def read_file_list(file_name):
    try:
        with open(file_name, 'r') as f:
            return [line.strip() for line in f.readlines()]
    except:
        return []

def append_file_string(file_name, string_of_lines):
    try:
        with open(file_name, 'a') as f:
            f.write(string_of_lines)
    except:
        pass

def write_file_list(file_name, list_of_lines):
    try:
        with open(file_name, 'w') as f:
            for line in list_of_lines:
                f.write(line + '\n')
    except:
        pass

def copy_file_add_line_numbers(file_name_read, file_name_write):
    try:
        with open(file_name_read, 'r') as fr:
            lines = fr.readlines()
        with open(file_name_write, 'w') as fw:
            for index, line in enumerate(lines, start=1):
                fw.write(f"{index}:{line.strip()}\n")
    except:
        pass

if __name__ == '__main__':
    file1 = 'seneca1.txt'
    file2 = 'seneca2.txt'
    file3 = 'seneca3.txt'
    string1 = 'First Line\nSecond Line\nThird Line\n'
    list1 = ['Line 1', 'Line 2', 'Line 3']
    append_file_string(file1, string1)
    print(read_file_string(file1), end='')
    write_file_list(file2, list1)
    print(read_file_string(file2), end='')
    copy_file_add_line_numbers(file2, file3)
    print(read_file_string(file3), end='')

