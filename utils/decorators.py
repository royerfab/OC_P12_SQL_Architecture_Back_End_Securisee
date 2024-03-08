def login_required(func):
    def inner(self):
        current_user = self.auth_controller.get_current_user()
        if current_user:
            return func(self)
        else:
            print("Vous n'êtes pas authentifié")
    return inner


def manager_required(func):
    def inner(self):
        current_user = self.auth_controller.is_manager()
        if current_user:
            return func(self)
        else:
            print("Vous n'êtes pas membre de l'équipe de gestion")
    return inner


def sales_required(func):
    def inner(self):
        current_user = self.auth_controller.is_sales_person()
        print(current_user)
        if current_user:
            return func(self)
        else:
            print("Vous n'êtes pas membre de l'équipe commerciale")
    return inner


def support_required(func):
    def inner(self):
        current_user = self.auth_controller.is_support()
        if current_user:
            return func(self)
        else:
            print("Vous n'êtes pas membre de l'équipe de support")
    return inner


def sales_or_manager_required(func):
    def inner(self):
        current_user = self.auth_controller.is_sales_or_manager()
        if current_user:
            return func(self)
        else:
            print("Vous n'êtes pas membre de l'équipe de gestion ou de l'équipe commerciale")
    return inner
