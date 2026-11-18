from datetime import datetime
from workshop_app.models.workshop import Workshop

class Session:
    def __init__(self, session_id: int, workshop: Workshop, start_time: datetime, max_capacity: int):
        self.session_id = session_id
        self.workshop = workshop
        self.start_time = start_time
        self.max_capacity = max_capacity
        self.registered_count = 0 # Will be updated by registrations

    @property
    def available_spaces(self) -> int:
        return max(0, self.max_capacity - self.registered_count)

    @property
    def is_fully_booked(self) -> bool:
        return self.available_spaces == 0

    @property
    def is_upcoming(self) -> bool:
        return self.start_time > datetime.now()
