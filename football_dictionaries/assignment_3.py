from football_dictionaries.assignment_2 import players_by_position, player_to_dictionary
def players_by_country_and_position(squads_list):
    import itertools
    new_list = {}
    for key, value in itertools.groupby(squads_list, key = lambda item: itme[6]):
        new_list[key] = players_by_position(value)
    return new_list

