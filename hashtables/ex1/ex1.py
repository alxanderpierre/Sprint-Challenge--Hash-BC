#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert, # remmember to use below
                        hash_table_remove,
                        hash_table_retrieve, # remember to use below
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)
    for key, value in enumerate(weights):
        hash_table_insert(ht,value,key)
    #must do the same with the index and weight
    for index, weight in enumerate(weights):
        in2 = hash_table_retrieve(ht, limit - weight)
    #else:
        if in2:
            return (in2,index)
    return None

#STOP
def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
