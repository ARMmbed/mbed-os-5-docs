import sys, os
import re
import subprocess

def split_into_pairs(l):
    for i in range(0, len(l), 2):
        yield l[i:i + 2]

def main(file):
    file_h = open(file, 'r+')
    file   = file_h.read()
    snippet_indices = [m.start() for m in re.finditer('```', file)]

    blocks = {}
    for i in range(0, int(len(snippet_indices) / 2)):
        # Need to rerun on every loop as the indices change each iteration
        snippet_indices = [m.start() for m in re.finditer('```', file)]
        ranges = list(split_into_pairs(snippet_indices))
        start  = ranges[i][0]
        end    = ranges[i][1]

        print(snippet_indices)

        try:
            blocks[i] = file[start : end + 3]
            if ('Name: ' in blocks[i]):
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

    file_h.truncate(0)
    file_h.seek(0)
    file_h.write(file)
    file_h.close()

if __name__ == '__main__':
    if (len(sys.argv) < 2):
        path = '../docs/reference/configuration'
    else:
        path = sys.argv[1]

    if (path == '-h' or path == '--help'):
        print("By default the script runs out of the docs tools directory and iterates through reference/configuration.\n"
              "You may pass in a directory path that will run on all files contained within, or a single file path optionally.")
        exit(0)

    if (os.path.isfile(path)):
        main(path)
    else:
        for doc in os.listdir(path):
            if (doc != 'configuration.md'):
                print('_____ %s _____' % os.path.join(path, doc))
                main(os.path.join(path, doc))
