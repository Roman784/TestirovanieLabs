import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

class TestPutUser:
    updated_user_data = {
        "id": 1,
        "name": "Updated Name",
        "username": "updateduser",
        "email": "updated@example.com",
        "phone": "88002323235",
        "website": "updated.org"
    }

    def test_put_user_status_code(self):
        response = requests.put(f"{BASE_URL}/users/1", json=self.updated_user_data)
        assert response.status_code == 200, f"Expected 200, got {response.status_code}"
        print("Status code is 200")

    def test_put_user_json_structure(self):
        response = requests.put(f"{BASE_URL}/users/1", json=self.updated_user_data)
        data = response.json()
        
        expected_fields = ["id", "name", "username", "email"]
        for field in expected_fields:
            assert field in data, f"Field '{field}' is missing in response"
        print("JSON structure is correct")

    def test_put_user_data_updated(self):
        response = requests.put(f"{BASE_URL}/users/1", json=self.updated_user_data)
        response_data = response.json()
        
        assert response_data["name"] == self.updated_user_data["name"]
        assert response_data["username"] == self.updated_user_data["username"]
        assert response_data["email"] == self.updated_user_data["email"]
        assert response_data["phone"] == self.updated_user_data["phone"]
        print("User data updated correctly")

    def test_put_user_id_unchanged(self):
        response = requests.put(f"{BASE_URL}/users/1", json=self.updated_user_data)
        data = response.json()
        assert data["id"] == 1, f"Expected ID 1, got {data['id']}"
        print("User ID remains unchanged")

    def test_put_user_json_schema(self):
        response = requests.put(f"{BASE_URL}/users/1", json=self.updated_user_data)
        data = response.json()
        
        assert isinstance(data["id"], int)
        assert isinstance(data["name"], str)
        assert isinstance(data["username"], str)
        assert isinstance(data["email"], str) and "@" in data["email"]
        print("JSON schema is valid")

if __name__ == "__main__":
    test_instance = TestPutUser()
    
    print("Running PUT user tests...")
    test_instance.test_put_user_status_code()
    test_instance.test_put_user_json_structure()
    test_instance.test_put_user_data_updated()
    test_instance.test_put_user_id_unchanged()
    test_instance.test_put_user_json_schema()
    print("All PUT tests passed!")