# Travelo

A full-stack travel management system built with **Django REST Framework** (backend) and **Angular** (frontend).

Plan trips, manage bookings, track expenses, and build itineraries — all in one place.

## Features

- **Dashboard** — Overview of trips, budgets, expenses, and top destinations
- **Trip Management** — Create, edit, and delete trips with status tracking
- **Bookings** — Manage flights, hotels, car rentals, and activities
- **Expenses** — Track spending by category with budget monitoring
- **Itinerary** — Day-by-day activity planning with timeline view

## Tech Stack

| Layer    | Technology                    |
|----------|-------------------------------|
| Backend  | Django 5, Django REST Framework |
| Frontend | Angular 19, SCSS              |
| Database | SQLite (development)          |

## Getting Started

### Prerequisites

- Python 3.10+
- Node.js 18+

### Backend Setup

```bash
cd backend
pip install -r requirements.txt
python3 manage.py migrate
python3 manage.py seed_data
python3 manage.py runserver
```

The API will be available at `http://localhost:8000/api/`.

### Frontend Setup

```bash
cd frontend
npm install
npm start
```

The app will be available at `http://localhost:4200/`.

## API Endpoints

| Method | Endpoint              | Description          |
|--------|-----------------------|----------------------|
| GET    | `/api/trips/`         | List all trips       |
| POST   | `/api/trips/`         | Create a trip        |
| GET    | `/api/trips/{id}/`    | Trip details         |
| GET    | `/api/trips/stats/`   | Dashboard statistics |
| GET    | `/api/bookings/`      | List bookings        |
| GET    | `/api/expenses/`      | List expenses        |
| GET    | `/api/itinerary/`     | List itinerary items |

## Project Structure

```
travelo/
├── backend/
│   ├── travelo/          # Django project settings
│   ├── travel/           # Travel app (models, views, API)
│   └── manage.py
└── frontend/
    └── src/app/
        ├── components/   # UI components
        ├── models/       # TypeScript interfaces
        └── services/     # API service layer
```
