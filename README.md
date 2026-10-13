# Django Internationalization & Localization (i18n & l10n) Project

A clean and foundational Django practice project demonstrating internationalization (**i18n**) and localization (**l10n**) capabilities, featuring multi-language text translation, localized date-time formatting, and regional number formatting.

---

## Features

* **Multi-Language Support:** Seamlessly switch between English, Spanish, and French using Django's language selection framework.
* **Text Translation:** Uses GNU gettext via `.po` (Portable Object) and compiled `.mo` (Machine Object) files to translate static template strings dynamically.
* **Regional Localization:** Automatically adapts numbers (e.g., decimal separators) and dates based on the active locale/language settings.

---

## Project Structure

```text
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