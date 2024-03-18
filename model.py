def calculate_score(participants):
    scoreboard = []
    
    for participant in participants:
        score = (participant['chickenwings'] * 5) + (participant['hamburgers'] * 3) + (participant['hotdogs'] * 2)
        scoreboard.append({'name': participant['name'], 'score': score})
    
    #-x['score'] is used to sort the list in descending order of score
    # x['name'] is used as a secondary sorting criterion in case the scores are equal
    scoreboard.sort(key=lambda x: (-x['score'], x['name']))
    
    return scoreboard

# Example usage:
participants = [

    {'name': "Habanero Hillary", 'chickenwings': 520, 'hamburgers': 94, 'hotdogs': 911},
    {'name': "Big Bob", 'chickenwings': 120, 'hamburgers': 64, 'hotdogs': 91},
    {'name': "Speedy Gonzales", 'chickenwings': 15, 'hamburgers': 10, 'hotdogs': 8},
    {'name': "Hungry Helen", 'chickenwings': 12, 'hamburgers': 8, 'hotdogs': 15},
    {'name': "Munching Mike", 'chickenwings': 120, 'hamburgers': 64, 'hotdogs': 91}
]

result = calculate_score(participants)
print(result)
