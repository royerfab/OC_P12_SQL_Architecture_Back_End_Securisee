from models.models import meta_base
from models.config import engine
from controllers.main import MainController

# checkfirst ici pour pouvoir modifier les champs du modèle et que ce soit pris en compte
meta_base.create_all(engine, checkfirst = True)
MainController().start()