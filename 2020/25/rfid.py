#!/usr/bin/python3

import unittest

def transform( subject_number, loop_size):
    value = 1
    for i in range(loop_size):
        value *= subject_number
        value = value % 20201227
    return value

def generate_lookup_table(subject_number, table_size):
    table = {}
    for i in range(1,table_size):
        table[transform(subject_number,i)] = i
    return table

def find_loopsize(door_pub, card_pub, search_size = 1024):
    door_lookup = generate_lookup_table(card_pub, search_size)
    card_lookup = generate_lookup_table(door_pub, search_size)

    for encryption_key,loop_size_door in door_lookup.items():
        try:
            loop_size_card = card_lookup[encryption_key]
            return (loop_size_door, loop_size_card, encryption_key)
        except KeyError:
            pass
    return None

if __name__ == '__main__':
    # Step 1
    print(f'Step one: {find_loopsize(6552760,13233401,search_size=4096)}')