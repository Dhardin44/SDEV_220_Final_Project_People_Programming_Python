import json
from workshop_app.models.workshop import Workshop
from datetime import datetime

def save_workshops(workshops):
    workshop_data = []

    for workshop in workshops:
        workshop_data.append({
            "workshop_id":workshop.workshop_id,
            "title": workshop.title,
            "category": workshop.category,
            "price": workshop.price,
            "description": workshop.description
        })

    with open("workshops.json", "w") as file:
        json.dump(workshop_data, file, indent=4)

def load_workshops():
    workshops = []

    try:
        with open("workshops.json", "r") as file:
            workshop_data = json.load(file)

        for data in workshop_data:
            workshops.append(Workshop(
                data["workshop_id"],
                data["title"],
                data["category"],
                data["price"],
                data["description"]
            ))

    except FileNotFoundError:
        return []

    return workshops

def validate_workshop(title, category, price, description):
    if not title.strip():
        return False

    if not category.strip():
        return False

    if not description.strip():
        return False

    if price < 0:
        return False

    return True

def edit_workshop(workshops, workshop_id, title, category, price, description):
    try:
        price = float(price)
    except (ValueError, TypeError):
        return False

    if not validate_workshop(title, category, price, description):
        return False

    for workshop in workshops:
        if workshop.workshop_id == workshop_id:
            workshop.title = title
            workshop.category = category
            workshop.price = price
            workshop.description = description

            save_workshops(workshops)
            return True

    return False

def validate_date(start_time):
    if not isinstance(start_time, datetime):
        return False

    if start_time <= datetime.now():
        return False

    return True