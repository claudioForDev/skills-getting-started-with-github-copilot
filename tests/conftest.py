from fastapi.testclient import TestClient
from src.app import app, activities
import pytest

# Initial state of activities for resetting
INITIAL_ACTIVITIES = {
    "Chess Club": {
        "description": "Learn strategies and compete in chess tournaments",
        "schedule": "Fridays, 3:30 PM - 5:00 PM",
        "max_participants": 12,
        "participants": ["michael@mergington.edu", "daniel@mergington.edu"]
    },
    "Programming Class": {
        "description": "Learn programming fundamentals and build software projects",
        "schedule": "Tuesdays and Thursdays, 3:30 PM - 4:30 PM",
        "max_participants": 20,
        "participants": ["emma@mergington.edu", "sophia@mergington.edu"]
    },
    "Gym Class": {
        "description": "Physical education and sports activities",
        "schedule": "Mondays, Wednesdays, Fridays, 2:00 PM - 3:00 PM",
        "max_participants": 30,
        "participants": ["john@mergington.edu", "olivia@mergington.edu"]
    },
    "Basketball Team": {
        "description": "Competitive basketball team for interscholastic play",
        "schedule": "Mondays and Wednesdays, 4:00 PM - 5:30 PM",
        "max_participants": 15,
        "participants": ["james@mergington.edu"]
    },
    "Tennis Club": {
        "description": "Learn and practice tennis skills",
        "schedule": "Tuesdays and Thursdays, 4:00 PM - 5:00 PM",
        "max_participants": 20,
        "participants": ["lucas@mergington.edu", "ava@mergington.edu"]
    },
    "Art Studio": {
        "description": "Explore painting, drawing, and mixed media techniques",
        "schedule": "Wednesdays, 3:30 PM - 5:00 PM",
        "max_participants": 25,
        "participants": ["isabella@mergington.edu"]
    },
    "Drama Club": {
        "description": "Perform in theatrical productions and improve acting skills",
        "schedule": "Thursdays, 3:30 PM - 5:00 PM",
        "max_participants": 30,
        "participants": ["noah@mergington.edu", "mia@mergington.edu"]
    },
    "Science Club": {
        "description": "Conduct experiments and explore scientific concepts",
        "schedule": "Mondays, 3:30 PM - 4:30 PM",
        "max_participants": 18,
        "participants": ["liam@mergington.edu"]
    },
    "Debate Team": {
        "description": "Develop public speaking and critical thinking skills",
        "schedule": "Fridays, 3:30 PM - 4:30 PM",
        "max_participants": 16,
        "participants": ["benjamin@mergington.edu", "charlotte@mergington.edu"]
    }
}

@pytest.fixture
def client():
    return TestClient(app)

@pytest.fixture(autouse=True)
def reset_activities():
    # Reset activities to initial state before each test
    activities.clear()
    activities.update(INITIAL_ACTIVITIES)