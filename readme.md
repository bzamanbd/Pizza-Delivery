# FastAPI Pizza Delivery App

## Overview
This project is built using FastAPI, a modern, fast (high-performance), web framework for building APIs with Python 3.7+ based on standard Python type hints.

## Features
- Fast: FastAPI is one of the fastest web frameworks available.
- Easy: Designed to be easy to use and learn, with concise and intuitive syntax.
- Automatic interactive API documentation: API endpoints are automatically documented and interactive via Swagger UI or ReDoc.
- Built-in support for data validation: Utilizes Python type annotations for request and response data validation.
- Asynchronous: Supports asynchronous programming for handling high-concurrency and I/O-bound tasks.

## Requirements
- Python 3.7+
- pip

## Installation
1. Clone the repository:
git clone https://github.com/bzamanbd/FastAPI-CRUD-Locally-without-DB

2. Navigate to the project directory:
cd PIZZA-DELIVERY

3. Create Virtual Environment:
python3 -m venv venv

4. Activate Virtual Environment:
source /venv/bin/activate

5. Install dependencies:
pip install -r requirements.txt


## Usage
1. Run the FastAPI application:
uvicorn main:app --reload

Replace `main` with the filename containing your FastAPI application instance if different.
2. Open your web browser and go to `http://localhost:8000/docs` to view the interactive API documentation.