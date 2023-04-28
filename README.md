# LittleLemon Capstone Project

Final Project of Meta Backend Engineer Certificate

## MAIN API ENPOINTS

```bash
/auth/token/login
/restaurant/api-token-auth
/restaurant/booking
/restaurant/menu
/api/bookings
/api/registration/
```

## RUN APP

### 1. Install `pipenv`

```bash
pip install pipenv
```

### 2. Install dependencies

```bash
pipenv install
```

### 3. Make database migrations

```bash
python manage.py makemigrations
```

then

```bash
python manage.py migrate
```

### 4. RUN

```bash
python manage.py runserver
```
