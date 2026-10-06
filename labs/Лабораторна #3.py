catalog = {
    1: {"name": "Локшина Buldak Cheese", "price": 125.50, "stock": 20},
    2: {"name": "Шаурма (без моркви і помідорів)", "price": 140.00, "stock": 15},
    3: {"name": "Енергетик Non Stop", "price": 45.00, "stock": 50},
    4: {"name": "Мишка для osu! (1200 DPI)", "price": 1250.75, "stock": 5}
}

cart = []

format_price = lambda price: f"{price:.2f} грн"
calc_total = lambda current_cart: sum(catalog[item_id]["price"] for item_id in current_cart)


def show_catalog():
    print("\n--- Каталог товарів ---")
    for item_id, info in catalog.items():
        print(f"[{item_id}] {info['name']} - {format_price(info['price'])}")


def add_to_cart():
    show_catalog()
    try:
        item_id = int(input("\nВведи ID товару, щоб додати в кошик: "))
        if item_id in catalog:
            # Перевіряємо, чи є ще товар на складі
            in_cart = cart.count(item_id)
            if in_cart < catalog[item_id]["stock"]:
                cart.append(item_id)
                print(f"+ '{catalog[item_id]['name']}' додано в кошик.")
            else:
                print("- Соррі, на складі більше нема, ти вигріб все.")
        else:
            print("- Нема такого ID, очі роззуй.")
    except ValueError:
        print("- Вводь цифру, геній.")


def remove_from_cart():
    if not cart:
        print("- Кошик пустий, що ти зібрався видаляти?")
        return

    print("\n--- Твій кошик ---")
    for item_id in set(cart):
        count = cart.count(item_id)
        print(f"[{item_id}] {catalog[item_id]['name']} (x{count})")

    try:
        item_id = int(input("\nВведи ID товару для видалення: "))
        if item_id in cart:
            cart.remove(item_id)
            print(f"- Одну штуку '{catalog[item_id]['name']}' видалено з кошика.")
        else:
            print("- Такого товару нема в кошику.")
    except ValueError:
        print("- Адекватно вводь ID.")


def checkout():
    if not cart:
        print("- Кошик пустий, йди щось вибери спочатку.")
        return

    total = calc_total(cart)
    print(f"\nДо сплати: {format_price(total)}")
    confirm = input("Купуємо? (1 - так, 0 - ні): ")

    if confirm == '1':
        # Списуємо залишки
        for item_id in cart:
            catalog[item_id]["stock"] -= 1
        cart.clear()
        print("Успішно куплено! (гроші списані, насправді ні).")
    else:
        print("Покупку скасовано.")


def admin_panel():
    pwd = input("Пароль адміна (підказка: admin): ")
    if pwd == "admin":
        print("\n=== Залишки на складі ===")
        for item_id, info in catalog.items():
            print(f"[{item_id}] {info['name']}: {info['stock']} шт.")
    else:
        print("- Неправильний пароль. Йди гуляй.")


def main():
    while True:
        print("\n=== Міні-Магазин ===")
        print("1. Переглянути каталог")
        print("2. Додати в кошик")
        print("3. Видалити з кошика")
        print("4. Оформити замовлення")
        print("5. Адмін-панель (залишки)")
        print("0. Вихід")

        choice = input("Обирай дію: ")

        if choice == '1':
            show_catalog()
        elif choice == '2':
            add_to_cart()
        elif choice == '3':
            remove_from_cart()
        elif choice == '4':
            checkout()
        elif choice == '5':
            admin_panel()
        elif choice == '0':
            print("Пака здоровяк!")
            break
        else:
            print("- Нормально цифру введи, від 0 до 5.")


if __name__ == "__main__":
    main()



