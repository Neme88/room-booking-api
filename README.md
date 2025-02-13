# Room Booking API Documentation

## 📌 Project Overview
The **Room Booking API** is a **RESTful API** built using **Django REST Framework (DRF)** and **PostgreSQL**. It allows users to **Create, Read, Update, and Delete (CRUD)** room bookings for a **conference facility at Bitcube**. The API ensures data integrity through **validation checks** and provides a structured approach for handling room reservations.

## ⚡ Installation & Setup
### **1️⃣ Clone the Repository**
```bash
# Clone the project
$ git clone https://github.com/Neme88/room-booking-api.git
$ cd room-booking-api
```

### **2️⃣ Create and Activate a Virtual Environment**
```bash
# Create virtual environment
$ python -m venv venv

# Activate virtual environment
# For Linux/macOS:
$ source venv/bin/activate

# For Windows:
$ venv\Scripts\activate
```

### **3️⃣ Install Dependencies**
```bash
$ pip install -r requirements.txt
```

### **4️⃣ Set Up the Environment Variables**
Create a `.env` file in the project's root directory and add the following:
```env
SECRET_KEY='your-secret-key'
DB_NAME=bookingapidb
DB_USER=adminuser
DB_PASSWORD=yourpassword
DB_HOST=localhost
DB_PORT=5432
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
```

### **5️⃣ Run Database Migrations**
```bash
$ python manage.py makemigrations bookings
$ python manage.py migrate
```

### **6️⃣ Create a Superuser (Admin Panel Access)**
```bash
$ python manage.py createsuperuser
# Follow the prompt to set username, email, and password.
```

### **7️⃣ Start the Server**
```bash
$ python manage.py runserver
```
API will be available at: `http://127.0.0.1:8000/api/room_bookings/`

---

## 📌 Database Schema
| Attribute         | Type      | Description                                      |
|------------------|----------|--------------------------------------------------|
| `room_id`        | UUID     | Unique ID for each booking                      |
| `booked_by`      | String   | Name of the person booking                      |
| `booking_start`  | DateTime | Start date and time of the booking              |
| `duration_minutes` | Integer | Duration in minutes                             |
| `booking_end`    | DateTime | Read-only value; auto-calculated from duration  |

---

## 🌍 API Endpoints & Usage

### **1️⃣ Create a Room Booking**
**Endpoint:** `POST /api/room_bookings/`
```json
{
  "booked_by": "John Doe",
  "booking_start": "2025-02-15T10:00:00Z",
  "duration_minutes": 120
}
```
**Response:**
```json
{
  "room_id": "550e8400-e29b-41d4-a716-446655440000",
  "booked_by": "John Doe",
  "booking_start": "2025-02-15T10:00:00Z",
  "duration_minutes": 120,
  "booking_end": "2025-02-15T12:00:00Z"
}
```

### **2️⃣ Retrieve All Bookings**
**Endpoint:** `GET /api/room_bookings/`
```json
[
  {
    "room_id": "550e8400-e29b-41d4-a716-446655440000",
    "booked_by": "John Doe",
    "booking_start": "2025-02-15T10:00:00Z",
    "duration_minutes": 120,
    "booking_end": "2025-02-15T12:00:00Z"
  }
]
```

### **3️⃣ Retrieve a Single Booking**
**Endpoint:** `GET /api/room_bookings/{room_id}/`

### **4️⃣ Update a Booking**
**Endpoint:** `PUT /api/room_bookings/{room_id}/`
```json
{
  "booked_by": "Alice",
  "booking_start": "2025-02-20T14:00:00Z",
  "duration_minutes": 90
}
```

### **5️⃣ Delete a Booking**
**Endpoint:** `DELETE /api/room_bookings/{room_id}/`
**Response:**
```json
{
  "message": "Booking deleted successfully."
}
```

---

## ⚠️ Validation & Error Handling
| Error Type             | HTTP Status | Description                                        |
|------------------------|------------|----------------------------------------------------|
| `400 Bad Request`      | 400        | Invalid data format or missing required fields    |
| `404 Not Found`        | 404        | Booking not found                                 |
| `500 Internal Server Error` | 500        | Unexpected server-side error                      |

---

## 🛠️ Testing the API
### **Run Unit Tests**
## 🧪 Running Tests

To ensure the API and database logic are working correctly, run the tests using:

```bash

python manage.py test bookings.tests

```bash

## Expected Test Output 

If test is run correctly below is the expected output
```bash

Found 7 test(s).
Creating test database for alias 'default'...
System check identified no issues (0 silenced).

⚠️ WARNING: booking_end is None. The database trigger may not be working correctly.
🔧 Please check PostgreSQL triggers and ensure the function is applied.
.......
----------------------------------------------------------------------
Ran 7 tests in 0.395s

OK
Destroying test database for alias 'default'...

```

### **Run API Tests with cURL**
```bash
curl -X POST `http://127.0.0.1:8000/api/room_bookings/`\
-H "Content-Type: application/json" \
-d '{"booked_by": "Neme", "booking_start": "2025-02-15T10:00:00Z", "duration_minutes": 100}'
```

### **Run API Tests with Postman**
1. Open **Postman**.
2. Set the **Method** to `POST`.
3. Enter URL: `http://127.0.0.1:8000/api/room_bookings/`
4. Go to **Body** -> **raw** -> Select **JSON**.
5. Enter:
   ```json
   {
      "booked_by": "John Doe",
      "booking_start": "2025-02-15T10:00:00Z",
      "duration_minutes": 120
   }
   ```
6. Click **Send**.

---

## 🏗️ Project Structure
```bash
room-booking-api/
│── bookings/          # Main API app (models, serializers, views, urls)
│── config/            # Project configuration
│── tests/             # Unit tests
│── .env               # Environment variables
│── requirements.txt   # Dependencies
│── README.md          # Documentation
│── manage.py          # App management
│── requirenments.txt  # Dependencies management
│── .env.example       # .env.example
│── .gitignore         # To Ignore file and folders so that git doesn't track them.
│── LICENSE            # MIT License
```
---
```bash
```
## Git Workflow

This project follows a feature branch workflow to ensure clean and organized code management.

- **`main`**: The production-ready code. Only stable, tested code should be merged here.
- **`dev`**: The development branch where active development and integration occur.
- **`feature/*`**: Feature-specific branches branched off `dev`. Example:
  - `feature/room-booking-api` The model development branch
  - `feature/add-room-booking-view`The views development branch
  - `feature/add-room-booking-routes`The URL routing development branch
  - `feature/add-room-booking-serializer`The serializer development branch
  - `feature/add-tests The tests development branch
- **`hotfix/*`**: For critical fixes that need to be applied directly to `main`.
``` 
```
### Branching Example:
```bash
git checkout dev
  - `feature/add-room-booking-serializer`
git checkout -b feature/room-booking-api
# After development
git push origin feature/room-booking-api
```

```bash
## 🤝 Contributing
If you'd like to contribute, please **fork the repository** and submit a **pull request**.

---

## 📜 License
This project is licensed under the **MIT License**.


## 🚀 Author
Developed by **Chinemerem** as part of a technical interview task at Bitcube.


**Happy Coding! 🚀**
```
