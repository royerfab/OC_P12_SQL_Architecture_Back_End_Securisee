from .errorview import InputCheckView
from rich.console import Console
from rich.table import Table


class EventView:
    def __init__(self):
        self.input = InputCheckView()

    def get_event_data(self):
        contract_id = self.input.check_int("Entrer l'id du contrat associé à l'événement : ")
        name = self.input.check_string("Entrer le nom de l'événement : ")
        event_date_start = self.input.check_date("Entrer la date de début de l'événement : ")
        event_date_end = self.input.check_date("Entrer la date de fin de l'événement : ")
        location = self.input.check_string("Entrer l'emplacement de l'événement : ")
        attendees = self.input.check_int("Entrer le nombre de participants : ")
        notes = self.input.check_string("Entrer des notes sur l'événement : ")
        return contract_id, name, event_date_start, event_date_end, location, attendees, notes

    def display_events(self, events):
        table = Table(title = "Liste des événements")
        table.add_column("Event id")
        table.add_column("Name")
        table.add_column("Contract")
        table.add_column("Support")
        table.add_column("Event date start")
        table.add_column("Event date end")
        table.add_column("Location")
        table.add_column("Attendees")
        table.add_column("Notes")
      
        for event in events:
            table.add_row(str(event.id), str(event.name), str(event.contract), str(event.support),
                          str(event.event_date_start), str(event.event_date_end), str(event.location), str(event.attendees), str(event.notes))

        console = Console()
        console.print(table)
    
    def get_event_id(self, event_id_list):
        choice = self.input.input_in_array_of_int("Entrer l'id de l'événement concerné : ", event_id_list)
        return choice
    
    def get_event_support_id(self, support_id_list):
        choice = self.input.input_in_array_of_int("Entrer l'id du contact support : ", support_id_list)
        return choice   
    
    def update_event(self, event):
        print("Taper Entrée pour conserver la valeur sans modification")
        name = self.input.check_string(f"Name ({event.name}) : ", updated=True) or event.name
        event_date_start = self.input.check_date(f"Start Date ({event.event_date_start}) : ", updated=True)
        event_date_end = self.input.check_date(f"End Date ({event.event_date_end}) : ", updated=True)
        location = self.input.check_string(f"Location ({event.location}) : ", updated=True) or event.location
        attendees = self.input.check_int(f"Attendees ({event.attendees}) : ", updated=True) or event.attendees
        notes = self.input.check_string(f"Notes ({event.notes}) : ", updated=True) or event.notes
        return name, event_date_start, event_date_end, location, attendees, notes