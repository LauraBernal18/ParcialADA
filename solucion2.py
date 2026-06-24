#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def insertionSort(arr):
    shifts = 0

    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                shifts += 1

    return shifts
    
if __name__ == '__main__':
    # Si se ejecuta en local, usa 'resultado.txt' de forma automática
    output_path = os.environ.get('OUTPUT_PATH', 'resultado2.txt')
    fptr = open(output_path, 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = insertionSort(arr)

        fptr.write(str(result) + '\n')

    fptr.close()
    print(f"\n¡Proceso terminado con éxito! El resultado se guardó en: {output_path}")