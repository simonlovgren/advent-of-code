#!/usr/bin/env python3

import unittest
from enum import IntEnum
from itertools import product

# Op-codes
class OPCode( IntEnum ):
    ADD = 1
    MUL = 2
    END = 99

def compute( tape ):
    pc = 0
    opcode = 0
    while( opcode != OPCode.END ):
        opcode = tape[ pc ]
        if ( opcode == OPCode.ADD ):
            src1 = tape[pc + 1]
            src2 = tape[pc + 2]
            dst = tape[pc + 3]
            tape[ dst ] = tape[ src1 ] + tape[ src2 ]
        elif( opcode == OPCode.MUL ):
            src1 = tape[pc + 1]
            src2 = tape[pc + 2]
            dst = tape[pc + 3]
            tape[ dst ] = tape[ src1 ] * tape[ src2 ]
        elif (opcode == OPCode.END ):
            # End of program
            break
        else:
            print( f'Unknown Op-Code: [{opcode}] at pc [{pc}]' )
            return
        # Advance PC
        pc += 4
    return tape


def bruteforce( tape ):
    for verb,noun in product( range( 0,100 ), range(0,100 ) ):
            tape_copy = tape.copy()
            tape_copy[1] = verb
            tape_copy[2] = noun
            result = compute( tape_copy )
            if ( result[0] == 19690720 ):
                return ( 100 * verb + noun )
    return None


if __name__ == '__main__':
    tape = [1, 0, 0, 3, 1, 1, 2, 3, 1, 3, 4, 3, 1, 5, 0, 3, 2, 13, 1, 19, 1, 5, 19, 23, 2, 10, 23, 27, 1, 27, 5, 31, 2,
            9, 31, 35, 1, 35, 5, 39, 2, 6, 39, 43, 1, 43, 5, 47, 2, 47, 10, 51, 2, 51, 6, 55, 1, 5, 55, 59, 2, 10, 59,
            63, 1, 63, 6, 67, 2, 67, 6, 71, 1, 71, 5, 75, 1, 13, 75, 79, 1, 6, 79, 83, 2, 83, 13, 87, 1, 87, 6, 91, 1,
            10, 91, 95, 1, 95, 9, 99, 2, 99, 13, 103, 1, 103, 6, 107, 2, 107, 6, 111, 1, 111, 2, 115, 1, 115, 13, 0, 99,
            2, 0, 14, 0]
    tape1202 = [1, 12, 2, 3, 1, 1, 2, 3, 1, 3, 4, 3, 1, 5, 0, 3, 2, 13, 1, 19, 1, 5, 19, 23, 2, 10, 23, 27, 1, 27, 5, 31, 2,
            9, 31, 35, 1, 35, 5, 39, 2, 6, 39, 43, 1, 43, 5, 47, 2, 47, 10, 51, 2, 51, 6, 55, 1, 5, 55, 59, 2, 10, 59,
            63, 1, 63, 6, 67, 2, 67, 6, 71, 1, 71, 5, 75, 1, 13, 75, 79, 1, 6, 79, 83, 2, 83, 13, 87, 1, 87, 6, 91, 1,
            10, 91, 95, 1, 95, 9, 99, 2, 99, 13, 103, 1, 103, 6, 107, 2, 107, 6, 111, 1, 111, 2, 115, 1, 115, 13, 0, 99,
            2, 0, 14, 0]
    print(f'Part 1: {compute(tape1202)}')
    print(f'Part 2: {bruteforce(tape)}')


# ######################################################################################################################
# Unit tests
# ######################################################################################################################


class TestCalculations( unittest.TestCase ):
    def test_compute( self ):
        self.assertEqual( compute( [1,0,0,0,99] ),          [2,0,0,0,99] )
        self.assertEqual( compute( [2,3,0,3,99] ),          [2,3,0,6,99] )
        self.assertEqual( compute( [2,4,4,5,99,0] ),        [2,4,4,5,99,9801] )
        self.assertEqual( compute( [1,1,1,4,99,5,6,0,99] ), [30,1,1,4,2,5,6,0,99] )
