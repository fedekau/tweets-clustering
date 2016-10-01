from orator import DatabaseManager, Model
import os

user = os.getlogin()

config = {
    'postgres': {
        'driver': 'postgres',
        'host': 'localhost',
        'database': 'tweets-db_development',
        'user': user,
    }
}

db = DatabaseManager(config)

Model.set_connection_resolver(db)
