"""
This module contains tests for the Country and Land classes.
"""
import pytest
from country import Country, Land, GovernmentType


@pytest.fixture(name="countries_test")
def sample_country():
    """
    Fixture for creating a sample Country instance.
    """
    return Country("TestCountry", "TestCapital", "TC", 1000000, 1000, 1.5, GovernmentType.DEMOCRACY)


@pytest.fixture(name="lands_test")
def sample_land():
    """
    Fixture for creating a sample Land instance with countries.
    """
    country1 = Country("Country1", "Capital1", "C1", 500000, 500, 1.0, GovernmentType.DEMOCRACY)
    country2 = Country("Country2", "Capital2", "C2", 1000000, 1000, 2.0, GovernmentType.REPUBLIC)
    return Land("TestLand", [country1, country2])


def test_country_repr(countries_test):
    """
    Test the string representation of a Country object.
    """
    assert repr(countries_test) == "TestCountry, TestCapital, TC, 1000000, 1000, 1.5, GovernmentType.DEMOCRACY"

# 1 елемени == кантрі2, 2 елемент == кантрі 1
def test_land_sort_population_density(lands_test):
    """
    Test if countries in a Land object are sorted by population density in descending order.
    """
    sorted_countries = lands_test.sort_population_density()
    assert sorted_countries[0].population / sorted_countries[0].area >= sorted_countries[1].population / sorted_countries[1].area


def test_land_sort_countries_by_gdp(lands_test):
    """
    Test if countries in a Land object are sorted by GDP in descending order.
    """
    sorted_countries = lands_test.sort_countries_by_gdp()
    assert sorted_countries[0].name == "Country2"


def test_land_choose_country(lands_test):
    """
    Test if the method to choose a country based on a key function works as expected.
    """
    chosen_country = lands_test.choose_country(lambda country: country.population)
    assert chosen_country.name == "Country2"
