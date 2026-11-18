---  SDEV 220 Final Project: Arts & Crafts Workshop Registration System ---

**Project Definition**

The Arts & Crafts Workshop Registration System is a modular, desktop, GUI based management application designed for established craft and hobby retailers (such as Michaels or Hobby Lobby). 

**Scope & Boundaries**

*In Scope:*

  **Workshop & Session Management:** Creating and managing workshop templates, scheduling specific calendar sessions, setting capacity limits, and tracking available spaces.

  **Customer Registration & Simulated Payments:** Allowing customers to browse active upcoming workshops, view required materials/supply lists, register, and process simulated payments with automated confirmations.

  **Instructor & Employee Rosters:** Providing instructors and coordinators with access to scheduled workshops and registered participant rosters.

*Out of Scope:*

  **Retail Inventory:** General store inventory, shelf stock tracking, inventory databases and retail e-commerce shopping carts are unnecessary.

**Architecture**

The application follows a basic separation of concerns, separating the main domain logic from the user interface to keep things clean:

* 'src/workshop_app/models/' : Main domain entities ('Workshop', 'Session', 'Registration').

* 'src/workshop_app/services/': Business logic, validation rules, and capacity checks.

* 'src/workshop_app/ui/': Decoupled Tkinter graphical user interface.

* 'tests/': Automated test suite using 'pytest'.


QUICK ANSWERS:

**A Python Workshop Management & Registration System for an Arts & Crafts Store**


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
