#!/usr/bin/env python3.12

from main import *

run_cases = [
    ("1", "10", "1010", (1, 2, 10)),
    ("101", "11", "10100", (5, 3, 20)),
    ("111", "1011", "11010", (7, 11, 26)),
]

submit_cases = run_cases + [
    ("0", "0", "0", (0, 0, 0)),
    ("1111", "1111", "1111", (15, 15, 15)),
    ("101010", "110011", "101010", (42, 51, 42)),
]


def test(input1, input2, input3, expected_output):
    print("---------------------------------")
    print(f"Inputs: {input1}, {input2}, {input3}")
    print(f"Expecting: {expected_output}")
    result = body_parts(input1, input2, input3)
    print(f"Actual: {result}")
    if result == expected_output:
        print("Pass")
        return True
    print("Fail")
    return False


def main():
    passed = 0
    failed = 0
    for test_case in test_cases:
        correct = test(*test_case)
        if correct:
            passed += 1
        else:
            failed += 1
    if failed == 0:
        print("============= PASS ==============")
    else:
        print("============= FAIL ==============")
    print(f"{passed} passed, {failed} failed")


test_cases = submit_cases
if "__RUN__" in globals():
    test_cases = run_cases

main()
