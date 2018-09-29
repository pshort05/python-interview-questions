"""""
Given an N-ary tree, write a function that prints out the node values in level-order.

Input:
Node(1, Node(2), Node(3, Node(4)))
 
Output:
1 2 3 4

Solution
Starting from the root, we can traverse the tree using a BFS traversal and print the nodes we visit. 
A follow-up discussion could be about BFS (Breadth-First Search) vs. DFS (Depth-First Search).
"""""


def printLevelOrder(root):
    if not root: return

    queue = [root]
    curLvlCount, nextLvlCount = 1, 0

    while len(queue) != 0:
        node = queue.pop(0)
        curLvlCount -= 1
        print node.val,

        if len(node.children) != 0:
            queue += node.children
            nextLvlCount += len(node.children)

        if curLvlCount == 0:
            curLvlCount, nextLvlCount = nextLvlCount, 0