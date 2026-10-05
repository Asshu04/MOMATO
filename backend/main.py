from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from sqlalchemy import delete, insert, update, select, func

from database import engine
from model import Restaurant, User, Food, Cart, CartItem

from schemas import (
    RestaurantCreate,
    RestaurantUpdate,
    UserCreate,
    UserLogin,
    FoodCreate,
    FoodUpdate,
    CartItemCreate,
    CartItemUpdate
)

from security import (
    hash_password,
    verify_password
)

from auth import (
    create_access_token,
    verify_access_token
)


app = FastAPI(
    title="MOMATO API"
)


# --------------------------------
# JWT CONFIGURATION
# --------------------------------

security = HTTPBearer()


def get_current_user_email(
    credentials: HTTPAuthorizationCredentials = Depends(security)
):

    token = credentials.credentials

    email = verify_access_token(token)

    if email is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid or expired token",
            headers={"WWW-Authenticate": "Bearer"}
        )

    return email

# --------------------------------
# HOME
# --------------------------------

@app.get("/")
def home():

    return {
        "message": "MOMATO API is running successfully!"
    }


# --------------------------------
# CREATE RESTAURANT
# POST /restaurants
# --------------------------------

@app.post("/restaurants")
def create_restaurants(
    restaurant: RestaurantCreate
):

    with engine.begin() as connection:

        connection.execute(
            insert(Restaurant).values(
                name=restaurant.name,
                location=restaurant.location,
                phone=restaurant.phone
            )
        )

    return {
        "message": "Restaurant created successfully",
        "name": restaurant.name,
        "location": restaurant.location,
        "phone": restaurant.phone
    }


# --------------------------------
# GET ALL RESTAURANTS
# GET /restaurants
# --------------------------------

@app.get("/restaurants")
def get_restaurants():

    with engine.connect() as connection:

        result = connection.execute(
            Restaurant.__table__.select()
        )

        restaurants = []

        for row in result:

            restaurants.append({
                "id": row.id,
                "name": row.name,
                "location": row.location,
                "phone": row.phone
            })

    return restaurants


# --------------------------------
# GET RESTAURANT BY ID
# GET /restaurants/{restaurant_id}
# --------------------------------

@app.get("/restaurants/{restaurant_id}")
def get_restaurant(
    restaurant_id: int
):

    with engine.connect() as connection:

        result = connection.execute(
            Restaurant.__table__.select().where(
                Restaurant.id == restaurant_id
            )
        )

        row = result.fetchone()

    if row is None:

        raise HTTPException(
            status_code=404,
            detail="Restaurant not found"
        )

    return {
        "id": row.id,
        "name": row.name,
        "location": row.location,
        "phone": row.phone
    }


# --------------------------------
# UPDATE RESTAURANT
# PUT /restaurants/{restaurant_id}
# --------------------------------

@app.put("/restaurants/{restaurant_id}")
def update_restaurant(
    restaurant_id: int,
    restaurant: RestaurantUpdate
):

    with engine.begin() as connection:

        result = connection.execute(
            update(Restaurant)
            .where(
                Restaurant.id == restaurant_id
            )
            .values(
                name=restaurant.name,
                location=restaurant.location,
                phone=restaurant.phone
            )
        )

        if result.rowcount == 0:

            raise HTTPException(
                status_code=404,
                detail="Restaurant not found"
            )

    return {
        "message": "Restaurant updated successfully",
        "id": restaurant_id,
        "name": restaurant.name,
        "location": restaurant.location,
        "phone": restaurant.phone
    }


# --------------------------------
# DELETE RESTAURANT
# DELETE /restaurants/{restaurant_id}
# --------------------------------

@app.delete("/restaurants/{restaurant_id}")
def delete_restaurant(
    restaurant_id: int
):

    with engine.begin() as connection:

        result = connection.execute(
            delete(Restaurant)
            .where(
                Restaurant.id == restaurant_id
            )
        )

        if result.rowcount == 0:

            raise HTTPException(
                status_code=404,
                detail="Restaurant not found"
            )

    return {
        "message": "Restaurant deleted successfully",
        "id": restaurant_id
    }

# --------------------------------
# CREATE FOOD
# POST /foods
# --------------------------------

@app.post("/foods")
def create_food(
    food: FoodCreate
):

    with engine.begin() as connection:

        # Check whether restaurant exists

        restaurant = connection.execute(
            select(Restaurant).where(
                Restaurant.id == food.restaurant_id
            )
        ).first()

        if restaurant is None:

            raise HTTPException(
                status_code=404,
                detail="Restaurant not found"
            )

        # Create food

        connection.execute(
            insert(Food).values(
                name=food.name,
                description=food.description,
                price=food.price,
                restaurant_id=food.restaurant_id
            )
        )

    return {
        "message": "Food created successfully",
        "name": food.name,
        "description": food.description,
        "price": food.price,
        "restaurant_id": food.restaurant_id
    }
# --------------------------------
# GET ALL FOODS
# GET /foods
# --------------------------------

