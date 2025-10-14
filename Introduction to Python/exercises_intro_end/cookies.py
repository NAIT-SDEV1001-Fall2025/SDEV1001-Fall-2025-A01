COOKIES_PER_BAG = 40
SERVINGS_PER_BAG = 10
CALORIES_PER_SERVING = 300

# Prompt the user to input 
cookies = int(input("How many cookies did you eat? "))
calories_consumed = (cookies / COOKIES_PER_BAG) * (SERVINGS_PER_BAG * CALORIES_PER_SERVING)

print(f"You ate {cookies} cookies")
print(f"Which is equal to: {calories_consumed} calories")