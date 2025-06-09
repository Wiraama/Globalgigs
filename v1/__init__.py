from flask import Flask
from v1.routes.main import bot
from v1.views.gig_dist import add_data
#from v1.extension import Base, engine
from datetime import datetime
from v1.models.database import Gigs, db

def create_bot():
    app = Flask(__name__)
    # Store the database file in the current directory
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bot.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    
    with app.app_context():
        db.drop_all()
        db.create_all()
        add_data()

    #Base.metadata.create_all(engine)
    now = datetime.now()
    """if now.hour == 0 and now.minute == 0:
        Gigs.__table__.drop(bind=engine)
        add_data()"""
        
    #Gigs.__table__.drop(db.engine)
    #with app.app_context():
    #    add_data()
    app.register_blueprint(bot)
    
    return app