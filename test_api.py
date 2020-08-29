import pytest
from app import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_roll_the_dice_enpoint(client):
    sides = 20
    response = client.get(f'/{sides}').get_json()
    assert response.get('roll') > 0 and response.get('roll') <= sides
