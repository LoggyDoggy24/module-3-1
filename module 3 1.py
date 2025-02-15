calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(string):
    count_calls()
    return len(string), string.upper(), string.lower()


def is_contains(string, list_to_search):
    count_calls()
    return string.upper() in [s.upper() for s in list_to_search]


print(string_info('Black hole'))
print(string_info('Milki way'))
print(is_contains('Earth', ['ear', 'Art', 'earth']))
print(is_contains('Core', ['ore', 'more']))
print(calls)
