from models.config import session
from models.models import Event, User, Contract
from views.events import EventView
from utils.decorators import login_required, manager_required, sales_required, support_required, sales_or_manager_required
from .authentication import AuthenticationController
from datetime import datetime


class EventController:
    def __init__(self):
        self.event_view = EventView()
        self.auth_controller = AuthenticationController()

    @login_required
    @sales_required
    def create_event(self):
        current_user = self.auth_controller.get_current_user()
        (
            contract_id,
            name,
            event_date_start,
            event_date_end,
            location,
            attendees,
            notes,
        ) = self.event_view.get_event_data()
        event_date_start = datetime.strptime(event_date_start, "%Y-%m-%d")
        event_date_end = datetime.strptime(event_date_end, "%Y-%m-%d")
        contract = session.query(Contract).filter_by(id=contract_id).first()
        if contract.status and contract.client.sales_contact_id == current_user.id:
            new_event = Event(
                contract_id=contract_id,
                name=name,
                event_date_start=event_date_start,
                event_date_end=event_date_end,
                location=location,
                attendees=attendees,
                notes=notes,
            )
            session.add(new_event)
            session.commit()
        else:
            print("Le contrat sélectionné n'est pas signé ou ce n'est pas votre client")

    @login_required
    def display_events(self):
        events = session.query(Event).all()
        self.event_view.display_events(events)

    #Affiche les événements d'un support.
    @login_required
    @support_required
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
            return events
        else:
            return None
        
    @login_required
    def display_events_by_support(self):
        current_user = self.auth_controller.get_current_user()
        events = session.query(Event).filter_by(support_id = current_user.id)
        if events.count() >0:   
            self.event_view.display_events(events)
            return events
        else:
            return None

    #Je prends les événements avec display_event_no_support, je récupère les événements, je choisi le support en récupérant les user avec query,
    # je modifie les events avec event.support_id pour assigner le support à l'event
    @login_required
    @manager_required
    def update_event_contact_support(self):
        events = self.display_events_no_support()
        if events:
            event_id_list = [event.id for event in events]
            event_id = self.event_view.get_event_id(event_id_list)
            contacts_support = session.query(User).filter_by(role='support')
            support_id_list = [contact_support.id for contact_support in contacts_support]
            support_id = self.event_view.get_event_support_id(support_id_list)
            event = session.query(Event).filter_by(id=event_id).first()
            event.support_id = support_id
            session.commit()
        else:
            print("Aucun événement existant sans support")

    @login_required
    @support_required
    def update_event(self):
        events = self.display_my_events()
        if events:
            event_id_list = [event.id for event in events]
            event_id = self.event_view.get_event_id(event_id_list)
            event = session.query(Event).filter_by(id=event_id).first()
            (
                name,
                event_date_start,
                event_date_end,
                location,
                attendees,
                notes,
            ) = self.event_view.update_event(event)

            if event_date_start:
                event_date_start = datetime.strptime(event_date_start, "%Y-%m-%d")
                event.event_date_start = event_date_start

            if event_date_end:
                event_date_end = datetime.strptime(event_date_end, "%Y-%m-%d")
                event.event_date_end = event_date_end
            
            event.name = name
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