@app.get("/foods")
def get_foods():

    with engine.connect() as connection:

        result = connection.execute(
            Food.__table__.select()
        )

        foods = []

        for row in result:

            foods.append({
                "id": row.id,
                "name": row.name,
                "description": row.description,
                "price": row.price,
                "restaurant_id": row.restaurant_id
            })

    return foods

# --------------------------------
# GET FOOD BY ID
# GET /foods/{food_id}
# --------------------------------

@app.get("/foods/{food_id}")
def get_food(
    food_id: int
):

    with engine.connect() as connection:

        result = connection.execute(
            Food.__table__.select().where(
                Food.id == food_id
            )
        )

        food = result.fetchone()

    if food is None:

        raise HTTPException(
            status_code=404,
            detail="Food not found"
        )

    return {
        "id": food.id,
        "name": food.name,
        "description": food.description,
        "price": food.price,
        "restaurant_id": food.restaurant_id
    }

# --------------------------------
# UPDATE FOOD
# PUT /foods/{food_id}
# --------------------------------

@app.put("/foods/{food_id}")
def update_food(
    food_id: int,
    food: FoodUpdate
):

    with engine.begin() as connection:

        result = connection.execute(
            update(Food)
            .where(
                Food.id == food_id
            )
            .values(
                name=food.name,
                description=food.description,
                price=food.price
            )
        )

        if result.rowcount == 0:

            raise HTTPException(
                status_code=404,
                detail="Food not found"
            )

    return {
        "message": "Food updated successfully",
        "id": food_id,
        "name": food.name,
        "description": food.description,
        "price": food.price
    }
# --------------------------------
# DELETE FOOD
# DELETE /foods/{food_id}
# --------------------------------

@app.delete("/foods/{food_id}")
def delete_food(
    food_id: int
):

    with engine.begin() as connection:

        result = connection.execute(
            delete(Food)
            .where(
                Food.id == food_id
            )
        )

        if result.rowcount == 0:

            raise HTTPException(
                status_code=404,
                detail="Food not found"
            )

    return {
        "message": "Food deleted successfully",
        "id": food_id
    }
# --------------------------------
# USER REGISTRATION
# POST /users/register
# --------------------------------

@app.post("/users/register")
def register_user(
    user: UserCreate
):

    try:

        hashed_password = hash_password(
            user.password
        )

    except ValueError as exc:

        raise HTTPException(
            status_code=422,
            detail=str(exc)
        ) from exc

    with engine.begin() as connection:

        # Check email

        existing_email = connection.execute(
            select(User).where(
                User.email == user.email
            )
        ).first()

        if existing_email:

            raise HTTPException(
                status_code=400,
                detail="Email already registered"
            )

        # Check phone

        existing_phone = connection.execute(
            select(User).where(
                User.phone == user.phone
            )
        ).first()

        if existing_phone:

            raise HTTPException(
                status_code=400,
                detail="Phone number already registered"
            )

        # Insert user

        connection.execute(
            insert(User).values(
                name=user.name,
                email=user.email,
                phone=user.phone,
                password=hashed_password
            )
        )

    return {
        "message": "User registered successfully",
        "name": user.name,
        "email": user.email,
        "phone": user.phone
    }


# --------------------------------
# USER LOGIN
# POST /users/login
# --------------------------------

@app.post("/users/login")
def login_user(
    user: UserLogin
):

    with engine.connect() as connection:

        # Find user by email

        result = connection.execute(
            select(User).where(
                User.email == user.email
            )
        )

        existing_user = result.fetchone()

        # User not found

        if existing_user is None:

            raise HTTPException(
                status_code=401,
                detail="Invalid email or password"
            )

        # Verify password

        password_correct = verify_password(
            user.password,
            existing_user.password
        )

        # Password incorrect

        if not password_correct:

            raise HTTPException(
                status_code=401,
                detail="Invalid email or password"
            )

    # Create JWT

    access_token = create_access_token(
        data={
            "sub": existing_user.email
        }
    )

    return {
        "message": "Login successful",
        "access_token": access_token,
        "token_type": "bearer",
        "user_id": existing_user.id,
        "name": existing_user.name,
        "email": existing_user.email
    }


# --------------------------------
# CART MANAGEMENT
# --------------------------------

@app.get("/cart")
def get_cart(
    current_user_email: str = Depends(get_current_user_email)
):

    with engine.connect() as connection:

        user = connection.execute(
            select(User).where(
                User.email == current_user_email
            )
        ).first()

        if user is None:
            raise HTTPException(
                status_code=404,
                detail="User not found"
            )

        cart = connection.execute(
            select(Cart).where(
                Cart.user_id == user.id
            )
        ).first()

        if cart is None:
            return {
                "cart_id": None,
                "user_id": user.id,
                "items": [],
                "total_amount": 0
            }

        cart_items = connection.execute(
            select(CartItem, Food)
            .join(Food, Food.id == CartItem.food_id)
            .where(CartItem.cart_id == cart.id)
        ).all()

        items = []
        total_amount = 0

        for cart_item, food in cart_items:
            item_total = food.price * cart_item.quantity
            total_amount += item_total
            items.append({
                "id": cart_item.id,
                "food_id": food.id,
                "name": food.name,
                "quantity": cart_item.quantity,
                "price": food.price,
                "subtotal": item_total
            })

    return {
        "cart_id": cart.id,
        "user_id": user.id,
        "items": items,
        "total_amount": total_amount
    }


