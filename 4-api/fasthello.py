from fastapi import FastAPI

app = FastAPI()  # Create a FastAPI instance

@app.get("/")    # Define a route
def root():      # Define a function that will be called when the route is requested
    return {"message": "Hello World"} # Serializes to JSON automatically


@app.get("/hi/{name}")  # Define a route with a path parameter
def say_hi(name: str):  # Define a function that takes a name as a parameter
    return {"message": f"Hi, {name}"}


#Function named roll_dice. It takes two integer arguments: number, which specifies how many dice to roll, 
#and sides, which specifies how many sides each die has (e.g., 6 for a standard die).

# The phrase for _ in range(number) is a  construct used for looping a specific number of times 
#when you don't need to use the loop counter inside the loop's body.


@app.get("/roll/{number}d{sides}")  # Define a route with two path parameters
def roll_dice(number: int, sides: int):  # Define a function that takes two parameters
    import random  # Import the random module
    rolls = [random.randint(1, sides) for _ in range(number)] 
    return {
        "number_of_rolls": number,
        "number_of_sides": sides,
        "total_of_rolls": sum(rolls)
    }  # Return the rolls as a JSON response
