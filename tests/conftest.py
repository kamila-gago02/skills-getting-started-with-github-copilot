from copy import deepcopy

import pytest
from fastapi.testclient import TestClient

from src import app as app_module


@pytest.fixture(autouse=True)
def isolated_activities():
    original_activities = app_module.activities
    app_module.activities = deepcopy(original_activities)
    yield
    app_module.activities = original_activities


@pytest.fixture
def client():
    with TestClient(app_module.app, follow_redirects=False) as test_client:
        yield test_client