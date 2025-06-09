#from v1.extension import SessionLocal
from v1.models.database import Gigs, User, db
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt()


def add_gig(gigs):
    #opening session
    duplicate = []
    count = 0
    #session = SessionLocal()

    # add items
    """for gig in gigs:
        if gig['link'] not in duplicate:
            new_gig = Gigs(
                title=gig['title'],
                about=gig['about'],
                link=gig['link']
            )
            session.add(new_gig)
            duplicate.append(gig['link'])
            count += 1
    session.commit()
    
    session.close()"""
    
    for gig in gigs:
        if Gigs.query.filter_by(link=gig['link']).first():
            continue
        if gig['link'] in duplicate:
            continue
        new_gig = Gigs(
            title=gig['title'],
            about=gig['about'],
            link=gig['link']
        )
        db.session.add(new_gig)
        duplicate.append(gig['link'])
        count += 1
    db.session.commit()
    print(count)

def add_user(user):
    """session = SessionLocal()

    new_user = User(
        username=user['username'],
        email=user['email'],
        password=bcrypt.generate_password_hash(user['password']).decode('utf-8')
    )

    session.add(new_user)
    session.commit()

    session.close()"""

    new_user = User(
        username=user['username'],
        email=user['email'],
        password=bcrypt.generate_password_hash(user['password']).decode('utf-8')
    )

    db.session.add(new_user)
    db.session.commit()