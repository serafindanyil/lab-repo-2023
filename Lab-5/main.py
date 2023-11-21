from country import Land, Country, GovernmentType


def main():
    Ukraine = Country("Ukraine", "Kyiv", "UA", 45000000, 603500, 1311.29, GovernmentType.DEMOCRACY)
    Poland = Country("Poland", "Warsaw", "PL", 38000000, 312696, 614.86, GovernmentType.REPUBLIC)
    France = Country("France", "Paris", "FR", 68000000, 551695, 2958, GovernmentType.REPUBLIC)


    Europe = Land("Europe", [Ukraine, Poland, France])
    Europe.get_top_population_density()
    Europe.get_top_gdp_countries()
    Europe.get_longest_name()


if __name__ == "__main__":
    main()






