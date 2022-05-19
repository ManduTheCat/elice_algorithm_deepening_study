def main():
    Node, Branch, Root = map(int, input().split())
    tree = [[] for _ in range(Node + 1)]

    for _ in range(Branch):
        a, b = map(int, input().split())
        tree[a].append(b)
        tree[b].append(a)

    for branch in tree:
        branch.sort()

    visited_DFS = []
    visited_BFS = []

    def DFS(root):
        visited_DFS.append(root)

        for node in tree[root]:
            if node not in visited_DFS:
                DFS(node)

    def BFS(root):
        q = [root]

        while (q):
            root = q.pop(0)
            visited_BFS.append(root)
            for node in tree[root]:
                if (node not in visited_BFS) and (node not in q):
                    q.append(node)

    DFS(Root)
    BFS(Root)
    print((' ').join(map(str, visited_DFS)))
    print((' ').join(map(str, visited_BFS)))


if __name__=='__main__':
    main()