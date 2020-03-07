def players_by_position(squads_list):
    new_list_by_position = {}
    for player in squads_list:
        position = player[1]
        new_list_by_position.setdefault(position, [])
        new_list_by_position[position].append({
            'number': player[0],
            'position': position,
            'name': player[2],
            'date_of_birth': player[3],
            'caps': player[4],
            'club': player[5],
            'country': player[6],
            'club_country': player[7],
            'year': player[8]
        })
    return new_list_by_position
        
        
