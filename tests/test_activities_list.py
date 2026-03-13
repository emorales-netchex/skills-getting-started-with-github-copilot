from src.app import activities


def test_get_activities_returns_200_and_all_activities(client):
    # Arrange
    expected_count = len(activities)

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200
    payload = response.json()
    assert isinstance(payload, dict)
    assert len(payload) == expected_count


def test_get_activities_returns_expected_activity_structure(client):
    # Arrange
    activity_name = "Chess Club"

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200
    payload = response.json()
    assert activity_name in payload
    assert set(payload[activity_name].keys()) == {
        "description",
        "schedule",
        "max_participants",
        "participants",
    }
    assert isinstance(payload[activity_name]["participants"], list)
