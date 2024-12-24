def main():
    # Test the code
    g = Graph(4)
    g.add_edge(0, 1, 9)
    g.add_edge(0, 2, 6)
    g.add_edge(0, 3, 5)
    g.add_edge(1, 3, 15)
    g.add_edge(2, 3, 4)

    mst = g.kruskal_mst()
    print("Edges in the MST:")
    for u, v, weight in mst:
        print(f"{u} -- {v} == {weight}")
    
class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.edges = []  # List to store edges (weight, u, v)

    def add_edge(self, u, v, w):
        self.edges.append((w, u, v))

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def union(self, parent, rank, x, y):
        root_x = self.find(parent, x)
        root_y = self.find(parent, y)

        # Union by rank
        if rank[root_x] < rank[root_y]:
            parent[root_x] = root_y
        elif rank[root_x] > rank[root_y]:
            parent[root_y] = root_x
        else:
            parent[root_y] = root_x
            rank[root_x] += 1

    def kruskal_mst(self):
        self.edges.sort()  # Sort edges by weight
        parent = [i for i in range(self.V)]  # Initialize parent array
        rank = [0] * self.V  # Initialize rank array
        mst = []  # Store MST edges

        for edge in self.edges:
            w, u, v = edge
            root_u = self.find(parent, u)
            root_v = self.find(parent, v)

            if root_u != root_v:  # Add edge if it doesn't form a cycle
                mst.append((u, v, w))
                self.union(parent, rank, root_u, root_v)

        return mst

if __name__ == "__main__" :
    main()