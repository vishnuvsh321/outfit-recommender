from recommender.data_loader import load_outfit_data
from recommender.model import recommmend_outfit

if __name__ == '__main__':
    outfit_data = load_outfit_data('outfit_data.csv')
    user_input = {'Ocassion': 'Casual'} # Example user input    
    outfit = recommmend_outfit(user_input, outfit_data)
    print("Recommended Outfit:", outfit)

