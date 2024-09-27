def print_models(unprinted_designs, completed_models):
    """ Print each design and move to new list """
    while unprinted_designs:
        current_model = unprinted_designs.pop()
        print(f"Working on {current_model}")
        completed_models.append(current_model)


def show_completed_models(completed_models):
    """ Show completed models """
    print("Completed models are:")
    for model in completed_models:
        print(f'\t {model}')

unprinted_designs = ['honda', 'bmw', 'jaguar']
completed_models = []

print_models(unprinted_designs[:], completed_models)
show_completed_models(completed_models)


