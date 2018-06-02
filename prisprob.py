from Prisonor import Prisonor
from Box import Box
import random

def main():
    # Initilizing list of prisonors
    list_of_prisonors = []
    for n in range(100):
        list_of_prisonors.append(Prisonor(n))

    # Initilizing list of boxes
    list_of_boxes = []
    random_val_array = [] # to set up what is inside boxes
    for n in range(100):
        random_val_array.append(n)
    random.shuffle(random_val_array)
    # print(random_val_array)

    # Initilize array of boxes
    for n in range(100):
        list_of_boxes.append(Box(n, random_val_array[n]))

    #misc inits
    falseones = 0
    correctones = 0
    runningaverage = []
    
    for n in range(10000):# Testing
        temp = True
        for n in range(100):
            if (check_if_in_loop(list_of_prisonors[n], list_of_boxes) == False):
                temp = False
        if (temp):
            correctones = correctones + 1
        else:
            falseones = falseones + 1

        random.shuffle(random_val_array)
        for curbox in list_of_boxes:
            curbox.set_val_in_box(random_val_array[list_of_boxes.index(curbox)])
    print(correctones / (correctones + falseones))
 
def check_if_in_loop(prisonor, list_of_boxes):
    timeswent = 0
    nextbox = list_of_boxes[prisonor.id]
    counter = 0
    while (prisonor.id != nextbox.val_in_box):
        counter = counter + 1
        nextbox = list_of_boxes[nextbox.val_in_box]
    return counter < 50
main()


