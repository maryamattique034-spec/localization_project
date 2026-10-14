# Django Internationalization & Localization (i18n & l10n) Project

A clean and foundational Django practice project demonstrating internationalization (**i18n**) and localization (**l10n**) capabilities, featuring multi-language text translation, localized date-time formatting, and regional number formatting.

---

## Features

- **Multi-Language Support:** Seamlessly switch between English, Spanish, and French using Django's language selection framework.
- **Text Translation:** Uses GNU gettext via `.po` (Portable Object) and compiled `.mo` (Machine Object) files to translate static template strings and view contexts dynamically.
- **Regional Localization:** Automatically adapts numbers (e.g., decimal separators) and dates based on the active locale/language settings.

---

## Setup & Translation Commands Workflow

Whenever you add new translatable text (such as `{% trans %}` tags in templates or `_()` strings in `views.py`), use the following terminal workflow:

### 1. Generate or Update Message Files (`.po`)

Scan your project to create or update the portable object files for your target languages (e.g., Spanish and French):

\`\`\`bash
python manage.py makemessages -l es
python manage.py makemessages -l fr
\`\`\`

### 2. Add Your Translations

Open the generated `.po` files located in your app's `locale/` directory (e.g., `locale/es/LC_MESSAGES/django.po`) and fill in the translated text under the `msgstr` fields:

\`\`\`po
msgid "Number"
msgstr "Número"
\`\`\`

### 3. Compile Message Files (`.mo`)

Convert your text-based `.po` files into binary machine-readable files so Django can serve them at runtime:

\`\`\`bash
python manage.py compilemessages
\`\`\`

### 4. Run the Development Server

Test your changes locally in the browser:

\`\`\`bash
python manage.py runserver
\`\`\`

---

## Project Structure

\`\`\`
localization_project/
│
├── homepage/             # Django app handling views and templates
│   ├── templates/        # HTML templates using i18n tags
│   └── views.py          # View logic
│
├── locale/               # Translation files repository
│   ├── es/               # Spanish translations
│   │   └── LC_MESSAGES/
│   │       ├── django.po
│   │       └── django.mo
│   └── fr/               # French translations
│       └── LC_MESSAGES/
│           ├── django.po
│           └── django.mo
│
├── manage.py             # Django project management script
└── README.md             # Project documentation
\`\`\`
