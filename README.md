# CodeAlpha Restaurant Management System

A RESTful API to manage a restaurant's menu, tables, orders, reservations, and inventory.

## 🚀 Features
- CRUD operations for menu, tables, orders, inventory
- Reservations with customer details and guest count
- API built using Django REST Framework
- Admin panel included

## 🛠️ Technologies
- Python
- Django
- Django REST Framework
- SQLite

## 🔗 API Endpoints

| Method | Endpoint             | Description                   |
|--------|----------------------|-------------------------------|
| GET/POST | `/api/menu/`       | Manage menu items             |
| GET/POST | `/api/tables/`     | Manage tables                 |
| GET/POST | `/api/orders/`     | Place and view orders         |
| GET/POST | `/api/reservations/` | Add/view/cancel reservations |
| GET/POST | `/api/inventory/`  | Track inventory               |

## 📦 How to Run
```bash
python manage.py runserver

