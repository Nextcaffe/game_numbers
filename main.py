import random
from composition import collection_of_information

while True:    
    number = random.randint(0, 999)
    print('')
    if not collection_of_information(number):
        while True:
            print('')
            if collection_of_information(number):
                break
