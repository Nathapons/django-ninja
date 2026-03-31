# Project Overview: Hospital Management System

This is a web application for a **Hospital Management System** built with **Django 6.0+** and **Django Ninja**. It uses a modular architecture with business logic separated into services, validation handled by Ninja schemas, and a custom session-based authentication layer.

## Core Technologies
- **Python**: 3.12+
- **Framework**: [Django](https://www.djangoproject.com/) 6.0+
- **API Framework**: [Django Ninja](https://django-ninja.rest-framework.com/)
- **Dependency Management**: [uv](https://github.com/astral-sh/uv)
- **Styling**: Tailwind CSS (used in server-side rendered fragments)
- **Database**: SQLite (default)

## Architecture and Design Patterns

### Directory Structure
- `apps/`: Contains modular Django applications.
  - `users/`: Handles registration, login, and authentication.
  - `dashboard/`: Main application interface after login.
- `myproject/`: Core project configuration (`settings.py`, `urls.py`, global `api.py`).
- `utils/`: Common utilities (e.g., `session_auth.py`).
- `design/`: UI/UX design mockups and HTML references.

### Development Conventions
- **Services Pattern**: Business logic is encapsulated in `services/` modules within each app.
- **Schemas**: Data validation for API requests is handled by Pydantic-based schemas in `schemas/`.
- **API Routing**: Routing is defined using Django Ninja's `Router` in `api.py` files.
- **HTMX-like approach**: Some service functions return `HttpResponse` containing raw HTML fragments (styled with Tailwind) for dynamic UI updates.
- **Authentication**: Custom session-based authentication is implemented in `utils/session_auth.py` and applied via `NinjaAPI` and `Router` configuration.

## Getting Started

### Prerequisites
Ensure you have `uv` installed.

### Installation
```bash
uv sync
```

### Running the Project
```bash
uv run python manage.py runserver
```

### Database Migrations
```bash
uv run python manage.py makemigrations
uv run python manage.py migrate
```

### Development Tools
- **Shell Plus**: Enhanced interactive shell with `ipython` and auto-loaded models.
  ```bash
  uv run python manage.py shell_plus
  ```

## Testing
Run tests using the standard Django test runner:
```bash
uv run python manage.py test
```
