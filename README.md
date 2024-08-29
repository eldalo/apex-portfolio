# APEX Portfolio

This project is an API developed with FastAPI that connects to a MongoDB database to manage portfolios.

## Prerequisites

- Python 3.8 or higher
- MongoDB (local or cloud)
- `pip` for managing Python packages

## Project Setup

### 1. Clone the Repository

Clone this repository to your local machine:

```bash
git clone https://github.com/eldalo/apex-portfolio
cd apex-portfolio
```

## 2. Create and Activate a Virtual Environment

Create a virtual environment to install dependencies without affecting your global Python environment:

```bash
python -m venv venv
```

```bash
source venv/bin/activate
```

## 3. Install Dependencies

Install the necessary dependencies listed in requirements.txt:

```bash
pip install -r requirements.txt
```

## 4. Set Up Environment Variables

Create a .env file in the root of the project with the following configuration to connect to MongoDB:

| Variable Name      | Default Value  | Required |
| ------------------ | -------------- | -------- |
| `MONGODB_USERNAME` | `apex_user`    | Yes      |
| `MONGODB_PASSWORD` | `abc123qwerty` | Yes      |
| `MONGODB_DATABASE` | `db_apex`      | Yes      |

Make sure to update the credentials and configuration according to your MongoDB environment.

## 5. Run the API

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 3002
```

The API will be available at http://localhost:3002.

### 6. Create the Dummy Data Script

Create a file named `insert_dummy_data.py` in the root of the project with the following content:

```python
import asyncio
from database import portfolio_collection

async def insert_dummy_data():
    dummy_data = [
        {
            "uuid": "123e4567-e89b-12d3-a456-426614174000",
            "channel": "online",
            "country": "USA",
            "customerCode": "CUST001",
            "items": [...],
            "route": "/home"
        },
        {
            "uuid": "123e4567-e89b-12d3-a456-426614174001",
            "channel": "offline",
            "country": "Canada",
            "customerCode": "CUST002",
            "items": [...],
            "route": "/about"
        }
    ]

    await portfolio_collection.insert_many(dummy_data)
    print("Dummy data inserted successfully")

if __name__ == "__main__":
    asyncio.run(insert_dummy_data())
```

### 7. Run the Dummy Data Script

Execute the script to insert the dummy data into your MongoDB database:

```bash
python insert_dummy_data.py
```

This script will insert a couple of example portfolios into the portfolios collection of your MongoDB database. You can then use these dummy entries to test the API endpoints.

## Endpoints

#### 1. Get Portfolios by Client

- Path: `/portfolios?clientId=:id`
- Method: GET
- Description: Retrieves a list of portfolios associated with the specified clientId.

#### 2. Get a Portfolio by ID

- Path: `/portfolios/:id`
- Method: GET
- Description: Retrieves the details of a specific portfolio by its ID.
