#!/usr/bin/env python3.12

def compare_heights(elon_height, sara_height, jill_height, bob_height):
    bob_same_height_as_elon = bob_height == elon_height
    sara_same_height_as_elon = sara_height == elon_height
    jill_same_height_as_sara = jill_height == sara_height
    return bob_same_height_as_elon, sara_same_height_as_elon, jill_same_height_as_sara
