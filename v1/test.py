from views.to_database import add_gig, add_user
from extension import Base, engine

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

gig = {
        "title": "mawira test job",
        "about": "am just Testing my bot",
        "link": "wiriama6@gmail.com"
        }

user = {
        "username": "Wiraama",
        "email": "nicholasmawira6@gmail.com",
        "password": "MAwira01"
        }

add_gig(gig)
add_user(user)
