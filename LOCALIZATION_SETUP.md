# Localization Setup Guide

This Django project now supports both Arabic and English languages with a language switcher.

## Features Implemented

1. **Internationalization (i18n) Support**
   - Added `LocaleMiddleware` to handle language detection
   - Configured supported languages: Arabic (ar) and English (en)
   - Set up locale paths for translation files

2. **Language Switcher**
   - Added a language switcher dropdown in the navigation bar
   - Switches between Arabic and English
   - Preserves the current page when switching languages

3. **Template Updates**
   - All text content wrapped with `{% trans %}` or `{% blocktrans %}` tags
   - HTML `lang` and `dir` attributes dynamically set based on selected language
   - RTL (Right-to-Left) for Arabic, LTR (Left-to-Right) for English

4. **Translation Files**
   - Created English translation file at `locale/en/LC_MESSAGES/django.po`
   - Contains all translatable strings from templates

5. **CSS Updates**
   - Added styles for language switcher
   - Support for both RTL and LTR layouts
   - Responsive design for mobile devices

## How to Compile Translation Messages

To compile the translation files (requires GNU gettext tools):

```bash
python manage.py compilemessages
```

If you don't have gettext installed, you can install it:
- **Windows**: Download from https://mlocati.github.io/articles/gettext-iconv-windows.html
- **Linux**: `sudo apt-get install gettext` (Ubuntu/Debian) or `sudo yum install gettext` (CentOS/RHEL)
- **macOS**: `brew install gettext`

## How to Update Translations

1. After modifying translatable strings in templates, run:
   ```bash
   python manage.py makemessages -l en
   ```

2. Edit `locale/en/LC_MESSAGES/django.po` to update translations

3. Compile the messages:
   ```bash
   python manage.py compilemessages
   ```

## URL Structure

- Arabic (default): `/` (no prefix)
- English: `/en/`

The language switcher automatically handles URL prefixes when switching languages.

## Testing

1. Start the development server:
   ```bash
   python manage.py runserver
   ```

2. Visit the homepage and use the language switcher in the navigation bar

3. Verify that:
   - Text changes to English when English is selected
   - Page direction changes from RTL to LTR
   - Navigation and layout remain consistent
   - Language preference persists during navigation

## Notes

- The default language is Arabic (ar)
- Language preference is stored in session/cookie
- All static text in templates is translatable
- Database content (from models) is not automatically translated - you may need to add multilingual fields if needed

