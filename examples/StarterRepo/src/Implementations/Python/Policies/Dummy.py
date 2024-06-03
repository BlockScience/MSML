def dummy_letter_count_policy(state, params, spaces):
    starting_string = spaces[0]["a"]
    unique = list(set(list(starting_string)))
    length = len(starting_string) * params["DUMMY Length Multiplier"]
    return [{"a": starting_string, "b": unique, "c": length}]
