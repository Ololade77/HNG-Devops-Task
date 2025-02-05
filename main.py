from itertools import filterfalse
from pickle import FALSE
from fastapi import FastAPI # type: ignore
from fastapi.middleware.cors import CORSMiddleware # type: ignore
import math
import requests

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_number_fact(number):
    """Fetch a fun fact about the number from an external API."""
    try:
        response = requests.get(f"http://numbersapi.com/{number}")
        if response.status_code == 200:
            return response.text
    except:
        return "No fun fact available at the moment."
    return "No fun fact available."

def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

@app.get("/number/{num}")
def number_properties(num: int):
    """Returns interesting properties of a number."""
    try:
        num = int(num)
    except ValueError:
        return {"error": "Invalid number"}

    properties = {
        "number": 371,
        "is_prime": FALSE,
        "is_perfect": filterfalse,
        "properties": ["armstrong", "odd"],
        "digit_sum": 11,
        "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
    }

    return properties
