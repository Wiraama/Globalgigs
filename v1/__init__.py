from flask import Flask
from v1.routes.main import bot
from v1.views.gig_dist import add_data
from v1.extension import Base, engine
from datetime import datetime

def create_bot():
    
    app = Flask(__name__)
    
    Base.metadata.create_all(engine)
    now = datetime.now()
    if now.hour == 0 and now.minute == 0:
        Gigs.__table__.drop(bind=engine)
        add_data()
    
    app.register_blueprint(bot)
    
    return app