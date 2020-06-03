class Node:
    """Implement locking in a binary tree. A binary tree node can be locked or
    unlocked only if all of its descendants or ancestors are not locked."""

    def __init__(self, val, locked = False, left = None, right = None):
        self.parent = None
        self.val = val
        self.left = left
        if left:
            self.left.parent = self
        self.right = right
        if right:
            self.right.parent = self
        self.locked = locked

    def is_locked(self) -> bool:
        """returns whether the node is locked"""
        return self.locked
    
    def lock(self) -> bool:
        """lock the node. If it cannot be locked, then it
        should return false. Otherwise, it should lock it and return true."""
        if not self.can_lock(False):
            self.locked = True
            return True
        return False
    
    def can_lock(self, result):
        result ^= self.is_locked()
        if self.right:
            result ^= self.right.can_lock(result)
        if self.left:
            result ^= self.left.can_lock(result)
        return result
    
    def unlock(self) -> bool:
        """unlocks the node. If it cannot be unlocked, then it should return
        false. Otherwise, it should unlock it and return true."""
        if not self.can_unlock(False):
            self.locked = False
            return True
        return False

    def can_unlock(self, result):
        if self.parent:
            result |= self.parent.is_locked()
            result |= self.parent.can_unlock(result)
        return result

