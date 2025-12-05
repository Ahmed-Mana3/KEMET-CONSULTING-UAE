# Deployment Guide

## Pre-Deployment Checklist

- [ ] Set `DEBUG=False` in `.env`
- [ ] Generate a new `SECRET_KEY` for production
- [ ] Update `ALLOWED_HOSTS` in `settings.py`
- [ ] Configure production database (PostgreSQL recommended)
- [ ] Set up SSL certificate
- [ ] Configure email settings
- [ ] Run `python manage.py collectstatic`
- [ ] Run `python manage.py migrate`
- [ ] Set up proper logging
- [ ] Configure backup strategy

## Environment Variables for Production

```env
DEBUG=False
SECRET_KEY=<generate-new-secret-key>
ALLOWED_HOSTS=kemetvision.com,www.kemetvision.com
```

## Static Files

```bash
python manage.py collectstatic --noinput
```

## Database Migration

```bash
python manage.py migrate
```

## Server Configuration

Recommended: Use Gunicorn with Nginx

### Gunicorn

```bash
gunicorn config.wsgi:application --bind 0.0.0.0:8000
```

### Nginx Configuration

See your hosting provider's documentation for Nginx setup with Django.

## Security Checklist

- [ ] `DEBUG=False`
- [ ] Strong `SECRET_KEY`
- [ ] SSL/HTTPS enabled
- [ ] `ALLOWED_HOSTS` configured
- [ ] `CSRF_TRUSTED_ORIGINS` configured
- [ ] Database credentials secured
- [ ] Environment variables not in code

