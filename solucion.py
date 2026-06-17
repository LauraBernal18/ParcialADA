#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the 'bigSorting' function below.
def bigSorting(unsorted):
    unsorted.sort(key=lambda x: (len(x), x))
    return unsorted
    
if __name__ == '__main__':
    # Si se ejecuta en local, usa 'resultado.txt' de forma automática
    output_path = os.environ.get('OUTPUT_PATH', 'resultado.txt')
    fptr = open(output_path, 'w')

    n = int(input().strip())

    unsorted = []

    for _ in range(n):
        unsorted_item = input()
        unsorted.append(unsorted_item)

    result = bigSorting(unsorted)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
    print(f"\n¡Proceso terminado con éxito! El resultado se guardó en: {output_path}")
