'''
Scenario 1:Vignan Campus Map
8context: Each bullding in a college campus is a node, and walkable paths are edges,.
Represent the campus map using an adjacency list, 
ICheck If there's a path from the library to the Auditorium using BFS.List all buildings that are directly connected to the Admin Block.
Use DFS to visit all reachable buildings from the Main Gate. 
Find if there are any disconnected buildings (buildings not connected to campus).
'''
campus = {
    "main gate": ["admin block"],
    "admin block": ["main gate", "library", "canteen", "engineering block"],
    "library": ["admin block", "hostel", "auditorium"],  # made bidirectional
    "canteen": ["admin block", "hostel"],
    "auditorium": ["library"],
    "engineering block": ["admin block", "science block"],
    "science block": ["engineering block"],
    "hostel": ["canteen", "library"]  # made bidirectional
}

def bfs(start, target):
    visited = set()
    queue = [start.lower()]
    target = target.lower()
    while queue:
        b = queue.pop(0)
        if b == target:
            return True
        if b not in visited:
            visited.add(b)
            queue += [n.lower() for n in campus[b] if n.lower() not in visited]
    return False

def dfs(start, visited=None):
    if visited is None:
        visited = set()
    if start not in visited:
        print(start, end=' ')
        visited.add(start)
        for neighbor in campus[start]:
            dfs(neighbor, visited)

def disconnected():
    visited = set()
    dfs(next(iter(campus)), visited)
    return set(campus.keys()) - visited

# ------------------------
# OUTPUT SECTION
# ------------------------

print("1. Campus Map:")
for building, neighbors in campus.items():
    print(f"{building.title()} -> {', '.join([n.title() for n in neighbors])}")

print("\n2. Path from Library to Auditorium exists:")
print("Yes" if bfs("library", "auditorium") else "No")

print("\n3. Direct Connections from Admin Block:")
print(", ".join(campus["admin block"]).title())

print("\n4. DFS from Main Gate:")
dfs("main gate")
print()

print("\n5. Disconnected Buildings:")
d = disconnected()
print(", ".join(d) if d else "None, campus is fully connected.")
