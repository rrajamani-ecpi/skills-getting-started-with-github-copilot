def test_get_activities_returns_expected_structure(client):
    response = client.get("/activities")

    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)
    assert len(data) == 9

    chess_club = data["Chess Club"]
    assert set(chess_club.keys()) == {
        "description",
        "schedule",
        "max_participants",
        "participants",
    }
    assert isinstance(chess_club["participants"], list)


def test_get_activities_contains_seed_data(client):
    response = client.get("/activities")

    assert response.status_code == 200
    data = response.json()
    assert "michael@mergington.edu" in data["Chess Club"]["participants"]
    assert data["Programming Class"]["max_participants"] == 20
