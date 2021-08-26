from .base import *

# Get variables from .env
import dotenv

dotenv.read_dotenv(dotenv=os.path.join(BASE_DIR, "../../.env"), override=True)

# TODO: add .env file to repo and readme

PG_METRICS = True

DATABASES = {
    # default values correspond with execution of start_pg.sh
    # create .env file to change values
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": os.getenv("DB_NAME", 'nplus1-pg'),
        "USER": os.getenv("DB_USER", 'nplus1-pg'),
        "PASSWORD": os.getenv("DB_PASSWORD", 'nplus1-pg'),
        "HOST": os.getenv("DB_HOST", '172.17.0.2'),
        "PORT": os.getenv("DB_PORT", '5432'),
    },
}

INSTALLED_APPS = ['postgres_metrics.apps.PostgresMetrics'] + INSTALLED_APPS
