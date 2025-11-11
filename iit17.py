# 06/11/2025
# Quick sort Algorithm=>Quick sort ek sorting algorithm hai jisse hum list ke elements
#  ascending (chhote se bade) order me arrange karte hain.
# steps 1:choose a value in the arr to be the pivot element
# 2: order the rest of the arr so that lower value than the pivot element are on the list and higher value are on the right.

def partition(array,low,high):
    pivot=array[high]
    