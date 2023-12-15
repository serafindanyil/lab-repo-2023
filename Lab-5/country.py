from enum import Enum


class GovernmentType(Enum):
    DEMOCRACY = "Democracy"
    REPUBLIC = "Republic"
    AUTOCRACY = "Autocracy"


class Country:
    def __init__(self, name, capital, code,  population, area, GDP, government_type):
        self.name = name
        self.capital = capital
        self.code = code
        self.population = population
        self.area = area
        self.GDP = GDP
        self.government_type = government_type

    #def calculate_population_density(self):
    #   return self.population / self.area

    def __repr__(self):
        return f"{self.name}, {self.capital}, {self.code}, {self.population}, {self.area}, {self.GDP}, {self.government_type}"


class Land:
    def __init__(self, name, countries=None):
        self.name = name
        self.countries = countries

    def sort_population_density(self):
        return sorted(self.countries, key=lambda country: country.population / country.area, reverse=True)

    def sort_countries_by_GDP(self):
        return sorted(self.countries, key=lambda country: country.GDP, reverse=True)

    def choose_country(self, criteria_func):
        return max(self.countries, key=criteria_func)

    def get_top_population_density(self):
        population_density = self.sort_population_density()
        for country in population_density:
            print(f"Population density of {country.name}: {country.population / country.area} people per square kilometer")

    def get_top_gdp_countries(self):
        top_gdp_countries = self.sort_countries_by_GDP()
        print(f"Top GDP countries in {self.name}")
        for country in top_gdp_countries:
            print(f"{country.name}: {country.GDP} USD trillion")

    def get_longest_name(self):
        get_longest_name = self.choose_country(lambda country: len(country.name))
        print(f"Country in Europe with the longest name: {get_longest_name.name}")
