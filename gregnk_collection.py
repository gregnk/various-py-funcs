'''
(c) 2023 Gregory Karastergios 
gregnk.com

Permission to use, copy, modify, and/or distribute this software for
any purpose with or without fee is hereby granted.

THE SOFTWARE IS PROVIDED “AS IS” AND THE AUTHOR DISCLAIMS ALL
WARRANTIES WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES
OF MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE
FOR ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY
DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN
AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT
OF OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
'''

from datetime import datetime
import os

# Last updated 2023-06-01
def remove_end_newline(input_str):
    if (input_str[-1:] == "\n"):
        return input_str[:-1]
    else:
        return input_str

# Last updated 2023-09-21
def remove_forbidden_file_name_chars(file_name_str):
    forbidden_chars = []

    if os.name == 'nt':
        forbidden_chars = ['<', '>', ':', '\"', '/', '\\', '|', '?', '*']
    elif os.name == 'posix':
        forbidden_chars = ['/']
    
    for char in forbidden_chars:
        file_name_str = file_name_str.replace(char, "-")
        
    return file_name_str

# Last updated 2023-06-01
# Requries import os
def get_os_dir_slash():
    if os.name == 'nt':
        return "\\"
        
    elif os.name == 'posix':
        return "/"
        
    elif os.name == 'java':
        return "/"
        
    else:
        raise Exception("Unsupported OS")
        
# Last updated 2023-06-01
# Requries from datetime import datetime
def print_current_time():
    print("Time: " + datetime.now().strftime("%Y-%m-%d @ %I:%M:%S %p"))   

# Last updated 2023-09-29
# Requries from datetime import datetime
def get_current_time():
    return "Time: " + datetime.now().strftime("%Y-%m-%d @ %I:%M:%S %p")

# Last updated 2023-09-28
# Requries from datetime import datetime
def print_iso_time():
    print(datetime.now().strftime("%Y-%m-%dT%H-%M-%S"))

# Last updated 2023-09-28
# Requries from datetime import datetime
def get_iso_time():
    return datetime.now().strftime("%Y-%m-%dT%H-%M-%S")

# Last updated 2023-09-21        
def clear_screen():
    print("\033[H\033[J")

# Last updated 2023-09-21
def escape_backslashes(input):
    return input.replace("\"", "\\\"")

# Last updated 2023-09-28
# Requires import pathlib
def get_file_ext(file):
    return (pathlib.Path(file).suffix)[1:]
