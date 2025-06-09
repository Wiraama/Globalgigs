from v1.gig_center.kenya.brightermonday import get_gig_brightermonday
from v1.gig_center.kenya.myjobmag import get_gig_myjobmag
from v1.gig_center.kenya.corporatestaffing import get_gig_corporatestaffing
from v1.gig_center.kenya.kenyajobs import get_gig_kenyajobs
from v1.gig_center.kenya.jobwebkenya import get_gig_jobwebkenya
from .to_database import add_gig
import mysql.connector
from v1.models.database import User, Gigs

def add_data():
    brightmonday = get_gig_brightermonday()
    myjobmag = get_gig_myjobmag()
    corporatestaffing = get_gig_corporatestaffing()
    kenyajobs = get_gig_kenyajobs()
    jobwebkenya = get_gig_jobwebkenya()
    
    gigs = [brightmonday, myjobmag, corporatestaffing, kenyajobs, jobwebkenya]
    
    for gig in gigs:
        add_gig(gig)

def ask_database():
    """conn = mysql.connector.connect(
        host="192.168.1.100",
        user="root",
        password="MyStrongPass123!",
        port=3306,
        database="bot"
    )
    gigs = []
    cursor = conn.cursor()

    cursor.execute(f"SELECT * FROM gigs;")
    gigs_data = cursor.fetchall()

    cursor.close()
    conn.close()"""
    gigs_data = Gigs.query.all()
    return gigs_data