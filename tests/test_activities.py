def test_get_activities(client):
    # Arrange
    # Activities are reset to initial state by fixture

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)
    assert "Chess Club" in data
    assert "Programming Class" in data
    assert len(data) == 9  # All activities present
    assert "description" in data["Chess Club"]
    assert "schedule" in data["Chess Club"]
    assert "max_participants" in data["Chess Club"]
    assert "participants" in data["Chess Club"]
    assert isinstance(data["Chess Club"]["participants"], list)

def test_signup_success(client):
    # Arrange
    email = "newstudent@mergington.edu"
    activity = "Chess Club"

    # Act
    response = client.post(f"/activities/{activity}/signup?email={email}")

    # Assert
    assert response.status_code == 200
    result = response.json()
    assert "message" in result
    assert f"Signed up {email} for {activity}" == result["message"]
    # Verify participant was added
    response2 = client.get("/activities")
    data = response2.json()
    assert email in data[activity]["participants"]

def test_signup_already_signed_up(client):
    # Arrange
    email = "michael@mergington.edu"  # Already in Chess Club
    activity = "Chess Club"

    # Act
    response = client.post(f"/activities/{activity}/signup?email={email}")

    # Assert
    assert response.status_code == 400
    result = response.json()
    assert "detail" in result
    assert "already signed up" in result["detail"]

def test_signup_activity_not_found(client):
    # Arrange
    email = "student@mergington.edu"
    activity = "Nonexistent Activity"

    # Act
    response = client.post(f"/activities/{activity}/signup?email={email}")

    # Assert
    assert response.status_code == 404
    result = response.json()
    assert "detail" in result
    assert "Activity not found" == result["detail"]

def test_remove_participant_success(client):
    # Arrange
    email = "michael@mergington.edu"
    activity = "Chess Club"

    # Act
    response = client.delete(f"/activities/{activity}/participants?email={email}")

    # Assert
    assert response.status_code == 200
    result = response.json()
    assert "message" in result
    assert f"Removed {email} from {activity}" == result["message"]
    # Verify participant was removed
    response2 = client.get("/activities")
    data = response2.json()
    assert email not in data[activity]["participants"]

def test_remove_participant_not_found(client):
    # Arrange
    email = "notsignedup@mergington.edu"
    activity = "Chess Club"

    # Act
    response = client.delete(f"/activities/{activity}/participants?email={email}")

    # Assert
    assert response.status_code == 404
    result = response.json()
    assert "detail" in result
    assert "Participant not found" == result["detail"]

def test_remove_participant_activity_not_found(client):
    # Arrange
    email = "student@mergington.edu"
    activity = "Nonexistent Activity"

    # Act
    response = client.delete(f"/activities/{activity}/participants?email={email}")

    # Assert
    assert response.status_code == 404
    result = response.json()
    assert "detail" in result
    assert "Activity not found" == result["detail"]