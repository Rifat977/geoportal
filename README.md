
# 🌍 Geoportal

A Django web application that fetches data from [REST Countries API](https://restcountries.com/v3.1/all), stores it locally, and provides RESTful APIs and a web interface to explore countries.

## 🚀 Features

- Fetch and store country data from external API
- RESTful API for CRUD and filtering/search
- Web UI with search and detail view
- Same-region and same-language country listings
- User authentication for secured access

## 🛠️ Setup Instructions

### ✅ Prerequisites

- Python 3.10+
- PostgreSQL
- Git

### 📦 Installation

```bash
git clone https://github.com/your-username/your-repo.git
cd your-repo
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
pip install -r requirements.txt
````

### ⚙️ Database Configuration (PostgreSQL)

In your `settings.py`, configure the `DATABASES` setting with your PostgreSQL credentials:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'geoportal_db',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

Make sure PostgreSQL is running and the database is created before continuing.

### 🔧 Migrations and Data Load

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py fetch_countries
```

---

### ▶️ Run the App

```bash
python manage.py runserver
```

Visit:

* `http://127.0.0.1:8000/accounts/login/` to log in
* `http://127.0.0.1:8000/api/` for APIs
* `http://127.0.0.1:8000/countries/` for the web interface


## 👥 Authentication

Only authenticated users can access the country listing and API endpoints.
To create a user:
```bash
python manage.py createsuperuser
```