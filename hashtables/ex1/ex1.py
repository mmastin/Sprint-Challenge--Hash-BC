#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    # iterating over all item weights given
    for item in range(len(weights)):
        weight_calc = limit - weights[item]
        answer = hash_table_retrieve(ht, weight_calc)
        if answer != None:
            return [item, answer]
        hash_table_insert(ht, weights[item], item)

    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
