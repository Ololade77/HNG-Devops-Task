from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
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

def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect(n):
    """Check if a number is a perfect number (sum of its divisors equals itself)."""
    if n < 2:
        return False
    return sum(i for i in range(1, n) if n % i == 0) == n

def is_armstrong(n):
    """Check if a number is an Armstrong number."""
    digits = [int(d) for d in str(n)]
    power = len(digits)
    return sum(d ** power for d in digits) == n

def digit_sum(n):
    """Calculate the sum of the digits of a number."""
    return sum(int(d) for d in str(n))

def get_number_fact(number):
    """Fetch a fun fact about the number from an external API."""
    try:
        response = requests.get(f"http://numbersapi.com/{number}")
        if response.status_code == 200:
            return response.text
    except:
        return "No fun fact available at the moment."
    return "No fun fact available."

@app.get("/number/{num}")
def number_properties(num: int):
    """Returns interesting properties of a number."""
    try:
        num = int(num)
    except ValueError:
        return {"error": "Invalid number"}

    properties = []
    if is_armstrong(num):
        properties.append("armstrong")
    if num % 2 == 1:
        properties.append("odd")
    else:
        properties.append("even")

    response = {
        "number": num,
        "is_prime": is_prime(num),
        "is_perfect": is_perfect(num),
        "properties": properties,
        "digit_sum": digit_sum(num),
        "fun_fact": f"{num} is an Armstrong number because {' + '.join(f'{d}^{len(str(num))}' for d in [int(d) for d in str(num)])} = {num}" if is_armstrong(num) else get_number_fact(num),
    }

    return response


