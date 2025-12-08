import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

class TestPostUser:
    user_data = {
        "name": "My Name",
        "username": "myusername",
        "email": "myusername@example.com",
        "phone": "88002323235",
        "website": "myname.org"
    }

    def test_post_user_status_code(self):
        response = requests.post(f"{BASE_URL}/users", json=self.user_data)
        assert response.status_code == 201, f"Expected 201, got {response.status_code}"
        print("Status code is 201")

    def test_post_user_json_structure(self):
        response = requests.post(f"{BASE_URL}/users", json=self.user_data)
        data = response.json()
        
        expected_fields = ["id", "name", "username", "email"]
        for field in expected_fields:
            assert field in data, f"Field '{field}' is missing in response"
        print("JSON structure is correct")

    def test_post_user_created_id(self):
        response = requests.post(f"{BASE_URL}/users", json=self.user_data)
        data = response.json()
        assert data["id"] == 11, f"Expected ID 11, got {data['id']}"
        print("Created user has correct ID")

    def test_post_user_data_matches(self):
        response = requests.post(f"{BASE_URL}/users", json=self.user_data)
        response_data = response.json()
        
        assert response_data["name"] == self.user_data["name"]
        assert response_data["username"] == self.user_data["username"]
        assert response_data["email"] == self.user_data["email"]
        print("Response data matches request data")

    def test_post_user_content_type(self):
        response = requests.post(f"{BASE_URL}/users", json=self.user_data)
        content_type = response.headers.get("Content-Type", "")
        assert "application/json" in content_type, f"Expected application/json, got {content_type}"
        print("Content-Type is application/json")

if __name__ == "__main__":
    test_instance = TestPostUser()
    
    print("Running POST user tests...")
    test_instance.test_post_user_status_code()
    test_instance.test_post_user_json_structure()
    test_instance.test_post_user_created_id()
    test_instance.test_post_user_data_matches()
    test_instance.test_post_user_content_type()
    print("All POST tests passed!")