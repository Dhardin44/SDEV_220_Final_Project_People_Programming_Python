# Workshop Registration System

A Python Workshop Management & Registration System for an arts & crafts retail hub. 

---  Project Definition ---

**What is it?** A modular system to handle craft workshops, scheduled sessions, instructor assignments, and customer registrations.

**What does it do?** Manages session capacity limits, prevents double-booking, tracks attendance rosters, and supports customer class sign-ups.

**Target Audience:** Customers browsing craft classes, instructors managing their class schedules, and store admins overseeing offerings.

----------------------------

 **Project Directory Structure**


workshop_registration/
├── .gitignore                   # Local files (like .env) that shouldn't go to GitHub
├── README.md                    # This file
├── pytest.ini                   # Test file    
├── conftest.py                  # Test file
├── src/
│   └── workshop_app/
│       ├── __init__.py
│       ├── models/
│       │   ├── __init__.py
│       │   ├── workshop.py      # Craft type, skill level, description
│       │   ├── instructor.py    # Instructor details and expertise
│       │   ├── session.py       # Specific scheduled class instance (date, time, capacity)
│       │   ├── user.py          # Customer info
│       │   └── registration.py  # Links User to Session with status
│       └── services/
│           ├── __init__.py
│           └── registration_service.py # Main booking and capacity logic
└── tests/
    ├── __init__.py
    ├── conftest.py               # Automated test run counter for QA
    ├── test_capacity.py          # Capacity and overbooking constraint tests
    └── test_registration.py      # Registration flow tests
