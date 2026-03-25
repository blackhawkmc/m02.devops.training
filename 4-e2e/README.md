# Module 4 - End-to-end tests (TDD)

**Goal**: implement end-to-end tests using TDD

## TDD Cycle

1. **(RED)** Run tests - they will fail because Flask endpoints raise NotImplementedError
2. **(GREEN)** Implement Flask endpoints in app.py
3. **(REFACTOR)** Improve code if needed

## Steps

Create a virtualenv with the following code:

```shell
python -m venv venv
source venv/bin/activate
```

1. Install the dependencies: `pip install -r requirements.txt`
2. Open `test_e2e.py` - it defines expected API behavior
3. Open `app.py` - routes raise NotImplementedError
4. Start Flask app: `python app.py` (in one terminal)
5. Run tests in another terminal: `python test_e2e.py` - all fail (RED)
6. Implement each endpoint to make tests pass (GREEN):

   - **GET `/`** - Return "Welcome to the Flask App!"
   - **GET `/health`** - Return `{"status": "ok"}`
   - **POST `/add`** - Add a + b, return `{"result": sum}`
   - **POST `/subtract`** - Subtract a - b, return `{"result": diff}`
   - **POST `/multiply`** - Multiply a * b, return `{"result": product}`
   - **POST `/divide`** - Divide a / b, return `{"result": quotient}` or 400 if b=0

7. Ensure all tests pass

## Challenge

Add a new endpoint using TDD:
- GET `/history` - returns list of all calculations performed
- Add corresponding test first

