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
    create_resp = await client.post(
        "/leads/",
        json={"name": "Beta Ltd", "domain": "beta.com"},
    )
    lead_id = create_resp.json()["id"]

    response = await client.get(f"/leads/{lead_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == lead_id
    assert data["name"] == "Beta Ltd"
    assert data["domain"] == "beta.com"


@pytest.mark.asyncio
async def test_list_leads(client):
    await client.post("/leads/", json={"name": "Gamma Inc", "domain": "gamma.com"})

    response = await client.get("/leads/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0


@pytest.mark.asyncio
async def test_update_lead(client):
    create_resp = await client.post(
        "/leads/",
        json={"name": "Delta LLC", "domain": "delta.com"},
    )
    lead_id = create_resp.json()["id"]

    response = await client.put(
        f"/leads/{lead_id}",
        json={"status": "qualified"},
    )
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "qualified"


@pytest.mark.asyncio
async def test_delete_lead(client):
    create_resp = await client.post(
        "/leads/",
        json={"name": "Epsilon GmbH", "domain": "epsilon.com"},
    )
    lead_id = create_resp.json()["id"]

    response = await client.delete(f"/leads/{lead_id}")
    assert response.status_code == 204

    get_resp = await client.get(f"/leads/{lead_id}")
    assert get_resp.status_code == 404


# -------- Erweiterte Tests --------


@pytest.mark.asyncio
async def test_create_lead_with_existing_contact(client):
    # Contact anlegen
    resp = await client.post(
        "/contacts/",
        json={
            "first_name": "Charlie",
            "last_name": "Brown",
            "emails": [{"value": "charlie@example.com", "is_primary": True}],
        },
    )
    contact_id = resp.json()["id"]

    # Lead mit diesem Contact
    resp = await client.post(
        "/leads/",
        json={
            "name": "Zeta AG",
            "domain": "zeta.com",
            "primary_contact_id": contact_id,
        },
    )
    assert resp.status_code == 201
    data = resp.json()
    assert data["primary_contact_id"] == contact_id


@pytest.mark.asyncio
async def test_create_lead_with_new_contact(client):
    resp = await client.post(
        "/leads/",
        json={
            "name": "Eta GmbH",
            "domain": "eta.de",
            "primary_contact": {
                "first_name": "Lisa",
                "last_name": "Müller",
                "emails": [{"value": "lisa@eta.de", "is_primary": True}],
            },
        },
    )
    assert resp.status_code == 201
    data = resp.json()
    assert data["primary_contact_id"] is not None


@pytest.mark.asyncio
async def test_list_leads_with_filter(client):
    # Lead mit Status "lost"
    resp = await client.post(
        "/leads/",
        json={"name": "Theta Inc", "domain": "theta.com", "status": "lost"},
    )
    assert resp.status_code == 201

    # Suche nach "theta" + status "lost"
    resp = await client.get("/leads/?q=theta&status=lost&limit=10&offset=0")
    assert resp.status_code == 200
    data = resp.json()
    assert any("theta" in lead["domain"] for lead in data)
    assert all(lead["status"] == "lost" for lead in data)


@pytest.mark.asyncio
async def test_update_lead_status_endpoint(client):
    resp = await client.post(
        "/leads/",
        json={"name": "Iota GmbH", "domain": "iota.com"},
    )
    lead_id = resp.json()["id"]

    resp = await client.post(f"/leads/{lead_id}/status?status=qualified")
    assert resp.status_code == 200
    data = resp.json()
    assert data["status"] == "qualified"
