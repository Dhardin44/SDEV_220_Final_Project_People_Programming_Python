from datetime import datetime, timedelta
from workshop_app.models.workshop import Workshop
from workshop_app.services.workshop_service import (
    save_workshops, load_workshops, edit_workshop,
    validate_workshop, validate_date
)

def test_save_and_load(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)

    workshops = [
        Workshop(1, "Pottery", "Ceramics", 45.00, "Make a bowl")
    ]

    save_workshops(workshops)
    loaded = load_workshops()

    assert len(loaded) == 1
    assert loaded[0].title == "Pottery"
    assert loaded[0].price == 45.00

def test_edit_workshop(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)

    workshops = [
        Workshop(1, "Pottery", "Ceramics", 45.00, "Make a bowl")
    ]

    assert edit_workshop(
        workshops, 1, "Painting", "Art", 35.00, "Paint a canvas"
    )

    loaded = load_workshops()
    assert loaded[0].title == "Painting"
    assert loaded[0].price == 35.00

def test_validate_workshop():
    assert validate_workshop("Pottery", "Ceramics", 45, "Make a bowl")
    assert not validate_workshop("", "Ceramics", 45, "Make a bowl")
    assert not validate_workshop("Pottery", "Ceramics", -10, "Make a bowl")

def test_validate_date():
    assert validate_date(datetime.now() + timedelta(days=1))
    assert not validate_date(datetime.now() - timedelta(days=1))
    assert not validate_date("invalid date")