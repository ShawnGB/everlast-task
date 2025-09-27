import pytest


@pytest.mark.asyncio
async def test_create_contact(client):
    response = await client.post(
        "/contacts/",
        json={
            "first_name": "Alice",
            "last_name": "Smith",
            "emails": [{"value": "alice@example.com", "is_primary": True}],
        },
    )
    assert response.status_code == 201
    data = response.json()
    assert data["first_name"] == "Alice"
    assert data["contact_emails"][0]["value"] == "alice@example.com"


@pytest.mark.asyncio
async def test_get_contact(client):
    # Erst erstellen
    response = await client.post(
        "/contacts/",
        json={"first_name": "Bob", "last_name": "Jones"},
    )
    contact_id = response.json()["id"]

    # Dann abrufen
    response = await client.get(f"/contacts/{contact_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["first_name"] == "Bob"
    assert data["last_name"] == "Jones"
