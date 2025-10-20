# String Analyzer API

A RESTful API built with FastAPI for analyzing and storing string properties in-memory. This application allows users to submit strings, compute various properties (such as length, palindrome status, character frequency), and query stored strings using filters or natural language queries.

## Features

- **String Property Analysis**: Computes comprehensive properties for submitted strings including:
  - Length
  - Palindrome check
  - Unique character count
  - Word count
  - SHA256 hash
  - Character frequency map

- **In-Memory Storage**: Stores string records with their properties using SHA256 hashes as unique identifiers.

- **Flexible Querying**:
  - Retrieve individual strings by value
  - Filter strings by properties (palindrome, length, word count, character presence)
  - Natural language query parsing for intuitive filtering

- **CRUD Operations**: Create, read, and delete string records.

- **FastAPI Framework**: Built with FastAPI for high performance, automatic API documentation, and type safety using Pydantic models.

## Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/codenamemomi/HNG_stage_1
   cd HNG_stage_1
   ```

2. Create a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Running the Application

Start the FastAPI server using Uvicorn:

```bash
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`.

### API Documentation

Once running, visit `http://localhost:8000/docs` for interactive Swagger UI documentation, or `http://localhost:8000/redoc` for ReDoc documentation.

## API Endpoints

### Root Endpoint

- **GET** `/`
  - Returns basic application information including name, version, and uptime.

### String Operations

#### Create a String

- **POST** `/strings`
  - Creates a new string record with computed properties.
  - **Request Body**:
    ```json
    {
      "value": "example string"
    }
    ```
  - **Response**: String record with properties.
  - **Status Codes**: 201 (Created), 409 (Conflict if string already exists), 422 (Invalid input).

#### Get a String by Value

- **GET** `/strings/{string_value}`
  - Retrieves a specific string record by its value.
  - **Response**: String record with properties.
  - **Status Codes**: 200 (OK), 404 (Not Found).

#### Get All Strings

- **GET** `/strings`
  - Retrieves all stored strings, optionally filtered by query parameters.
  - **Query Parameters** (all optional):
    - `is_palindrome`: boolean
    - `min_length`: integer
    - `max_length`: integer
    - `word_count`: integer
    - `contains_character`: string
  - **Response**: List of string records with count and applied filters.
  - **Example**: `GET /strings?is_palindrome=true&min_length=5`

#### Filter by Natural Language

- **GET** `/strings/filter-by-natural-language`
  - Filters strings using natural language queries.
  - **Query Parameter**: `query` (string)
  - **Supported Queries**:
    - "palindromic strings"
    - "single word strings"
    - "strings longer than 10"
    - "strings containing the letter a"
  - **Response**: Filtered results with interpreted query.
  - **Status Codes**: 200 (OK), 400 (Invalid query).

#### Delete a String

- **DELETE** `/strings/{string_value}`
  - Deletes a string record by its value.
  - **Status Codes**: 204 (No Content), 404 (Not Found).

## Examples

### Creating a String

```bash
curl -X POST "http://localhost:8000/strings" \
     -H "Content-Type: application/json" \
     -d '{"value": "radar"}'
```

Response:
```json
{
  "id": "hash_value",
  "value": "radar",
  "properties": {
    "length": 5,
    "is_palindrome": true,
    "unique_characters": 4,
    "word_count": 1,
    "sha256_hash": "...",
    "character_frequency_map": {"r": 2, "a": 2, "d": 1}
  },
  "created_at": "2023-..."
}
```

### Filtering Strings

```bash
curl "http://localhost:8000/strings?is_palindrome=true&min_length=3"
```

### Natural Language Query

```bash
curl "http://localhost:8000/strings/filter-by-natural-language?query=palindromic%20strings%20longer%20than%205"
```

## Project Structure

```
.
├── main.py                 # FastAPI application entry point
├── core/
│   └── settings.py         # Application settings and configuration
├── api/
│   ├── utils/
│   │   ├── analyzer.py     # String property computation utilities
│   │   └── nlp_parser.py   # Natural language query parsing
│   └── v1/
│       ├── models/
│       │   └── string_model.py    # String record model
│       ├── schemas/
│       │   └── string_schema.py   # Pydantic schemas for API
│       ├── services/
│       │   └── string_service.py  # Business logic and in-memory storage
│       └── routes/
│           └── strings.py         # API route definitions
├── requirements.txt        # Python dependencies
└── .gitignore             # Git ignore patterns
```

## Dependencies

Key dependencies include:
- **FastAPI**: Web framework for building APIs
- **Pydantic**: Data validation and serialization
- **Uvicorn**: ASGI server for running FastAPI
- **Black**: Code formatter (development dependency)

See `requirements.txt` for the complete list.

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
