# Multi-level Cache System Simulation
# Objective: Design a class `CacheSystem` that simulates a two-level cache (L1 and L2). L1 cache has faster access but lower capacity than L2.
# Parameters:
# - l1_size: Integer representing the number of entries L1 cache can hold.
# - l2_size: Integer representing the number of entries L2 cache can hold.
# Returns:
# - None; methods will handle cache operations.
# Details:
# - Implement methods for `put` (to add or update data) and `get` (to retrieve data).
# - Use an LRU (Least Recently Used) policy for cache eviction when the cache is full.
# - If an item is accessed from L2, it should be moved to L1 (if there's space, otherwise evict the least recently used item from L1).

from collections import OrderedDict

class CacheSystem:
    def __init__(self, l1_size, l2_size):
        self.l1_size = l1_size
        self.l2_size = l2_size
        self.l1_cache = OrderedDict()  # L1 cache (OrderedDict for LRU eviction)
        self.l2_cache = {}  # L2 cache (simple dictionary)

    def put(self, key, value):
        # Add/update data in L1 cache
        if key in self.l1_cache:
            # If key exists, move it to the end (most recently used)
            self.l1_cache.move_to_end(key)
        elif len(self.l1_cache) >= self.l1_size:
            # Evict least recently used item from L1
            self.l1_cache.popitem(last=False)
        self.l1_cache[key] = value

        # Check if key exists in L2 cache
        if key in self.l2_cache:
            # Move it to L1 cache
            self.l2_cache.pop(key)
        elif len(self.l2_cache) >= self.l2_size:
            # Evict least recently used item from L2
            self.l2_cache.pop(next(iter(self.l2_cache)))

    def get(self, key):
        # Try to retrieve from L1 cache
        if key in self.l1_cache:
            # Move it to the end (most recently used)
            self.l1_cache.move_to_end(key)
            return self.l1_cache[key]
        # Try to retrieve from L2 cache
        elif key in self.l2_cache:
            # Move it to L1 cache
            value = self.l2_cache.pop(key)
            self.l1_cache[key] = value
            return value
        else:
            return None

cache = CacheSystem(2, 3)
cache.put('a', 1)
cache.put('b', 2)
print(cache.get('a'))  # Expected to access from L1
cache.put('c', 3)
cache.put('d', 4)  # Should trigger eviction in L2, moving 'c' to L1, evicting 'b'
print(cache.get('b'))  # Expected: None
print(cache.get('c'))  # Expected to move from L1, 'd' remains in L2