"""User Manager - CRUD operations for users"""

class UserManager:
    def __init__(self):
        self.users = {}
    
    def create_user(self, user):
        if user.user_id in self.users:
            return False, "User ID already exists"
        self.users[user.user_id] = user
        return True, f"User created: {user.name}"
    
    def get_user(self, user_id):
        return self.users.get(user_id)
    
    def update_user(self, user_id, **kwargs):
        user = self.users.get(user_id)
        if not user:
            return False, "User not found"
        
        for key, value in kwargs.items():
            if hasattr(user, key):
                setattr(user, key, value)
        
        return True, f"User updated: {user.name}"
    
    def delete_user(self, user_id):
        if user_id in self.users:
            user = self.users.pop(user_id)
            return True, f"User deleted: {user.name}"
        return False, "User not found"
    
    def list_all_users(self):
        return list(self.users.values())
    
    def search_users(self, query):
        query_lower = query.lower()
        return [u for u in self.users.values() 
                if query_lower in u.name.lower() or query_lower in u.email.lower()]
