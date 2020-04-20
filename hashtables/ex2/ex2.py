#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * (length - 1)

    for t in tickets:
        hash_table_insert(hashtable, t.source, t)

    t = hash_table_retrieve(hashtable,'NONE')

    j=0
    #if t.destination != "NONE":
    #if t.destination not "NONE":
    while t.destination != "NONE":
        route[j] = t.destination
        j+=1
        t = hash_table_retrieve(hashtable, t.destination)


    return route
    #pass
