#!/usr/bin/env python3.12

def should_serve_customer(customer_age, on_break, time):
    if 5 <= time <= 10 and not on_break and customer_age >= 21:
        return True
    else:
        return False
