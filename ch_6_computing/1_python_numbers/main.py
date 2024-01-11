#!/usr/bin/env python3.12

def calculate_damage(sword, arrow, spear, dagger, fire):
    total_damage = sword + arrow + spear + dagger + fire
    average_damage = (sword + arrow + spear + dagger + fire) / 5
    return total_damage, average_damage
