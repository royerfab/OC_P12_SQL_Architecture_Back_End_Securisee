from models.config import session
from models.models import Event
from views.events import EventView
from utils.decorators import login_required, manager_required, sales_required, support_required


class EventController:
    def __init__(self):
        self.event_view = EventView()

    @login_required
    @sales_required
    def create_event(self):
        (
            contract_id,
            name,
            client_name,
            client_contact,
            start_date,
            support_contact,
            location,
            attendees,
            notes,
        ) = self.event_view.get_event_data()
        new_event = Event(
            contract_id=contract_id,
            name=name,
            client_name=client_name,
            client_contact=client_contact,
            start_date=start_date,
            support_contact=support_contact,
            location=location,
            attendees=attendees,
            notes=notes,
        )
        session.add(new_event)
        session.commit()

    @login_required
    def display_events(self):
        events = session.query(Event).all()
        self.event_view.display_events(events)

    @login_required
    @manager_required or @support_required
    def update_event(self):
        self.display_events()
        event_id = self.event_view.get_event_id()
        event = session.query(Event).filter_by(id=event_id).first()
        (
            contract_id,
            name,
            client_name,
            client_contact,
            start_date,
            support_contact,
            location,
            attendees,
            notes,
        ) = self.event_view.update_event(event)
        event.contract_id = contract_id
        event.name = name
        event.client_name = client_name
        event.client_contact = client_contact
        event.start_date = start_date
        event.support_contact = support_contact
        event.location = location
        event.attendees = attendees
        event.notes = notes
        session.commit()

    @login_required
    @manager_required
    def delete_event(self):
        self.display_events()
        event_id = self.event_view.get_event_id()
        event = session.query(Event).filter_by(id = event_id).first()
        session.delete(event)
        session.commit()