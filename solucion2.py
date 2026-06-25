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
    def merge_sort_count(arr):
        if len(arr) <= 1:
            return arr, 0

        mid = len(arr) // 2

        left, left_inv = merge_sort_count(arr[:mid])
        right, right_inv = merge_sort_count(arr[mid:])

        merged = []
        i = j = 0
        split_inv = 0

        while i < len(left) and j < len(right):

            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                split_inv += len(left) - i
                j += 1

        merged.extend(left[i:])
        merged.extend(right[j:])

        total_inv = left_inv + right_inv + split_inv

        return merged, total_inv

    _, inversions = merge_sort_count(arr)

    return inversions
    
    
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