#!/usr/bin/env python3.12

def take_magic_damage(health, resist, amp, spell_power):
    return health - ((amp * spell_power) - resist)
