import pandas as pd
import random

"""-----------------------------------------
Generate a realistic random dataset
-----------------------------------------"""

brands = ["Ford", "Chevy", "Toyota", "Honda", "BMW", "Volkswagen"]
models = ["LX", "Sport", "Deluxe", "GT", "SE", "Custom"]
origins = ["US", "Europe", "Japan"]

cars = []  # Create an empty list.

for i in range(50):  # generate 50 rows
    car = {  # create a dictionary, remember dictionaries use {}, not [] or ()
        "Car": f"{random.choice(brands)} {random.choice(models)}",
            # random.choice(list) → picks ONE random item from a list

        "MPG": round(random.uniform(12, 45), 1),
            # random.uniform(a, b) → returns a random FLOAT between a and b
            # round(value, 1) → round to 1 decimal place

        "Cylinders": random.choice([3, 4, 6, 8]),

        "Displacement": round(random.uniform(70, 450), 1),

        "Horsepower": random.randint(50, 250),
            # random.randint(a, b) → random INTEGER between a and b (inclusive)

        "Weight": random.randint(1500, 5000),

        "Acceleration": round(random.uniform(8, 22), 1),

        "Model": random.randint(70, 82),

        "Origin": random.choice(origins)
    }

    cars.append(car)
    # So, why do we do this?
    # Because each iteration creates one new car dictionary, and append() adds that dictionary to the list that will become your full dataset; 
    # without this step, the loop would generate 50 random cars but only the last one would remain in memory, 
    # while appending ensures every generated row is stored so pandas can convert the entire list into a complete DataFrame.

df_random = pd.DataFrame(cars)

print(df_random.head())  

"""
KEY TAKEAWAYS
    random.choice(list) → picks ONE random item from a list
    random.uniform(a, b) → returns a random FLOAT between a and b
    round(value, 1) → round to 1 decimal place
    random.randint(a, b) → random INTEGER between a and b (inclusive)
    dictionaries use {}, not [] or ()
