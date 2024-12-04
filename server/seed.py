from app import app
from models import db, Deli, Hamburger

if __name__ == '__main__':
    with app.app_context():
        print("Seeding database...")

        Deli.query.delete()
        Hamburger.query.delete()

        d1 = Deli(name="Mr Mango", location="Fort Greene", has_bodega_cat=True)
        d2 = Deli(name="Mr Kiwi", location="Bed Stuy", has_bodega_cat=True)
        d3 = Deli(name="Mr Pineapple", location="Park Slope", has_bodega_cat=True)

        db.session.add_all( [d1,d2,d3] )
        db.session.commit()

        print("Seeding complete!")
