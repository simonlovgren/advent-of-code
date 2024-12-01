#!/usr/bin/python3

import rfid

# **********************************************
# Unittest
# **********************************************
class TestFunctions():

    door_pub = 17807724
    door_loopsize = 11
    card_pub = 5764801
    card_loopsize = 8
    encryption_key = 14897079

    def test_transform(self):
        assert rfid.transform(7,self.door_loopsize) == self.door_pub
        assert rfid.transform(7,self.card_loopsize) == self.card_pub

    def test_lookupgen(self):
        card_lookup = rfid.generate_lookup_table(self.door_pub, 255)
        door_lookup = rfid.generate_lookup_table(self.card_pub, 255)

        assert card_lookup[self.encryption_key] == self.card_loopsize
        assert door_lookup[self.encryption_key] == self.door_loopsize

    def test_find_loopsize(self):
        door_loopsize, card_loopsize, encryption_key = rfid.find_loopsize(self.door_pub, self.card_pub)
        assert self.door_loopsize == door_loopsize
        assert self.card_loopsize == card_loopsize
        assert self.encryption_key == encryption_key