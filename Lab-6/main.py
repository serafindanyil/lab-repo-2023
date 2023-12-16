"""
This module provides functionality related to countries and land masses.
"""

from country import Land, Country, GovernmentType

def main():
    """
    The main function that demonstrates the usage of the Country and Land classes.
    """
    ukraine = Country("Ukraine", "Kyiv", "UA", 45000000, 603500, 1311.29, GovernmentType.DEMOCRACY)
    poland = Country("Poland", "Warsaw", "PL", 38000000, 312696, 614.86, GovernmentType.REPUBLIC)
    france = Country("France", "Paris", "FR", 68000000, 551695, 2958, GovernmentType.REPUBLIC)

    europe = Land("Europe", [ukraine, poland, france])
    europe.get_top_population_density()
    europe.get_top_gdp_countries()
    europe.get_longest_name()

if __name__ == "__main__":
    main()
