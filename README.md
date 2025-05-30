# Cycle Pure Agarbattis - Production Planning System

A comprehensive production planning and management system built with Django backend and vanilla HTML/CSS/JavaScript frontend.

## Overview

This application manages production planning for Cycle Pure Agarbattis across multiple plants in India, enabling monthly planning, weekly scheduling, and machine-level production management with integrated reporting and analytics.

## Technology Stack

- **Backend**: Django 5.2.1 with Django REST Framework
- **Database**: PostgreSQL
- **Frontend**: HTML5, CSS3 (Tailwind CSS), Vanilla JavaScript
- **Charts**: Chart.js for data visualization

## Features

- **Dashboard**: Real-time production monitoring and KPIs
- **Monthly Planning**: Long-term production requirements planning
- **Weekly Scheduling**: Medium-term production plans
- **Machine Planning**: Detailed machine-level scheduling
- **Reports**: Machine efficiency and SKU-wise plan vs actual analysis
- **Multi-plant Support**: Manages 5 plants across India

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/production-planning-django.git
   cd production-planning-django
   ```

2. **Install Python dependencies**
   ```bash
   pip install django djangorestframework psycopg2-binary django-cors-headers python-decouple
   ```

3. **Set up environment variables**
   Create a `.env` file with:
   ```
   SECRET_KEY=your-secret-key
   DEBUG=True
   PGDATABASE=your-db-name
   PGUSER=your-db-user
   PGPASSWORD=your-db-password
   PGHOST=your-db-host
   PGPORT=5432
   ```

4. **Run database migrations**
   ```bash
   python manage.py migrate
   ```

5. **Initialize sample data**
   ```bash
   python manage.py init_data
   ```

6. **Start the development server**
   ```bash
   python manage.py runserver 0.0.0.0:5000
   ```

## API Endpoints

- `/api/plants/` - Plant management
- `/api/categories/` - Product categories
- `/api/sku-clusters/` - SKU cluster management
- `/api/production-lines/` - Production line management
- `/api/machines/` - Machine management
- `/api/monthly-plans/` - Monthly planning
- `/api/weekly-schedules/` - Weekly scheduling
- `/api/machine-schedules/` - Machine-level scheduling
- `/api/production-kpis/` - Production KPIs and metrics

## Project Structure

```
production-planning/
├── production_planning/        # Django project settings
├── core/                      # Main Django app
│   ├── models.py             # Database models
│   ├── views.py              # API views and frontend views
│   ├── serializers.py        # DRF serializers
│   ├── urls.py               # URL routing
│   └── management/commands/   # Custom management commands
├── templates/                 # HTML templates
│   ├── base.html             # Base template
│   └── dashboard.html        # Dashboard page
├── static/                   # Static files
│   ├── css/                  # CSS files
│   └── js/                   # JavaScript files
├── manage.py                 # Django management script
└── run_django.py            # Custom server runner
```

## Production Data

The system includes realistic production data for:
- 5 plants: Mysore, Bengaluru, Chennai, Mumbai, Hyderabad
- 4 product categories: Premium, Standard, Economy, Dhoop
- 6 SKU clusters with various product lines
- 15 production lines (3 per plant)
- 60 machines (4 per production line)
- Sample monthly plans, weekly schedules, and production KPIs

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is proprietary software for Cycle Pure Agarbattis.