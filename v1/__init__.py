from flask import Flask
from v1.routes.main import bot
from v1.views.gig_dist import add_data
from v1.extension import Base, engine

def create_bot():
    
    app = Flask(__name__)
    
    #Base.metadata.drop_all(engine)
    #Base.metadata.create_all(engine)
    #add_data()
    
    app.register_blueprint(bot)
    
    return app