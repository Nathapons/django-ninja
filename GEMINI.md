# Precision Plastic Lab

This is a **Precision Plastic Lab** built with **Django 6.0+** and **Django Ninja**. The project follows a modular architecture with a clear separation between business logic (services), API validation (schemas), and UI presentation.

## Core Technologies

- **Python**: 3.12+
- **Framework**: [Django](https://www.djangoproject.com/) 6.0+
- **API Framework**: [Django Ninja](https://django-ninja.rest-framework.com/)
- **Dependency Management**: [uv](https://github.com/astral-sh/uv)
- **Styling**: [Tailwind CSS](https://tailwindcss.com/) (used in server-side rendered HTML fragments)
- **Database**: SQLite (default)

## Architecture and Design Patterns

### Directory Structure

- `apps/`: Contains modular Django applications.
  - `users/`: Handles registration, login, and authentication.
  - `dashboard/`: Main application interface post-login.
- `myproject/`: Core project configuration (`settings.py`, `urls.py`, global `api.py`).
- `utils/`: Common utilities (e.g., `session_auth.py` for custom authentication).
- `design/`: UI/UX design mockups and reference HTML/CSS.

### Development Conventions

- **Services Pattern**: All business logic and complex view logic must be encapsulated in `services/` modules within each application (e.g., `apps/users/services/login_service.py`).
- **Schemas**: Data validation and serialization for API requests are handled by Pydantic-based schemas in `schemas/` directories (e.g., `apps/users/schemas/login_schema.py`).
- **API Routing**: Routing is defined using Django Ninja's `Router` in `api.py` files within each app, and then aggregated in `myproject/api.py`.
- **HTMX-like Approach**: Many service functions return `HttpResponse` containing raw HTML fragments styled with Tailwind CSS. This allows for dynamic UI updates by swapping content on the client side without full page reloads.
- **Authentication**: 
  - Custom session-based authentication is defined in `utils/session_auth.py` (`CustomSessionAuth`).
  - Login logic in `apps.users.services.login_service` handles session persistence and expiration.
  - Dashboard access is guarded by authentication checks in `apps.dashboard.services.dashboard_service`.

## Building and Running

### Prerequisites
Ensure you have `uv` installed on your system.

### Installation
```bash
uv sync
```

### Database Migrations
```bash
uv run python manage.py makemigrations
uv run python manage.py migrate
```

### Running the Project
```bash
uv run python manage.py runserver
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

## Design Resources
UI mockups and reference code can be found in the `design/` directory, organized by screen:
- `login_page_updated_brand/`
- `dashboard_screen/`
- `register_page_full_screen/`
- `forgot_password_screen/`
- `unauthorization_page/`
