import pytest

from app.modules.auth.models import User
from app.modules.conftest import login, logout
from app import db


@pytest.fixture(scope='module')
def test_client(test_client):
    """
    Extends the test_client fixture to add additional specific data for module testing.
    """
    with test_client.application.app_context():
        user_test = User(email="user@example.com", password="test1234")
        db.session.add(user_test)
        db.session.commit()

    yield test_client


def test_show_empty_notepads(test_client):
    """
    Tests access to the empty notepad list page via GET request.
    """
    login_response = login(test_client, "user@example.com", "test1234")
    assert login_response.status_code == 200, "Login was unsuccessful."
    
    response = test_client.get("/notepad")
    assert response.status_code == 200, "Failed to retrieve notepad page."
    assert b'You have no notepads.' in response.data, "Notepad list page content is incorrect."
    
    logout(test_client)
    
def test_get_create_form_notepad(test_client):
    """
    Tests the creation of a new notepad via POST request.
    """
    login_response = login(test_client, "user@example.com", "test1234")
    assert login_response.status_code == 200, "Login was unsuccessful."
    
    response = test_client.get("/notepad/create")
    assert response.status_code == 200, "Failed to retrieve notepad creation form."
    assert b'Title' in response.data, "Notepad creation form content is incorrect."
    assert b'Body' in response.data, "Notepad creation form content is incorrect."
    
    logout(test_client)
    
def test_post_create_notepad(test_client):
    """
    Tests the creation of a new notepad via POST request.
    """
    login_response = login(test_client, "user@example.com", "test1234")
    assert login_response.status_code == 200, "Login was unsuccessful."
    
    response = test_client.post("/notepad/create", data={
        'title': 'Test Notepad',
        'body': 'This is a test notepad body.'
    }, follow_redirects=True)
    assert response.status_code == 200, "Failed to create notepad."
    assert b'Test Notepad' in response.data, "Notepad is not showing on the notepad list page."
    assert b'This is a test notepad body.' in response.data, "Notepad is not showing on the notepad list page."
    
    logout(test_client)