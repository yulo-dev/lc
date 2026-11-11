class Solution:
    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:
        queue = deque([])
        queue.append(0)
        visited = set()
        visited.add(0)

        while queue:
            room = queue.popleft()
            for r in rooms[room]:
                if r not in visited:
                    queue.append(r)
                    visited.add(r)

        return len(rooms) == len(visited)
