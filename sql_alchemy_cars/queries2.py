from tables import Brands, Models, Users


def add_test_many_data(session):
    bmw = Brands(name="BMW", country="Germany")
    lada = Brands(name="Lada", country="Russia")
    ferrari = Brands(name="Ferrari", country="Italy")
    dodge = Brands(name="Dodge", country="USA")
    toyota = Brands(name="Toyota", country="Japan")

    m3 = Models(name="M3", year=2005, price=1500000, brand_id=1)
    vesta = Models(name="Vesta", year=2018, price=1800000, brand_id=2)
    f40 = Models(name="F-40", year=1990, price=150000000, brand_id=3)
    viper = Models(name="Viper", year=2010, price=7500000, brand_id=4)
    supra = Models(name="Supra", year=2007, price=3000000, brand_id=5)
    charger = Models(name="Charger", year=2010, price=5000000, brand_id=4)
    enzo = Models(name="Enzo", year=2005, price=30000000, brand_id=3)
    challenger = Models(name="Challenger", year=2012, price=8500000, brand_id=4)

    messi = Users(full_name="Lionel Messi", phone="88005553535")
    ronaldo = Users(full_name="Cristiano Ronaldo", phone="1654613156")
    mbappe = Users(full_name="Killian Mbappe", phone="4567471876")
    neimar = Users(full_name="Neimar", phone="7817856145")
    sigma_boy = Users(full_name="Sigma Boy", phone="1111111111111")

    session.add_all([
        bmw, lada, ferrari, dodge, toyota,
        m3, vesta, f40, viper, supra, charger, enzo, challenger,
        messi, ronaldo, mbappe, neimar, sigma_boy
    ])
    session.commit()
    print("Тестовые данные успешно вставлены.")

def add_brand(session):
    name = input("Производитель: ")
    country = input("Страна: ")
    session.add(Brands(name=name, country=country))
    session.commit()
    print(f"Марка {name} из {country} успешно добавлена")


def add_model(session):
    pass
def add_user(session):
    pass
def show_all_brands(session):
    all_brands = session.query(Brands).all()
    for n, brand in enumerate(all_brands, start=1):
        print(f"{n}: {brand.name}, {brand.country}, id={brand.id}")
    print("\n\n")


def show_all_models(session):
    pass
def show_all_users(session):
    pass
def show_all_users_with_their_cars(session):
    pass
def show_all_models_by_brand(session):
    pass
def show_all_users_by_model(session):
    pass
def delete_model(session):
    pass
def update_model(session):
    pass