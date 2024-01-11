#!/usr/bin/env python3.12

def get_title(first_name, last_name, job):
    title = first_name + " " + last_name + " the " + job
    return title


# Don't touch below this line


def test(first_name, last_name, job):
    title = get_title(first_name, last_name, job)
    print(f"First name: {first_name}")
    print(f"Last name: {last_name}")
    print(f"Job: {job}")
    print(f"Title: {title}")
    print("=====================================")


test("Frodo", "Baggins", "warrior")
test("Bilbo", "Baggins", "thief")
test("Gandalf", "The Grey", "wizard")
test("Aragon", "Son of Arathorn", "ranger")
