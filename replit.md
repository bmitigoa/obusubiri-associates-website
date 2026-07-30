# Obusubiri Associates Website

A Django 6 website for Obusubiri Associates, a Kenyan consultancy firm.

## Stack

- **Framework:** Django 6.0.6
- **Database:** SQLite (`db.sqlite3`)
- **Email:** Zoho SMTP (`smtp.zoho.com:587`)
- **Python:** 3.12

## Running the app

```bash
python manage.py runserver 0.0.0.0:5000
```

The workflow "Start application" is already configured and will start automatically.

## Environment / Secrets

| Key | Purpose |
|-----|---------|
| `EMAIL_HOST_PASSWORD` | Zoho SMTP password for `info@obusubiriassociates.co.ke` |
| `SECRET_KEY` | Django secret key (optional; falls back to insecure dev default) |

## Migrations

```bash
python manage.py migrate
```

## Apps

- `core` — main site (home, about, services, training, contact, sitemap)

## User preferences

- Keep email credentials in Replit Secrets, never hardcoded in settings.py.
