#!/usr/bin/env python3.12

def does_attack_hit(attack_roll, armor_class):
    should_hit = (attack_roll != 1 and attack_roll >= armor_class) or (attack_roll == 20 <= armor_class)
    return should_hit
