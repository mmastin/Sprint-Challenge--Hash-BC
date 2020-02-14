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
    route = [None] * length

    for ticket in tickets:
        # print(ticket.source, ticket.destination)
        hash_table_insert(hashtable, ticket.source, ticket.destination)

    # where_in_the_world = hash_table_retrieve(hashtable, "NONE")
    # key = 'NONE'
    source = hash_table_retrieve(hashtable, 'NONE')
    route[0] = source

    # for airport in range(length):
    airport = 1
    while source != 'NONE':
        next_leg = hash_table_retrieve(hashtable, source)

        source = next_leg
        route[airport] = next_leg

        airport += 1

    # None was still appended to end of route
    return route[:-1]

    # for airport in range(len(length)):
    # for airport in range(length):
    #     found_ticket = hash_table_retrieve(hashtable, airport)
    #     # where_in_the_world = hash_table_retrieve(hashtable, where_in_the_world)
    #     key = found_ticket
    #     route[airport - 1] = found_ticket

    #     # hash_table_remove(hashtable, 'NONE')