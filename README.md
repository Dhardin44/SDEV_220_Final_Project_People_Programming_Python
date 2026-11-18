# Workshop Registration System

A Python Workshop Management & Registration System for an arts & crafts retail hub. 

---  Project Definition ---

**What is it?** A modular system to handle craft workshops, scheduled sessions, instructor assignments, and customer registrations.

**What does it do?** Manages session capacity limits, prevents double-booking, tracks attendance rosters, and supports customer class sign-ups.

**Target Audience:** Customers browsing craft classes, instructors managing their class schedules, and store admins overseeing offerings.

----------------------------

 **Project Directory Structure**

SDEV_220_Final_Project_People_Programming_Python/
├── .gitignore
├── .test_run_count
├── conftest.py
├── pytest.ini
├── README.md
├── requirements.txt
├── src
│   └── workshop_app
│       ├── __init__.py
│       ├── main.py                     # App entry
│       ├── models                      # Main entities
│       │   ├── __init__.py
│       │   ├── registration.py         # Bookings and payment states
│       │   ├── session.py              # Time, capacity, availability
│       │   └── workshop.py             # Business logic/validation
│       ├── services
│       │   ├── __init__.py
│       │   ├── booking_service.py      # Filtering, creating, managing 
│       │   ├── instructor_service.py   # Instructor assignments/schedules
│       │   └── workshop_service.py     # Filtering, creating, managing
│       └── ui                          # TKinter GUI
│           ├── __init__.py
│           ├── browse_tab.py           # Tkinter views for US-01/02
│           ├── instructor_tab.py       # Tkinter views for US-05
│           ├── main_window.py          # Root application window
│           └── registration_tab.py     # Tkinter forms for US-03/04
└── tests                               # Automated Pytest
    ├── __init__.py
    ├── test_capacity.py
    └── test_registration.py
