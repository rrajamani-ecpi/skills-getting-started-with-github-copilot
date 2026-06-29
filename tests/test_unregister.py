def test_unregister_success(client):
    activity = "Chess Club"
    email = "michael@mergington.edu"

    response = client.delete(
        f"/activities/{activity}/participants",
        params={"email": email},
    )

    assert response.status_code == 200
    assert response.json() == {"message": f"Unregistered {email} from {activity}"}

    activities_response = client.get("/activities")
    assert email not in activities_response.json()[activity]["participants"]


def test_unregister_unknown_activity_returns_404(client):
    response = client.delete(
        "/activities/Unknown%20Club/participants",
        params={"email": "student@mergington.edu"},
    )

    assert response.status_code == 404
    assert response.json() == {"detail": "Activity not found"}


def test_unregister_not_signed_up_returns_404(client):
    response = client.delete(
        "/activities/Chess%20Club/participants",
        params={"email": "notenrolled@mergington.edu"},
    )

    assert response.status_code == 404
    assert response.json() == {
        "detail": "Student not signed up for this activity"
    }
