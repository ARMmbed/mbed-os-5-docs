import sys
import re
import subprocess

def split_into_pairs(l): 
    # looping till length l 
    for i in range(0, len(l), 2):  
        yield l[i:i + 2] 

def main(file):
    file_h = open(file, 'r')
    file   = file_h.read()
    snippet_indices = [m.start() for m in re.finditer('```', file)]
    print(snippet_indices)

    ranges = list(split_into_pairs(snippet_indices))

    blocks = {}

    for start, end in ranges:
        blocks[start] = file[start : end + 3]
        try:
            lib = blocks[start].split('Name: ')[1].split('.')[0]
            print("=================   %s   =================" % lib)
            out = subprocess.check_output(["mbed", "compile", "--config", "-v", "--prefix", lib])
            print(out)
        
        except:
            pass
    

    #print(blocks)
    print(ranges)

    #out = subprocess.check_output(["mbed", "compile", "--config", "-v"])
    #print(out)

    file_h.close()

if __name__ == '__main__':
    main(sys.argv[1])
