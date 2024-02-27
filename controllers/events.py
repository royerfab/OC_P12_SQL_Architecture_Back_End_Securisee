from models.config import session
from models.models import Event, User
from views.events import EventView
from utils.decorators import login_required, manager_required, sales_required, support_required, sales_or_manager_required
from .authentication import AuthenticationController


class EventController:
    def __init__(self):
        self.event_view = EventView()
        self.auth_controller = AuthenticationController()

    @login_required
    @sales_required
    def create_event(self):
        (
            client_id,
            contract_id,
            support_id,
            name,
            client_name,
            client_contact,
            event_date_start,
            event_date_end,
            support_contact,
            location,
            attendees,
            notes,
        ) = self.event_view.get_event_data()
        new_event = Event(
            client_id=client_id,
            contract_id=contract_id,
            support_id=support_id,
            name=name,
            client_name=client_name,
            client_contact=client_contact,
            event_date_start=event_date_start,
            event_date_end=event_date_end,
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

    #Affiche les événements d'un support.
    @login_required
    @sales_required
    def display_my_events(self):
        current_user = self.auth_controller.get_current_user()
        events = session.query(Event).filter_by(support_id=current_user.id)
        if events.count() >0:
            self.event_view.display_events(events)
            return events
        else:
            return None

    @login_required
    def display_events_no_support(self):
        events = session.query(Event).filter_by(support_id = None)
        if events.count() >0:   
            self.event_view.display_events(events)
            return True
        else:
            return False
        
    @login_required
    def display_events_by_support(self):
        current_user = self.auth_controller.get_current_user()
        events = session.query(Event).filter_by(support_id = current_user.id)
        if events.count() >0:   
            self.event_view.display_events(events)
            return events
        else:
            return None

    #Je prends les événements avec display_event_no_support et je récupère les user avec query
    def update_event_contact_support(self):
        events = self.display_events_no_support()
        if events:
            event_id = self.event_view.get_event_id()
            contacts_support = session.query(User).filter_by(role='support')
            support_id_list = [contact_support.id for contact_support in contacts_support]
            support_id = self.event_view.get_event_support_id(support_id_list)
            print(support_id, event_id)
        else:
            print("Aucun événement existant sans support")

    @login_required
    @sales_or_manager_required
    def update_event(self):
        events = self.display_events()
        if events:
            event_id_list = [event.id for event in events]
            event_id = self.event_view.get_event_id(event_id_list)
            event = session.query(Event).filter_by(id=event_id).first()
            (
                contract_id,
                name,
                client_name,
                client_contact,
                event_date_end,
                support_contact,
                location,
                attendees,
                notes,
            ) = self.event_view.update_event(event)
            event.contract_id = contract_id
            event.name = name
            event.client_name = client_name
            event.client_contact = client_contact
            event.event_date_end = event_date_end,
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