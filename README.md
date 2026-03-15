# InternTracker API

A backend API project for tracking internship and job applications.

## Features

- User registration and login
- JWT-based authentication
- Company CRUD
- Application CRUD
- Note CRUD
- Search, filtering, and pagination

## Tech Stack

- FastAPI
- SQLAlchemy
- SQLite
- Pydantic
- JWT
- Passlib / bcrypt

## Project Structure

```text
app/
  api/
    deps.py
    routes/
      auth.py
      companies.py
      applications.py
      notes.py
  core/
    config.py
    database.py
    security.py
  models/
    user.py
    company.py
    application.py
    note.py
  schemas/
    user.py
    auth.py
    company.py
    application.py
    note.py
  main.py
tests/
requirements.txt
README.md
```

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
uvicorn app.main:app --reload
```

## API Docs

After starting the server, open:

```text
http://127.0.0.1:8000/docs
```

## Example Workflow

1. Register a user
2. Login and authorize in Swagger UI
3. Create a company
4. Create an application linked to that company
5. Add notes to the application

## Testing

Run the basic API tests with:

```bash
pytest -q
```

## Notes

- This project currently uses SQLite for simplicity.
- Dependency versions are pinned where compatibility matters.

## Future Improvements

- Add more API tests
- Add Docker support
- Migrate from SQLite to Postgres
- Add Alembic migrations
- Add stricter validation and error handling
- Deploy the project to a cloud platform