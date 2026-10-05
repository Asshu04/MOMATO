from database import engine, Base
from model import Restaurant, User, Food, Cart, CartItem


Base.metadata.create_all(bind=engine)

print("MOMATO tables created successfully!")