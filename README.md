# KEMET Consulting UAE

Website for KEMET CONSULTING Company based in United Arab Emirates.

🌐 **Live Site:** [kemetvision.com](https://kemetvision.com)

## Features

- ✅ Bilingual support (Arabic & English)
- ✅ Responsive design
- ✅ SEO optimized
- ✅ Modern UI/UX
- ✅ Django admin interface with Jazzmin

## Tech Stack

- **Backend:** Django 5.2.8
- **Database:** SQLite (development) / PostgreSQL (production)
- **Static Files:** WhiteNoise
- **Admin:** Django Jazzmin
- **Languages:** Arabic (RTL) & English (LTR)

## Getting Started

### Prerequisites

- Python 3.8+
- pip
- virtualenv (recommended)

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/KEMET-CONSULTING-UAE.git
   cd KEMET-CONSULTING-UAE
   ```

2. **Create and activate virtual environment:**
   ```bash
   python -m venv venv
   
   # Windows
   venv\Scripts\activate
   
   # Linux/Mac
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**
   ```bash
   # Copy the example env file
   cp .env.example .env
   
   # Edit .env and add your SECRET_KEY
   # Generate a secret key: python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
   ```

5. **Run migrations:**
   ```bash
   python manage.py migrate
   ```

6. **Create a superuser (optional):**
   ```bash
   python manage.py createsuperuser
   ```

7. **Collect static files:**
   ```bash
   python manage.py collectstatic --noinput
   ```

8. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

9. **Access the site:**
   - Homepage: `http://127.0.0.1:8000/`
   - English: `http://127.0.0.1:8000/en/`
   - Admin: `http://127.0.0.1:8000/admin/`

## Project Structure

```
KEMET-CONSULTING-UAE/
├── app/              # Main application
│   ├── models.py    # Database models
│   ├── views.py     # View functions
│   ├── urls.py      # App URLs
│   └── admin.py     # Admin configuration
├── config/          # Project settings
│   ├── settings.py  # Django settings
│   ├── urls.py      # Main URL configuration
│   └── sitemaps.py  # Sitemap configuration
├── templates/       # HTML templates
├── static/          # Static files (CSS, JS, images)
├── media/           # User uploaded files
├── locale/          # Translation files
└── manage.py        # Django management script
```

## Environment Variables

Create a `.env` file in the root directory with the following variables:

```env
DEBUG=True
SECRET_KEY=your-secret-key-here
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
```

See `.env.example` for reference.

## Internationalization (i18n)

The site supports both Arabic and English:

- **Arabic (default):** `/`
- **English:** `/en/`

### Adding Translations

1. Extract translatable strings:
   ```bash
   python manage.py makemessages -l en
   ```

2. Edit `locale/en/LC_MESSAGES/django.po`

3. Compile messages:
   ```bash
   python manage.py compilemessages
   ```

## Admin Panel

Access the admin panel at `/admin/` after creating a superuser.

The admin uses Django Jazzmin for a modern interface.

## Production Deployment

1. Set `DEBUG=False` in `.env`
2. Set a strong `SECRET_KEY`
3. Configure `ALLOWED_HOSTS` in `settings.py`
4. Use a production database (PostgreSQL recommended)
5. Set up SSL/HTTPS
6. Configure static files serving
7. Set up proper logging

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is proprietary and confidential.

## Contact

For inquiries, visit [kemetvision.com](https://kemetvision.com)

---

**Developed for KEMET Consulting UAE**
