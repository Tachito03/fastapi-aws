from urllib import response
import json
import pytest
import requests
from fastapi.testclient import TestClient
from routes.email import email

client = TestClient(email)



def test_envia_email(client):
        with client.app() as client, client.app_context():
            data = {
                "email": "waxef72794@about27.com", 
                "subject": "Prueba test", 
                "idtemplate": "1"
            }

        response = client.post("/mails", json = json.dumps(data), headers={"Content-Type": "application/json"})
        assert response.status_code == 200
