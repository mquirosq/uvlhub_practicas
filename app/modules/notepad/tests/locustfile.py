from locust import HttpUser, TaskSet, task
from core.environment.host import get_host_for_locust_testing
from core.locust.common import fake, get_csrf_token


class AuthenticatedNotepadBehavior(TaskSet):
    def on_start(self):
        self.login()

    def login(self):
        response = self.client.get("/login")
        if response.status_code != 200:
            print(f"Failed to get login page: {response.status_code}")
            return

        csrf_token = get_csrf_token(response)

        response = self.client.post(
            "/login", 
            data={
                "email": "user1@example.com",
                "password": "1234", 
                "csrf_token": csrf_token
            }
        )
        if response.status_code != 200:
            print(f"Login failed: {response.status_code}")

    @task
    def get_notepads(self):
        response = self.client.get("/notepad")
        if response.status_code != 200:
            print(f"Failed to access notepads: {response.status_code}")

    @task
    def create_notepad(self):
        response = self.client.get("/notepad/create")
        if response.status_code != 200:
            print(f"Failed to get notepad creation page: {response.status_code}")
            return

        csrf_token = get_csrf_token(response)

        response = self.client.post(
            "/notepad/create", 
            data={
                "title": fake.sentence(nb_words=4), 
                "content": fake.text(max_nb_chars=200), 
                "csrf_token": csrf_token
            }
        )
        if response.status_code != 200:
            print(f"Failed to create notepad: {response.status_code}")


class NotepadUser(HttpUser):
    tasks = [AuthenticatedNotepadBehavior]
    min_wait = 5000
    max_wait = 9000
    host = get_host_for_locust_testing()
