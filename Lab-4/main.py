from dishwasher import Dishwasher


def main():
    Dish1 = Dishwasher(2000, 10, 'Samsung', 40)
    Dish2 = Dishwasher(10000, 5, 'LG', 60)
    Dish3 = Dishwasher(12000, 24, 'Toshiba', 15)

    print(Dish1)
    print(Dish2)
    print(Dish3)


if __name__ == "__main__":
    main()
