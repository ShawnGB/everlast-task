# test/test_leads.py
import pytest


@pytest.mark.asyncio
async def test_create_lead(client):
    response = await client.post(
        "/leads/",
        json={
            "name": "Acme Corp",
            "domain": "acme.com",
        },
    )
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "Acme Corp"
    assert data["domain"] == "acme.com"
    assert data["status"] == "new"
    assert "id" in data


@pytest.mark.asyncio
async def test_get_lead(client):
    # Erst einen Lead erstellen
    create_resp = await client.post(
        "/leads/",
        json={"name": "Beta Ltd", "domain": "beta.com"},
    )
    lead_id = create_resp.json()["id"]

    # Dann abrufen
    response = await client.get(f"/leads/{lead_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == lead_id
    assert data["name"] == "Beta Ltd"
    assert data["domain"] == "beta.com"


@pytest.mark.asyncio
async def test_list_leads(client):
    # Sicherstellen, dass mindestens ein Lead existiert
    await client.post("/leads/", json={"name": "Gamma Inc", "domain": "gamma.com"})

    response = await client.get("/leads/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0


@pytest.mark.asyncio
async def test_update_lead(client):
    # Lead anlegen
    create_resp = await client.post(
        "/leads/",
        json={"name": "Delta LLC", "domain": "delta.com"},
    )
    lead_id = create_resp.json()["id"]

    # Lead updaten
    response = await client.patch(
        f"/leads/{lead_id}",
        json={"status": "qualified"},
    )
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "qualified"


@pytest.mark.asyncio
async def test_delete_lead(client):
    # Lead anlegen
    create_resp = await client.post(
        "/leads/",
        json={"name": "Epsilon GmbH", "domain": "epsilon.com"},
    )
    lead_id = create_resp.json()["id"]

    # Löschen
    response = await client.delete(f"/leads/{lead_id}")
    assert response.status_code == 204

    # Erneut abrufen → 404
    get_resp = await client.get(f"/leads/{lead_id}")
    assert get_resp.status_code == 404
