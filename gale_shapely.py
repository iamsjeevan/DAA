def gale_shapley(men_preferences, women_preferences):
    num_people = len(men_preferences)
    
    free_men = list(range(num_people))
    women_partner = [-1] * num_people
    men_partner = [-1] * num_people
    proposals = [0] * num_people
    
    while free_men:
        man = free_men.pop(0)
        woman = men_preferences[man][proposals[man]]
        proposals[man] += 1
        
        if women_partner[woman] == -1:
            women_partner[woman] = man
            men_partner[man] = woman
        else:
            current_partner = women_partner[woman]
            woman_preference = women_preferences[woman]
            if woman_preference.index(man) < woman_preference.index(current_partner):
                women_partner[woman] = man
                men_partner[man] = woman
                free_men.append(current_partner)
            else:
                free_men.append(man)
    
    return men_partner

num_people = int(input("Enter the number of men and women: "))

men_preferences = []
women_preferences = []

print("Enter the preferences for each man (space-separated indices):")
for i in range(num_people):
    preferences = list(map(int, input(f"Man {i+1}'s preferences: ").split()))
    men_preferences.append(preferences)

print("Enter the preferences for each woman (space-separated indices):")
for i in range(num_people):
    preferences = list(map(int, input(f"Woman {i+1}'s preferences: ").split()))
    women_preferences.append(preferences)

matches = gale_shapley(men_preferences, women_preferences)

print("Stable matchings (man -> woman):")
for man, woman in enumerate(matches):
    print(f"Man {man+1} is matched to Woman {woman+1}")


# INPUT SHOULD BE IN THIS FORMAT
# men_preferences = [
#         [0, 1, 2],  # Man 1's preferences
#         [1, 2, 0],  # Man 2's preferences
#         [1, 0, 2]   # Man 3's preferences
#     ]
    
#     women_preferences = [
#         [2, 0, 1],  # Woman 1's preferences
#         [0, 1, 2],  # Woman 2's preferences
#         [1, 2, 0]   # Woman 3's preferences
#     ]