from demo import create_app
from demo.blueprint.search import db

app = create_app()

with app.app_context():
    db.create_all()



