"""
Custom exceptions.
"""
from logged import logged
from enum import Enum


class CountriesException(Exception):
    pass


class SortPopulationException(CountriesException):
    pass


class SortCountriesException(CountriesException):
    pass


class ChooseCountryException(CountriesException):
    pass


class GetTopPopulationDensityException(CountriesException):
    pass


class GetTopGdpCountriesException(CountriesException):
    pass


class GetLongestNameException(CountriesException):
    pass


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
        return (
            f"{self.name}, {self.capital}, {self.code}, {self.population},  {self.area}, {self.gdp}, {self.government_type}")


class Land:
    """Class representing a landmass or region."""

    def __init__(self, name, countries=None):
        """Initialize land attributes."""
        self.name = name
        self.countries = countries

    @logged(SortPopulationException, mode="console")
    def sort_population_density(self):
        """Sort countries by population density."""
        try:
            return sorted(self.countries, key=lambda country: country.population / country.area, reverse=True)
        except Exception as e:
            raise SortPopulationException(f"Error sorting population density: {str(e)}")

    @logged(SortCountriesException, mode="file")
    def sort_countries_by_gdp(self):
        """Sort countries by GDP."""
        try:
            return sorted(self.countries, key=lambda country: country.gdp, reverse=True)
        except Exception as e:
            raise SortCountriesException(f"Error sorting countries by GDP: {str(e)}")

    @logged(ChooseCountryException, mode="file")
    def choose_country(self, criteria_func):
        """Choose a country based on a given criteria function."""
        try:
            return max(self.countries, key=criteria_func)
        except Exception as e:
            raise ChooseCountryException(f"Error choosing country: {str(e)}")

    @logged(GetTopPopulationDensityException, mode="file")
    def get_top_population_density(self):
        """Print the top population density for each country."""
        try:
            population_density = self.sort_population_density()
            for country in population_density:
                density = country.population / country.area
                print(f"Population density of {country.name}: {density} people per square kilometer")
        except Exception as e:
            raise GetTopPopulationDensityException(f"Error getting top population density: {str(e)}")

    @logged(GetTopGdpCountriesException, mode="file")
    def get_top_gdp_countries(self):
        """Print the top GDP countries."""
        try:
            top_gdp_countries = self.sort_countries_by_gdp()
            print(f"Top GDP countries in {self.name}")
            for country in top_gdp_countries:
                print(f"{country.name}: {country.gdp} USD trillion")
        except Exception as e:
            raise GetTopGdpCountriesException(f"Error getting top GDP countries: {str(e)}")

    @logged(GetLongestNameException, mode="file")
    def get_longest_name(self):
        """Find and print the country with the longest name."""
        try:
            longest_name_country = self.choose_country(lambda country: len(country.name))
            print(f"Country in {self.name} with the longest name: {longest_name_country.name}")
        except Exception as e:
            raise GetLongestNameException(f"Error getting longest name country: {str(e)}")
