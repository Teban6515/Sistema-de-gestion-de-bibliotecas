

class ReservationStack:
      
    def __init__(self):
        """Initialize empty reservation stack."""
        self.items = []
    
    def push(self, user_id):

        #Add a reservation to the stack (LIFO).
        
       
        self.items.append(user_id)
        print(f"   📚 {user_id} added to reservation stack (position: TOP)")
        return True
    
    def pop(self):

        #Remove and return the MOST RECENT reservation (LIFO).
        
        if self.is_empty():
            return None
        
        user_id = self.items.pop()
        print(f"   ✅ {user_id} served from reservation stack (was most recent)")
        return user_id
    
    def peek(self):
        
        # View the NEXT user to be served without removing them.

        if self.is_empty():
            return None
        return self.items[-1]  # Top of stack
    
    def is_empty(self):
        """Check if reservation stack is empty."""
        return len(self.items) == 0
    
    def size(self):
        """Get number of reservations in stack."""
        return len(self.items)
    
    def clear(self):
        """Remove all reservations."""
        self.items.clear()
    
    def get_all_reservations(self):
        """
        Get all reservations in order (top to bottom).
        
        Returns:
            list: List of user IDs, top of stack first
        """
        return self.items[::-1]  # Reverse to show top first
    
    def to_dict(self):
        """Convert to dictionary for JSON serialization."""
        return {
            'items': self.items,
            'size': len(self.items)
        }
    
    @staticmethod
    def from_dict(data):
        """Create ReservationStack from dictionary."""
        stack = ReservationStack()
        stack.items = data.get('items', [])
        return stack
    
    def __repr__(self):
        if self.is_empty():
            return "ReservationStack(empty)"
        top = self.items[-1]
        return f"ReservationStack(size={len(self.items)}, next={top})"
    
    def __len__(self):
        return len(self.items)
    
    def __iter__(self):
        """Iterate from top to bottom (most recent first)."""
        return reversed(self.items)

