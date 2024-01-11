#!/usr/bin/env python3.12

def convert_hours_to_seconds(hours):
    return hours * 60 * 60


def test(hours):
    secs = convert_hours_to_seconds(hours)
    print(f"{hours} hours is {secs} seconds")


test(10)
test(1)
test(2.5)
test(100)
test(33)
