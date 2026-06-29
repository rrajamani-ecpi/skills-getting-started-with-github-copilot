import copy

import pytest
from fastapi.testclient import TestClient

from src.app import activities, app

BASE_ACTIVITIES = copy.deepcopy(activities)


@pytest.fixture(autouse=True)
def reset_activities():
    """Reset in-memory activities before each test for isolation."""
    activities.clear()
    activities.update(copy.deepcopy(BASE_ACTIVITIES))


@pytest.fixture
def client():
    return TestClient(app)
