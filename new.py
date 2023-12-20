python_program_content = ""
import random

# Fake data for the restaurant recommendation system
restaurants_data = [
    {"name": "Spicy Affair", "cuisine": "Indian", "rating": 4.5, "proximity": 1.2},
    {"name": "The Pasta Place", "cuisine": "Italian", "rating": 4.7, "proximity": 3.4},
    {"name": "Sushi World", "cuisine": "Japanese", "rating": 4.6, "proximity": 2.5},
    {"name": "Taco Town", "cuisine": "Mexican", "rating": 4.2, "proximity": 5.1},
    {"name": "Dragon's Breath", "cuisine": "Chinese", "rating": 4.3, "proximity": 0.9},
    {"name": "Le French Gourmet", "cuisine": "French", "rating": 4.8, "proximity": 2.2},
    {"name": "Burger Hub", "cuisine": "American", "rating": 4.1, "proximity": 3.0},
    {"name": "Green Garden", "cuisine": "Vegetarian", "rating": 4.4, "proximity": 1.8}
]

def recommend_restaurant(food_type):
    suitable_restaurants = [restaurant for restaurant in restaurants_data if restaurant['cuisine'].lower() == food_type.lower()]
    sorted_restaurants = sorted(suitable_restaurants, key=lambda x: (-x['rating'], x['proximity']))
    return sorted_restaurants

# Test cases
test_cases = [
    ("Italian", 1),
    ("indian", 1),
    ("Japanese", 1),
    ("French", 1),
    ("German", 0),
    ("Vegetarian", 1),
    ("", 0),
    ("123", 0)
]

# Function to run test cases
def run_test_cases():
    test_results = {}
    for food_type, expected_count in test_cases:
        recommendations = recommend_restaurant(food_type)
        result = "Pass" if len(recommendations) == expected_count else "Fail"
        test_results[food_type] = result
    return test_results

# Execute test cases and print results
if __name__ == "__main__":
    print("Running test cases...")
    results = run_test_cases()
    print(results)