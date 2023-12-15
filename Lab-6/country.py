"""
This is main script.
"""
from enum import Enum


class GovernmentType(Enum):
    """Enumeration for government types."""
    DEMOCRACY = "Democracy"
    REPUBLIC = "Republic"
    AUTOCRACY = "Autocracy"


class Country:
    """Class representing a country."""
    def __init__(self, name, capital, code, population, area, gdp, government_type):
        """Initialize country attributes."""
        self.name = name
        self.capital = capital
        self.code = code
        self.population = population
        self.area = area
        self.gdp = gdp
        self.government_type = government_type

    def __repr__(self):
        """String representation of the country."""
        return (f"{self.name},"
                f" {self.capital},"
                f" {self.code},"
                f" {self.population},"
                f" {self.area},"
                f" {self.gdp},"
                f" {self.government_type}"
        )


class Land:
    """Class representing a landmass or region."""
    def __init__(self, name, countries=None):
        """Initialize land attributes."""
        self.name = name
        self.countries = countries

    def sort_population_density(self):
        """Sort countries by population density."""
        return sorted(self.countries,
                      key=lambda country: country.population / country.area,
                      reverse=True
                      )

    def sort_countries_by_gdp(self):
        """Sort countries by GDP."""
        return sorted(self.countries, key=lambda country: country.gdp, reverse=True)

    def choose_country(self, criteria_func):
        """Choose a country based on a given criteria function."""
        return max(self.countries, key=criteria_func)

    def get_top_population_density(self):  # Витягнути stdout і перевірити
        """Print the top population density for each country."""
        population_density = self.sort_population_density()
        for country in population_density:
            density = country.population / country.area
            print(f"Population density of {country.name}: {density} people per square kilometer")

    def get_top_gdp_countries(self):  # Витягнути stdout і перевірити
        """Print the top GDP countries."""
        top_gdp_countries = self.sort_countries_by_gdp()
        print(f"Top GDP countries in {self.name}")
        for country in top_gdp_countries:
            print(f"{country.name}: {country.gdp} USD trillion")

    def get_longest_name(self):  # Ретурн стрічки + тест
        """Find and print the country with the longest name."""
        longest_name_country = self.choose_country(lambda country: len(country.name))
        print(f"Country in {self.name} with the longest name: {longest_name_country.name}")
