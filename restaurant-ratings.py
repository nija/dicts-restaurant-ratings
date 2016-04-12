import random

def get_initial_ratings(text_file, restaurants):
    '''Takes a file of restaurants and ratings, adds them to the restaurant 
    dict, returns nothing'''

    restaurant_file = open(text_file)

    for line in restaurant_file:
        restaurant, rating = line.strip().split(":")
        restaurants[restaurant] = int(rating)

    restaurant_file.close()

    return None



def pretty_print_restaurants(restaurants):
    '''Takes a dict of restaurants and prints it alphabetically. 
    Returns nothing'''

    for restaurant in sorted(restaurants):
        print (restaurant 
            + " is rated at " 
            + str(restaurants[restaurant]) 
            + ".")

    return None



def process_user_input(restaurants):
    '''Takes a dict of restaurants and adds the user's restaurant and 
    restaurant rating'''
    
    user_restaurant = raw_input("Choose a restaurant: ")
    rating = raw_input("What do you rate this restaurant (1-5) ? ")

    restaurants[user_restaurant] = int(rating)

    return None



def update_random_restaurant_rating(restaurants):
    '''Takes a dict of restaurants and prompts user to rate multiple 
    random restaurant and updates restaurant ratings until they decide 
    to quit.'''

    random_restaurant_rating = None

    username = raw_input("Hello user, what is your name? ")
    print "Hi %s" % (username)

    while random_restaurant_rating != 'q':
        random_restaurant = random.choice(restaurants.keys())

        random_restaurant_rating = raw_input("%s, what would you rate %s (q to quit)? " 
            % (username, random_restaurant))

        if random_restaurant_rating == 'q':
            break

        restaurants[random_restaurant] = int(random_restaurant_rating)




restaurants = {}

get_initial_ratings("scores.txt", restaurants)
process_user_input(restaurants)
pretty_print_restaurants(restaurants)
update_random_restaurant_rating(restaurants)
pretty_print_restaurants(restaurants)