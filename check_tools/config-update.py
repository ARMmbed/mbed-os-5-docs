import sys, os
import re
import subprocess

def split_into_pairs(l):
    # looping till length l
    for i in range(0, len(l), 2):
        yield l[i:i + 2]

def main(file):
    file_h = open(file, 'r+')
    file   = file_h.read()
    snippet_indices = [m.start() for m in re.finditer('```', file)]

    blocks = {}
    for i in range(0, len(snippet_indices), 2):
        snippet_indices = [m.start() for m in re.finditer('```', file)]
        ranges = list(split_into_pairs(snippet_indices))
        start  = ranges[i][0]
        end    = ranges[i][1]

        try:
            blocks[i] = file[start : end + 3]
            lib = blocks[i].split('Name: ')[1].split('.')[0]
            print("=================   %s   =================" % lib)
            out = subprocess.check_output(["mbed", "compile", "--config", "-v", "--prefix", lib]).decode()
            file = file[:start+4] + out[:out.index("Macros") - 1] + file[end:]

        except Exception as e:
            print("Error")
            print(e)
            print("____________________")
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
            pass


    file_h.seek(0)
    file_h.write(file)
    file_h.close()

if __name__ == '__main__':
    main(sys.argv[1])
