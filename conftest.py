import pytest
from selenium import webdriver


@pytest.fixture
def dr():
    dr = webdriver.Firefox()
    dr.get("http://mobizon.ua/")
    yield dr
    dr.close()

@pytest.fixture
def wd():
    wd = webdriver.Firefox()
    wd.get("http://mobizon.ua/")
    yield wd
    wd.close()

