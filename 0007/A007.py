import re
import os


def analyse_code_dir(dirpath):
    if os.path.exists(dirpath):
        for dirpath, dirname, dirfiles in os.walk(dirpath):
            for file in dirfiles:
                if file.endswith('.py'):
                    abspath = os.path.join(dirpath, file)
                    (code_lines, blank_lines, comment_lines) = analyse_code_file(abspath)
                    print(abspath + '\n' +
                          'code_lines: ' + str(code_lines) + '\n' +
                          'blank_lines: ' + str(blank_lines) + '\n' +
                          'comment_lines: ' + str(comment_lines) + '\n');

def analyse_code_file(filepath):
    """
    analyse code_lines, blank_lines, comment_lines in a code file
    :param filepath:  code file path
    :return: code_lines, blank_lines, comment_lines
    """
    file = open(filepath)

    code_lines, blank_lines, comment_lines = 0, 0, 0
    is_comment = False
    for line in file:
        if is_comment is True:
            if line.endswith("'''\n") or line.endswith('"""\n'):
                is_comment = False
            comment_lines += 1
            continue

        if line == '\n':
            blank_lines += 1
        elif line.strip().startswith('#'):
            comment_lines += 1
        elif line.strip().startswith('"""') or line.strip().startswith("'''"):
            comment_lines += 1
            is_comment = True
        else:
            code_lines += 1

    return (code_lines, blank_lines, comment_lines)

if __name__ == '__main__':
    dirpath = os.path.abspath('.')
    analyse_code_dir(dirpath)