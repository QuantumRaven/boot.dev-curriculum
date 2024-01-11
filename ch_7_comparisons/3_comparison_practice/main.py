#!/usr/bin/env python3.12

def can_withstand_blow(hero_armor, enemy_damage):
    armor_greater = hero_armor >= enemy_damage
    return armor_greater
