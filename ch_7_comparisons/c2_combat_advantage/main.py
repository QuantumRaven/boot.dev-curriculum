#!/usr/bin/env python3.12

def combat_evaluation(player_power, enemy_defense):
    advantage, disadvantage, evenly_matched = False, False, False

    # your code here
    strong_player = player_power > enemy_defense
    strong_enemy = player_power < enemy_defense

    if strong_player > strong_enemy:
        return True
    elif strong_player == strong_enemy:
        return True
    else:
        return advantage, disadvantage, evenly_matched
