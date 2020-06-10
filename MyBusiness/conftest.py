import pytest
from application import Application


@pytest.fixture(scope="session")
def app(request):
    fixture = Application()

    def quit_driver():
        fixture.close()

    request.addfinalizer(quit_driver)