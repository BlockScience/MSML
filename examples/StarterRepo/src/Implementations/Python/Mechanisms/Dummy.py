def dummy_log_results_mechanism(state, params, spaces):
    new_string = spaces[0]["a"]
    new_length = spaces[0]["c"]
    state["Dummy"]["Words"].append(new_string)
    state["Dummy"]["Total Length"] += new_length