@app.post("/cart/items")
def add_to_cart(
    item: CartItemCreate,
    current_user_email: str = Depends(get_current_user_email)
):
    with engine.begin() as connection:

        # Find the logged-in user
        user_result = connection.execute(
            select(User).where(
                User.email == current_user_email
            )
        )

        user = user_result.fetchone()

        if user is None:
            raise HTTPException(
                status_code=404,
                detail="User not found"
            )

        # Check whether the food exists
        food_result = connection.execute(
            select(Food).where(
                Food.id == item.food_id
            )
        )

        food = food_result.fetchone()

        if food is None:
            raise HTTPException(
                status_code=404,
                detail="Food not found"
            )

        # Find user's cart
        cart_result = connection.execute(
            select(Cart).where(
                Cart.user_id == user.id
            )
        )

        cart = cart_result.fetchone()

        # Create cart if user doesn't have one
        if cart is None:
            connection.execute(
                insert(Cart).values(
                    user_id=user.id
                )
            )

            cart = connection.execute(
                select(Cart).where(
                    Cart.user_id == user.id
                )
            ).first()

            if cart is None:
                raise HTTPException(
                    status_code=500,
                    detail="Failed to create cart"
                )

            cart_id = cart.id
        else:
            cart_id = cart.id

        # Check whether food is already in cart
        existing_item = connection.execute(
            select(CartItem).where(
                CartItem.cart_id == cart_id,
                CartItem.food_id == item.food_id
            )
        ).fetchone()

        if existing_item:
            new_quantity = existing_item.quantity + item.quantity

            connection.execute(
                update(CartItem)
                .where(CartItem.id == existing_item.id)
                .values(
                    quantity=new_quantity
                )
            )

            return {
                "message": "Cart item quantity updated",
                "food_id": item.food_id,
                "quantity": new_quantity
            }

        # Add new item
        connection.execute(
            insert(CartItem).values(
                cart_id=cart_id,
                food_id=item.food_id,
                quantity=item.quantity
            )
        )

    return {
        "message": "Food added to cart",
        "food_id": item.food_id,
        "quantity": item.quantity
    }

@app.put("/cart/items/{food_id}")
def update_cart_item(
    food_id: int,
    item: CartItemUpdate,
    current_user_email: str = Depends(get_current_user_email)
):

    with engine.begin() as connection:

        user = connection.execute(
            select(User).where(
                User.email == current_user_email
            )
        ).first()

        if user is None:
            raise HTTPException(
                status_code=404,
                detail="User not found"
            )

        cart = connection.execute(
            select(Cart).where(
                Cart.user_id == user.id
            )
        ).first()

        if cart is None:
            raise HTTPException(
                status_code=404,
                detail="Cart not found"
            )

        cart_item = connection.execute(
            select(CartItem).where(
                CartItem.cart_id == cart.id,
                CartItem.food_id == food_id
            )
        ).first()

        if cart_item is None:
            raise HTTPException(
                status_code=404,
                detail="Cart item not found"
            )

        connection.execute(
            update(CartItem)
            .where(
                CartItem.id == cart_item.id
            )
            .values(
                quantity=item.quantity
            )
        )

    return {
        "message": "Cart item updated successfully",
        "food_id": food_id,
        "quantity": item.quantity
    }


@app.delete("/cart/items/{food_id}")
def delete_cart_item(
    food_id: int,
    current_user_email: str = Depends(get_current_user_email)
):

    with engine.begin() as connection:

        user = connection.execute(
            select(User).where(
                User.email == current_user_email
            )
        ).first()

        if user is None:
            raise HTTPException(
                status_code=404,
                detail="User not found"
            )

        cart = connection.execute(
            select(Cart).where(
                Cart.user_id == user.id
            )
        ).first()

        if cart is None:
            raise HTTPException(
                status_code=404,
                detail="Cart not found"
            )

        result = connection.execute(
            delete(CartItem)
            .where(
                CartItem.cart_id == cart.id,
                CartItem.food_id == food_id
            )
        )

        if result.rowcount == 0:
            raise HTTPException(
                status_code=404,
                detail="Cart item not found"
            )

    return {
        "message": "Cart item removed successfully",
        "food_id": food_id
    }


# --------------------------------
# GET CURRENT USER
# GET /users/me
# --------------------------------

@app.get("/users/me")
def get_current_user(
    current_user_email: str = Depends(get_current_user_email)
):

    with engine.connect() as connection:

        result = connection.execute(
            select(User).where(
                User.email == current_user_email
            )
        )

        user = result.fetchone()

    if user is None:

        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return {
        "id": user.id,
        "name": user.name,
        "email": user.email,
        "phone": user.phone
    }
