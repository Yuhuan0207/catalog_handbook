from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Category, Base, CatalogItem

engine = create_engine('sqlite:///catalog.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

# Item for Snowboarding
category1 = Category(name="Snowboarding")
session.add(category1)
session.commit()

catalogItem1 = CatalogItem(name="Boots", description="Snowboard boots are designed to conform to your feet specifically", 
    category=category1)
session.add(catalogItem1)
session.commit()

catalogItem2 = CatalogItem(name="Snowboard Socks", description="Snowboard socks are essential because cold feet will quickly ruin your day.", 
    category=category1)
session.add(catalogItem2)
session.commit()

catalogItem3 = CatalogItem(name="Snowboard Helmet", description="Your brain is the most important organ in your body, so wearing a helmet should be an easy decision.", 
    category=category1)
session.add(catalogItem3)
session.commit()

catalogItem4 = CatalogItem(name="Snowboard Goggles", description="Snowboard goggles help battle glare and protect your eyes from the snow and wind while riding.", 
    category=category1)
session.add(catalogItem4)
session.commit()


# Item for Basketball
category2 = Category(name="Basketball")
session.add(category2)
session.commit()

catalogItem5 = CatalogItem(name="Basketball", description="The ball specifically designed for the basketball game.", 
    category=category2)
session.add(catalogItem5)
session.commit()

catalogItem6 = CatalogItem(name="Basketball Socks", description="The socks specifically designed for the basketball game. Keep your feet warm and ankle protected.", 
    category=category2)
session.add(catalogItem6)
session.commit()

catalogItem7 = CatalogItem(name="Basketball Hoop", description="Basketball hoop that player shoot the basketball in to score in the game.", 
    category=category2)
session.add(catalogItem7)
session.commit()

catalogItem8 = CatalogItem(name="Basketball Shorts", description="Shorts designed specifically for the basketball game which is flexible.", 
    category=category2)
session.add(catalogItem8)
session.commit()

# Item for Running
category3 = Category(name="Running")
session.add(category3)
session.commit()

catalogItem1 = CatalogItem(name="Running Tights", description="Running tights provides extra compression to leg muscle and improve performance", 
    category=category3)
session.add(catalogItem1)
session.commit()

catalogItem2 = CatalogItem(name="Running Jacket", description="Running jacket keeps the runner warm during the exercise but still provide comfort.", 
    category=category3)
session.add(catalogItem2)
session.commit()

catalogItem3 = CatalogItem(name="Running Shoes", description="Running shoes provides extra cushion to protect the runners' knees.", 
    category=category3)
session.add(catalogItem3)
session.commit()

catalogItem4 = CatalogItem(name="Sports Bra", description="Sports bra provides support to women's breast to ensure the overall health condition.", 
    category=category3)
session.add(catalogItem4)
session.commit()

print("Populated the catalog!")