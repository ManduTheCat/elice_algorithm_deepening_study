def main():
    level = int(input())
    paper = list(map(int, input().split()))
    tree = [[] for _ in range(level)]

    def inorder(arr, depth):
        if len(arr)==1:
            tree[depth].append(arr[0])
            return
        
        mid = len(arr)//2
        tree[depth].append(arr[mid])
        inorder(arr[:mid], depth+1)
        inorder(arr[mid+1:], depth+1)
    
    inorder(tree, 0)
    
    for branch in tree:
        print((' ').join(map(str, branch)))


if __name__=='__main__':
    main()