from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Restaurant, Base, MenuItem, User

engine = create_engine('sqlite:///restaurantmenu.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

session = DBSession()

# Create user
User1 = User(name="sakr", email="sakr@yahoo.com")
session.add(User1)
session.commit()

# Menu of restaurant1
restaurant1 = Restaurant(user_id=1, name="Urban Burger")

session.add(restaurant1)
session.commit()

menuItem1 = MenuItem(user_id=1, name="French Fries",
                     description="with garlic and parmesan",
                     price="$2.99",
                     restaurant=restaurant1)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(user_id=1,
                     name="Chicken Burger",
                     description="Juicy grilled chicken patty with tomato mayo and lettuce",
                     price="$5.50",
                     restaurant=restaurant1)

session.add(menuItem2)
session.commit()


menuItem3 = MenuItem(name="Pongal",
                     description="South indian porridge"
                     "made with rice and yellow moong lentils.",
                     price="$5.50", restaurant=restaurant1, user_id=1)

session.add(menuItem3)
session.commit()


# Menu for restaurant2
restaurant2 = Restaurant(name="Super Stir Fry")

session.add(restaurant2)
session.commit()


menuItem1 = MenuItem(name="Chicken Stir Fry",
                     description="With your choice of noodles vegetables and sauces",
                     price="$7.99",
                     restaurant=restaurant2)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem( name="Peking Duck",
                     description=" labala",
                      price="$25",
                      restaurant=restaurant2)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(name=" safary",
                     description="lslslsl",
                     price="$25",
                     restaurant=restaurant2)

session.add(menuItem3)
session.commit()


print ("Added menu items!")
