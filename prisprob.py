from Prisoner import Prisoner
from Box import Box
import random


def main():
    # Initializing list of prisonors
    list_of_prisoners = []
    for n in range(100):
        list_of_prisoners.append(Prisoner(n))

    # Initializing list of boxes
    list_of_boxes = []
    # to set up what is inside boxes
    random_val_array = [n for n in range(100)]
    random.shuffle(random_val_array)
    # print(random_val_array)

    # Initializing array of boxes
    for n in range(100):
        list_of_boxes.append(Box(n, random_val_array[n]))

    # misc inits
    false_ones = 0
    correct_ones = 0

    for n in range(10000):
        temp = True
        for n in range(100):
            if (not check_if_in_loop(list_of_prisoners[n], list_of_boxes)):
                temp = False
        if (temp):
            correct_ones = correct_ones + 1
        else:
            false_ones = false_ones + 1

        random.shuffle(random_val_array)
        for curbox in list_of_boxes:
            curbox.set_val_in_box(
                random_val_array[list_of_boxes.index(curbox)])
    print(correct_ones / (correct_ones + false_ones))


def check_if_in_loop(prisoner, list_of_boxes):
    nextbox = list_of_boxes[prisoner.id]
    counter = 0
    while (prisoner.id != nextbox.val_in_box):
        counter = counter + 1
        nextbox = list_of_boxes[nextbox.val_in_box]
    return counter < 50


main()
