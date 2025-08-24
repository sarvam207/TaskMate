# TaskMate – Django To-Do App

TaskMate is a simple task management application built with Django.  
It allows users to create, update, and manage daily tasks.  

This project is configured to run on [Railway](https://railway.app) with PostgreSQL and Whitenoise for static file handling.

Check out live:

[TaskMate By Sarvam](https://taskmatebysarvam.up.railway.app/)
---

##  Features
- User authentication (login, logout, register)
- Create, update, delete tasks
- Mark tasks as complete/incomplete
- Mobile responsive UI
- PostgreSQL database on Railway
- Static file serving with Whitenoise

---

##  Tech Stack
- **Backend:** Django 5.x
- **Database:** PostgreSQL
- **Deployment:** Railway
- **Static Files:** Whitenoise
- **Frontend:** HTML, CSS, Bootstrap

---

##  Deployment on Railway
1. Requirements

Make sure requriements.txt is updated:

```bash
asgiref==3.9.1
crispy-bootstrap5==2025.6
Django==5.2.5
django-crispy-forms==2.4
django-environ==0.12.0
gunicorn==23.0.0
packaging==25.0
psycopg==3.2.9
psycopg-binary==3.2.9
psycopg-pool==3.2.6
pytz==2025.2
sqlparse==0.5.3
typing_extensions==4.14.1
tzdata==2025.2
whitenoise==6.9.0

```

2. Settings Adjustments:
```
BASE_DIR = Path(__file__).resolve().parent.parent

DEBUG = False

ALLOWED_HOSTS = ["https://your-app-name.up.railway.app"]  # for Railway deployment
```
## Static files
```
STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    ...
]

CSRF_TRUSTED_ORIGINS = [
    "https://your-app-name.up.railway.app",
]
```
3. Collect Static Files
```
python manage.py collectstatic --noinput
```
4. Deploy

Push code to GitHub

Connect repo to Railway


## Common Issues & Fixes
1. Static Files Not Loading
Ensure whitenoise.middleware.WhiteNoiseMiddleware is added in MIDDLEWARE

Run 
```
python manage.py collectstatic --noinput
```
Use 
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

2. CSRF Verification Failed (403)
Add your Railway domain to CSRF_TRUSTED_ORIGINS

CSRF_TRUSTED_ORIGINS = ["https://your-app-name.up.railway.app"]

3. Database Connection Refused
Make sure PostgreSQL is added in Railway
Copy the Railway DATABASE_URL into your Django settings

## Author

**Sarvam Saroha**
🔗 [LinkedIn](https://linkedin.com/in/sarvamsaroha) |
 [GitHub](https://github.com/sarvam207)
