from copy import deepcopy

import pytest
from fastapi.testclient import TestClient

from src.app import activities, app


@pytest.fixture(autouse=True)
def reset_activities_state():
    """Backup and restore the in-memory activities dict around every test."""
    original = deepcopy(activities)
    yield
    activities.clear()
    activities.update(deepcopy(original))


@pytest.fixture
def client():
    with TestClient(app) as test_client:
        yield test_client
