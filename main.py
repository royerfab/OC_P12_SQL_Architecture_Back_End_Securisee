from models.models import meta_base
from models.config import engine
from controllers.main import MainController
import sentry_sdk


if __name__ == "__main__":
    sentry_sdk.init(
        dsn="https://80c0762539a37202c8ba7ab1f9dafc83@o4506810488258560.ingest.sentry.io/4506810496122880",
        # Set traces_sample_rate to 1.0 to capture 100%
        # of transactions for performance monitoring.
        traces_sample_rate=1.0,
        # Set profiles_sample_rate to 1.0 to profile 100%
        # of sampled transactions.
        # We recommend adjusting this value in production.
        profiles_sample_rate=1.0,
    )
    # checkfirst ici pour pouvoir modifier les champs du modèle et que ce soit pris en compte
    meta_base.create_all(engine, checkfirst=True)
    MainController().start()
