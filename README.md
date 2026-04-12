# Precision Plastic Lab

ระบบจัดการคลินิกศัลยกรรมพลาสติก (Precision Plastic Lab System) พัฒนาด้วย Django 6 และ Django Ninja

---

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend Framework | [Django 6.0+](https://www.djangoproject.com/) |
| API Layer | [Django Ninja 1.6+](https://django-ninja.dev/) (FastAPI-style REST) |
| Database | PostgreSQL 15 |
| Frontend | HTML + [Tailwind CSS](https://tailwindcss.com/) (CDN) + [HTMX](https://htmx.org/) |
| Package Manager | [uv](https://docs.astral.sh/uv/) |
| Runtime | Python 3.12+ |

**Dependencies หลัก**
- `django-ninja` — API routing + Pydantic schema validation
- `django-extensions` — shell_plus และ utilities เพิ่มเติม
- `psycopg2-binary` — PostgreSQL adapter
- `python-dotenv` — โหลด environment variables จาก `.env`
- `ipython` — interactive shell ที่ดีกว่า default

---

## การติดตั้งและรันโปรเจค

### 1. Clone และติดตั้ง dependencies

```bash
git clone <repo-url>
cd django-ninja

# ติดตั้ง dependencies ด้วย uv
uv sync
```

### 2. ตั้งค่า Environment Variables

สร้างไฟล์ `.env` ที่ root ของโปรเจค:

```env
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Database
DB_NAME=precision_plastic_lab
DB_USER=postgres
DB_PASSWORD=postgrespassword
DB_HOST=localhost
DB_PORT=5432

# Email (Gmail SMTP)
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
```

### 3. เริ่มต้น Database ด้วย Docker

```bash
docker-compose up -d
```

| Service | URL | Credentials |
|---------|-----|-------------|
| PostgreSQL | `localhost:5432` | user: `postgres` / pass: `postgrespassword` |
| pgAdmin 4 | `http://localhost:5050` | email: `admin@admin.com` / pass: `adminpassword` |

### 4. Migrate และรัน Server

```bash
# สร้างตาราง database
uv run python manage.py migrate

# รัน development server
uv run python manage.py runserver
```

เปิด browser ที่ `http://localhost:8000`

---

## คำสั่งที่ใช้บ่อย

```bash
# ติดตั้ง / อัปเดต dependencies
uv sync

# รัน development server
uv run python manage.py runserver

# สร้าง migration files หลังแก้ไข models
uv run python manage.py makemigrations

# Apply migrations
uv run python manage.py migrate

# รัน tests ทั้งหมด
uv run python manage.py test

# รัน tests เฉพาะ app
uv run python manage.py test apps.users
uv run python manage.py test apps.dashboard

# Django shell พร้อม models auto-import
uv run python manage.py shell_plus

# สร้าง superuser
uv run python manage.py createsuperuser
```

---

## โครงสร้างโปรเจค

```
precision-plastic-lab/
│
├── apps/                          # Django applications
│   ├── users/                     # Authentication — login, register, forgot password, logout
│   │   ├── schemas/               # Pydantic request validation schemas
│   │   │   ├── login_schema.py
│   │   │   ├── register_schema.py
│   │   │   └── forgot_password_schema.py
│   │   ├── services/              # Business logic (services pattern)
│   │   │   ├── login_service.py
│   │   │   ├── register_service.py
│   │   │   ├── forgot_service.py
│   │   │   └── logout_service.py
│   │   ├── templates/             # HTML templates ของ users app
│   │   │   ├── login.html
│   │   │   ├── register.html
│   │   │   ├── forgot_password.html
│   │   │   ├── forgot_password_email.html
│   │   │   └── unauthorized.html
│   │   └── api.py                 # Route definitions (user_router)
│   │
│   └── dashboard/                 # Post-login main interface
│       ├── services/
│       │   └── dashboard_service.py
│       ├── templates/
│       └── api.py                 # Route definitions (dashboard_router)
│
├── precision_plastic_lab/         # Project configuration
│   ├── settings.py                # Django settings
│   ├── urls.py                    # Root URL config
│   ├── api.py                     # NinjaAPI aggregator — รวม routers ทั้งหมด
│   ├── asgi.py
│   └── wsgi.py
│
├── utils/                         # Shared utilities
│   ├── session_auth.py            # CustomSessionAuth — redirect unauthenticated users
│   └── templates/
│       └── menu_base.html         # Base template สำหรับ dashboard
│
├── docker-compose.yml             # PostgreSQL + pgAdmin
├── pyproject.toml                 # Project metadata และ dependencies (uv)
├── manage.py
└── .env                           # Environment variables (ไม่ commit)
```

---

## URL Routes

### Public Routes (ไม่ต้อง login)

| Method | URL | คำอธิบาย |
|--------|-----|----------|
| GET | `/` | หน้า Login |
| POST | `/login` | ส่งข้อมูล Login |
| GET | `/register` | หน้า Register |
| POST | `/register` | สมัครสมาชิก |
| GET | `/forgot-password` | หน้า Forgot Password |
| POST | `/forgot-password` | ส่ง email reset password |
| GET | `/logout` | Logout |
| GET | `/unauthorized` | หน้าแจ้ง unauthorized |

### Protected Routes (ต้อง login)

| Method | URL | คำอธิบาย |
|--------|-----|----------|
| GET | `/dashboard/` | หน้า Dashboard หลัก |

---

## Architecture

### Services Pattern

Business logic ทั้งหมดอยู่ใน `services/` ของแต่ละ app — views และ API handlers เพียงแค่ delegate ต่อให้ service ทันที

```
Request → api.py (route) → service.py (logic) → HttpResponse
```

### API Routing

แต่ละ app มี `Router` ของตัวเอง รวมกันใน `precision_plastic_lab/api.py`:

```python
api = NinjaAPI(docs_url=None)
api.add_router("", user_router)                          # public
api.add_router("", dashboard_router, auth=CustomSessionAuth())  # protected
```

### Authentication

Session-based auth ผ่าน `CustomSessionAuth` (`utils/session_auth.py`):
- Dashboard routes ทั้งหมดถูก protect ด้วย `CustomSessionAuth`
- หาก unauthenticated จะ redirect ไปที่ `/unauthorized`
- Login สำเร็จ: session expiry 8 ชั่วโมง (กด Remember Me) หรือหมดเมื่อปิด browser

### HTML Fragment Responses (HTMX)

Services คืน `HttpResponse` ที่มี HTML fragment สำเร็จรูป สำหรับ HTMX partial update:
- หน้า full-page ใช้ `render()` กับ template files
- Partial responses (form feedback) ใช้ inline Tailwind-styled HTML strings
