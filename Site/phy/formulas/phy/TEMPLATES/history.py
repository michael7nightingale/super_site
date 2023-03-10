def form_history(result, literal, history):
    # global history
    if result:
        string_result = f"{literal} = {result}"
        if len(history) < 8:
            history.insert(0, string_result)
        else:
            del history[-1]
            history.insert(0, string_result)
    return history
