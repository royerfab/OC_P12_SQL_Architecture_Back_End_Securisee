from .errorview import InputCheckView


class EventView:
    def __init__(self):
        self.input = InputCheckView()

    def get_event_data(self):
        contract_id = self.input.check_int("Entrer l'id du contrat associé à l'événement : ")
        name = self.input.check_string("Entrer le nom de l'événement : ")
        client_name = self.input.check_string("Entrer le nom du client : ")
        client_contact = self.input.check_string("Entrer le contact du client : ")
        start_date = self.input.check_date("Entrer la date de début de l'événement : ")
        support_contact = self.input.check_string("Entrer le contact du support : ")
        location = self.input.check_string("Entrer l'emplacement de l'événement : ")
        attendees = self.input.check_int("Entrer le nombre de participants : ")
        notes = self.input.check_string("Entrer des notes sur l'événement : ")
        return contract_id, name, client_name, client_contact, start_date, support_contact, location, attendees, notes
    
    def display_events(self, events):
        for event in events:
            print("Event ID:", event.id)
            print("Contract ID:", event.contract_id)
            print("Name:", event.name)
            print("Client Name:", event.client_name)
            print("Client Contact:", event.client_contact)
            print("Start Date:", event.start_date)
            print("Support Contact:", event.support_contact)
            print("Location:", event.location)
            print("Attendees:", event.attendees)
            print("Notes:", event.notes)
            print("---------------------------------------")
    
    def get_event_id(self, event_id_list):
        choice = self.input.input_in_array_of_int("Entrer l'id de l'événement concerné : ", event_id_list)
        return choice
    
    def get_event_support_id(self, support_id_list):
        choice = self.input.input_in_array_of_int("Entrer l'id du contact support : ", support_id_list)
        return choice   
    
    def update_event(self, event):
        print("Taper Entrée pour conserver la valeur sans modification")
        name = self.input.check_string(f"Name ({event.name}) : ", updated=True) or event.name
        start_date = self.input.check_date(f"Start Date ({event.start_date}) : ", updated=True) or event.start_date
        location = self.input.check_string(f"Location ({event.location}) : ", updated=True) or event.location
        attendees = self.input.check_int(f"Attendees ({event.attendees}) : ", updated=True) or event.attendees
        notes = self.input.check_string(f"Notes ({event.notes}) : ", updated=True) or event.notes
        return name, start_date, location, attendees, notes