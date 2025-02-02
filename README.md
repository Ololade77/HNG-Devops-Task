# Number Classification API

The **Number Classification API** is a FastAPI-based web service that accepts a number as input and returns interesting mathematical properties along with a fun fact. The API determines whether the number is prime, perfect, or an Armstrong number, calculates the digit sum, and classifies the number as odd or even. It also retrieves a fun math fact using the Numbers API.

## Table of Contents

- [Features](#features)
- [Technology Stack](#technology-stack)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Local Development](#local-development)
- [API Endpoints](#api-endpoints)
- [Usage Examples](#usage-examples)
- [License](#license)

## Features

- **Number Classification:**  
  - Determines if the number is an Armstrong number.
  - Checks if the number is prime.
  - Checks if the number is a perfect number.
  - Calculates the digit sum.
  - Classifies the number as odd or even.
- **Fun Fact Integration:**  
  - Retrieves a fun math fact from the Numbers API.
- **CORS Enabled:**  
  - Allows cross-origin requests.
- **Static File Handling:**  
  - Serves a favicon from the static directory.
- **Deployment Ready:**  
  - Configured to run as a serverless function on Vercel using the `vercel-asgi` adapter.

## Technology Stack

- **Python 3.8+**
- **FastAPI:** For building the API.
- **Uvicorn:** ASGI server for running the FastAPI app.
- **Requests:** For HTTP requests to the Numbers API.
- **Docker:** For deployment


## Project Structure


- **main.py:** Contains all the API logic, endpoints, and helper functions.
- **api/index.py:** Wraps the FastAPI app using `vercel-asgi` for Vercel deployment.
- **static/favicon.ico:** A favicon file to serve for the endpoint `/favicon.ico`.
- **requirements.txt:** Lists required packages and their versions.
- **Dockerfile:** Ship the code and deploy

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Healerkay/HNG-Devops-Task  
    ```

2. **Create and activate a virtual environment::**
    ```
    python -m venv venv
    ```
    ```
    On macOS/Linux:
    source venv/bin/activate
    ```
    ```
    On Windows:
    venv\Scripts\activate

    ```

3. **Install dependencies:::**

    ```
    pip install -r requirements.txt      

    ```  

# Local Development
Ensure you have the static directory and a favicon.ico file in it.

Run the application using Uvicorn:
```
uvicorn main:app --reload
```

# Access the API:

Root endpoint: http://127.0.0.1:8000/  

API endpoint: http://127.0.0.1:8000/api/classify-number?number=371  

Swagger UI documentation: http://127.0.0.1:8000/docs


![Alt text](./images/Screenshot%202025-02-02%20at%2019.19.24.png)
![Alt text](./images/Screenshot%202025-02-02%20at%2019.20.08.png)





# Remote Deployment using docker

![Alt text](./images/Screenshot%202025-02-02%20at%2019.20.08.png)
