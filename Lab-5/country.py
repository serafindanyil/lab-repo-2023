from enum import Enum


class GovernmentType(Enum):
    """Enumeration for government types."""
    DEMOCRACY = "Democracy"  # The constant is written in upper case
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
        return f"{self.name}, {self.capital}, {self.code}, {self.population}, {self.area}, {self.gdp}, {self.government_type}"


class Land:
    """Class representing a landmass or region."""
    def __init__(self, name, countries=None):
        self.name = name
        self.countries = countries

    def sort_population_density(self):
        """Sort countries by population density."""
        return sorted(self.countries, key=lambda country: country.population / country.area, reverse=True)

    def sort_countries_by_gdp(self):
        """Sort countries by GDP."""
        return sorted(self.countries, key=lambda country: country.gdp, reverse=True)

    def choose_country(self, criteria_func):
        """Choose a country based on a given criteria function."""
        return max(self.countries, key=criteria_func)

    def get_top_population_density(self):
        """Print the top population density for each country."""
        population_density = self.sort_population_density()
        for country in population_density:
            print(f"Population density of {country.name}: {country.population / country.area} people per square kilometer")

    def get_top_gdp_countries(self):
        """Print the top GDP countries."""
        top_gdp_countries = self.sort_countries_by_gdp()
        print(f"Top GDP countries in {self.name}")
        for country in top_gdp_countries:
            print(f"{country.name}: {country.gdp} USD trillion")

    def get_longest_name(self):
        """Find and print the country with the longest name."""
        get_longest_name = self.choose_country(lambda country: len(country.name))
        print(f"Country in Europe with the longest name: {get_longest_name.name}")
