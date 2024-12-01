#!/usr/bin/env python3

import unittest


def fuel_requirement( mass ):
    return ( int( mass / 3 ) - 2 )


def total_fuel_requirement( module_weights ):
    return sum( [ fuel_requirement( w ) for w in module_weights ] )


def fuel_compensated_requirement_v1( module_weights ):
    total_requirement = total_fuel_requirement( module_weights )
    tmp_requirement = fuel_requirement( total_requirement )
    while( tmp_requirement > 0 ):
        total_requirement += tmp_requirement
        tmp_requirement = fuel_requirement( tmp_requirement )
    return total_requirement


def fuel_compensated_requirement_v2( module_weights ):
    total_requirement = 0
    for weight in module_weights:
        tmp_requirement = fuel_requirement( weight )
        additional_fuel = fuel_requirement( tmp_requirement )
        while( additional_fuel > 0 ):
            tmp_requirement += additional_fuel
            additional_fuel = fuel_requirement( additional_fuel )
        total_requirement += tmp_requirement
    return total_requirement


if __name__ == '__main__':
    module_weights = [ 119606, 94066, 80497, 136413, 83710, 136098, 113785, 100655, 148973, 78186, 75572, 68954, 140581, 76963, 123969, 111620, 106957, 80469, 140605, 119650, 112495, 124851, 119725, 93118, 123105, 92952, 131053, 74500, 135647, 107536, 56501, 64458, 115542, 111894, 51608, 85570, 133474, 118513, 109296, 128000, 87127, 146391, 149508, 107219, 70461, 85261, 137378, 138297, 106834, 112664, 53841, 124055, 96992, 91394, 135390, 119457, 84966, 110652, 138798, 65060, 108499, 126384, 116976, 135353, 52801, 53139, 54144, 69494, 52068, 61600, 62762, 102578, 100023, 119232, 97153, 94554, 114131, 54643, 65729, 124430, 106513, 133856, 96803, 132140, 113994, 65320, 123970, 115693, 129066, 132805, 143283, 132702, 109683, 126041, 63310, 82628, 68097, 58927, 123635, 117809 ]
    print( f'Part 1: {total_fuel_requirement(module_weights)}' )
    print( f'Part 2 (v1): {fuel_compensated_requirement_v1(module_weights)}' )
    print( f'Part 2 (v2): {fuel_compensated_requirement_v2(module_weights)}' )

# ######################################################################################################################
# Unit tests
# ######################################################################################################################


class TestCalculations( unittest.TestCase ):
    def test_fuel_requirement( self ):
        self.assertEqual( fuel_requirement( 12 ), 2 )
        self.assertEqual( fuel_requirement( 14 ), 2 )
        self.assertEqual( fuel_requirement( 1969 ), 654 )
        self.assertEqual( fuel_requirement( 100756 ), 33583 )

    def test_compensated_requirement_v1( self ):
        self.assertEqual( fuel_compensated_requirement_v1( [12] ), 2 )
        self.assertEqual( fuel_compensated_requirement_v1( [1969] ), 966 )
        self.assertEqual( fuel_compensated_requirement_v1( [100756] ), 50346 )

    def test_compensated_requirement_v2( self ):
        self.assertEqual( fuel_compensated_requirement_v2( [12] ), 2 )
        self.assertEqual( fuel_compensated_requirement_v2( [1969] ), 966 )
        self.assertEqual( fuel_compensated_requirement_v2( [100756] ), 50346 )