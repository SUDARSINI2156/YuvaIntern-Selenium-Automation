
import uuid

registration_data = [
    {
        "name": "Sudarsini",
        "email": f"sudarsini_{uuid.uuid4().hex[:8]}@example.com",
        "password": "Password123",
        "confirm_password": "Password123"
    },
    {
        "name": "Test User",
        "email": f"testuser_{uuid.uuid4().hex[:8]}@example.com",
        "password": "Password123",
        "confirm_password": "Wrong123"
    }
]
