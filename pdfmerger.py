# Python code to merge pdf files locally
# Sensative information not suitable for onliner pdf mergers

import os
import sys
import time
from PyPDF2 import PdfFileMerger

merger = PdfFileMerger()

def merge(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".pdf"):
            path_to_file = os.path.join(directory, filename)
            merger.append(path_to_file)
    merger.write(os.path.join(directory, 'mergedfile.pdf'))
    merger.close()

if __name__ == '__main__':
    print("Enter the path to the folder:")
    while True:
        directory = input('path>')
        if directory=="":
            break
        err = merge(directory)
        if err is None:
            time.sleep(2)
            break
