# Django Internationalization & Localization (i18n & l10n) Project

A foundational Django practice project demonstrating internationalization (**i18n**) and localization (**l10n**) — covering static template translation, dynamic database content translation via `django-parler`, localized number/date formatting, and language switching.

---

## Features

- **Multi-Language Support:** Switch between English, Spanish, and French using Django's built-in language selection framework.
- **Static Text Translation:** Uses GNU gettext via `.po` / `.mo` files to translate template strings and view-level strings with `{% trans %}` and `_()`.
- **Dynamic Content Translation:** Uses `django-parler` to store and serve per-language translations of database model fields (e.g., `Article.title`, `Article.content`).
- **Regional Localization:** Automatically adapts numbers (e.g., decimal separators) and date/time formatting based on the active locale (`USE_L10N = True`).
- **Timezone Support:** Configured to `Asia/Karachi` timezone.
- **Language Persistence:** The selected language is remembered across requests via Django's session and `LocaleMiddleware`.

---

## Tech Stack

| Tool | Purpose |
|---|---|
| Django 6.1+ | Web framework |
| GNU gettext (`.po` / `.mo`) | Static string translations |
| `django-parler` | Dynamic database content translations |
| `django.contrib.sites` | Required by parler for multi-site support |
| SQLite | Default database |

---

## Setup & Installation

```bash
# 1. Clone and enter the project
cd django_localization

# 2. Create and activate virtual environment
python -m venv myenv
source myenv/bin/activate      # macOS/Linux
myenv\Scripts\activate         # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Apply migrations (creates DB tables including parler translation tables)
python manage.py migrate

# 5. Create a superuser (to add articles via admin panel)
python manage.py createsuperuser

# 6. Run the development server
python manage.py runserver
```

---

## Static Translation Workflow

Whenever you add new translatable text (`{% trans %}` tags in templates or `_()` in `views.py`), follow this workflow:

### 1. Generate or Update Message Files (`.po`)

```bash
python manage.py makemessages -l es
python manage.py makemessages -l fr
```

### 2. Add Your Translations

Open the `.po` files in `locale/<lang>/LC_MESSAGES/django.po` and fill in the `msgstr` fields:

```po
msgid "Number"
msgstr "Número"
```

### 3. Compile Message Files (`.mo`)

```bash
python manage.py compilemessages
```

### 4. Run the Server

```bash
python manage.py runserver
```

---

## Dynamic Content Translation (django-parler)

`django-parler` lets you store translations of **database content** (like article titles and body text) directly in the database — one row per language — without any extra translation files.

### How it works

1. Your model extends `TranslatableModel` and defines translatable fields inside `TranslatedFields(...)`.
2. Parler creates a separate DB table (`homepage_articletranslation`) that stores one row per language per object.
3. When a request comes in, parler automatically serves the translation matching the active language set by `LocaleMiddleware`.

```python
# homepage/models.py
class Article(TranslatableModel):
    translations = TranslatedFields(
        title   = models.CharField(max_length=200),
        content = models.TextField(),
    )
    created_at = models.DateTimeField(auto_now_add=True)
```

### Adding translated content

1. Go to `http://127.0.0.1:8000/admin/`
2. Open **Articles → Add Article**
3. Use the language tabs to fill in the title and content in each language (English, Español, Français)
4. Save — the homepage will now show the correct translation for the active language automatically

---

## Key Settings

```python
USE_I18N  = True   # enables translation machinery
USE_L10N  = True   # enables localized number/date formatting
TIME_ZONE = 'Asia/Karachi'

PARLER_LANGUAGES = {
    1: (
        {'code': 'en'},
        {'code': 'es'},
        {'code': 'fr'},
    ),
    'default': {
        'fallback': 'en',       # fall back to English if translation missing
        'hide_untranslated': False,
    }
}
```

> **Important:** `LocaleMiddleware` must be placed **after** `SessionMiddleware` and **before** `CommonMiddleware` in the `MIDDLEWARE` list, otherwise language selection will reset on every page load.

---

## Project Structure

```
localization_project/
│
├── homepage/                   # Django app
│   ├── templates/
│   │   └── home.html           # Template with {% trans %} tags & language switcher
│   ├── models.py               # Article model using django-parler
│   ├── views.py                # Passes greeting, number, date, and latest article to template
│   ├── admin.py                # TranslatableAdmin for managing article translations
│   └── urls.py                 # App URL patterns
│
├── locale/                     # Static translation files (gettext)
│   ├── es/LC_MESSAGES/
│   │   ├── django.po           # Spanish source translations
│   │   └── django.mo           # Compiled binary
│   └── fr/LC_MESSAGES/
│       ├── django.po           # French source translations
│       └── django.mo           # Compiled binary
│
├── localization_project/
│   ├── settings.py             # All project configuration
│   └── urls.py                 # Root URL config (includes i18n/ for set_language)
│
├── requirements.txt            # Python dependencies
├── manage.py
└── README.md
```

---

## Going Further: Fully Dynamic Translation APIs

For fully automated translation (no manual `.po` files or admin entry), you can integrate a **Translation API** that translates content on-the-fly at runtime. These APIs have both free and paid tiers:

| Provider | Free Tier | Paid |
|---|---|---|
| **Google Cloud Translation** | 500,000 chars/month free | ~$20 per 1M chars after |
| **DeepL API** | 500,000 chars/month free (DeepL API Free) | Paid plans from $6.99/mo |
| **LibreTranslate** | Unlimited (self-hosted, open source) | Hosted plans available |

**LibreTranslate** is the best choice if you want completely free and private translation — you run it on your own machine or server with no character limits.

> In a real production app, you would call one of these APIs when saving content (or on request), cache the result, and serve the cached translation — keeping your DB as the source of truth.
