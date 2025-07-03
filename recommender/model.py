import random

def recommmend_outfit(user_input,outfit_data):
    filtered = outfit_data[outfit_data['Occasion'] == user_input['Ocassion']]
    if filtered.empty:
        return "No Suitable outfits found."
    return filtered.sample(1).iloc[0]