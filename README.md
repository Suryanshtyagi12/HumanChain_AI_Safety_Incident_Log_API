# HumanChain AI Safety Incident Log API

This project provides a backend API to log, manage, and track AI safety incidents in a simple and structured manner. The API follows REST principles and uses SQLite as the database for local development.

## Table of Contents
- [Technologies Used](#technologies-used)
- [Setup Instructions](#setup-instructions)
- [API Endpoints](#api-endpoints)
- [Design Decisions](#design-decisions)
- [Challenges](#challenges)

## Technologies Used
- **Language**: Python
- **Framework**: Flask
- **Database**: SQLite (with SQLAlchemy ORM)
- **Other Libraries**: Flask-RESTful, Marshmallow (for validation)

## Setup Instructions
1. Clone the repository
    ```bash
    git clone https://github.com/Suryanshtyagi12/HumanChain_AI_Safety_Incident_Log_API.git
    cd HumanChain_AI_Safety_Incident_Log_API
    ```
2. Install dependencies
    ```bash
    pip install -r requirements.txt
    ```
3. Set up the database
    ```bash
    python setup_db.py
    ```
4. Optionally, pre-populate the database with sample data
    ```bash
    python populate_db.py
    ```
5. Run the Flask app
    ```bash
    python app.py
    ```

## API Endpoints

### `GET /incidents`
- **Action**: Retrieve all AI safety incidents.
- **Response Example**:
    ```json
    [
      { "id": 1, "title": "Incident 1", "description": "Description of Incident 1", "severity": "Medium", "reported_at": "2025-04-01T12:00:00Z" }
    ]
    ```

### `POST /incidents`
- **Action**: Log a new incident.
- **Request Body**:
    ```json
    { "title": "New Incident", "description": "Incident details", "severity": "Low" }
    ```
- **Response Example**:
    ```json
    { "id": 3, "title": "New Incident", "description": "Incident details", "severity": "Low", "reported_at": "2025-04-02T14:00:00Z" }
    ```

## Design Decisions
- Chose **Flask** for simplicity in building RESTful APIs.
- **SQLite** was chosen for its ease of use in local development.

## Challenges
- Ensuring proper error handling when validating incoming request data.

## License
MIT License
