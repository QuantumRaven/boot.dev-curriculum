#!/usr/bin/env python3.12

def check_parking_meter(time_parked, time_purchased):
    if time_parked >= time_purchased:
        return "overtime charged"
    elif time_parked <= time_purchased:
        return "no charges yet"
