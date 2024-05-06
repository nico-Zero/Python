# import json
# from random import choice, randint


# class BinaryTree:
#     def __init__(self, rootnode):
#         self.key = rootnode
#         self.leftnode = None
#         self.rightnode = None

#     def insertLeft(self, node):
#         if self.leftnode == None:
#             self.leftnode = BinaryTree(node)
#         else:
#             new_node = BinaryTree(node)
#             if node > self.leftnode.getKey():
#                 new_node.leftnode = self.leftnode
#                 self.leftnode = new_node
#             else:
#                 self.leftnode.leftnode = new_node

#     def insertRight(self, node):
#         if self.rightnode == None:
#             self.rightnode = BinaryTree(node)
#         else:
#             new_node = BinaryTree(node)
#             if node < self.rightnode.getKey():
#                 new_node.rightnode = self.rightnode
#                 self.rightnode = new_node
#             else:
#                 self.rightnode.rightnode = new_node

#     def getLeftNode(self):
#         return self.leftnode

#     def getRightNode(self):
#         return self.rightnode

#     def getKey(self):
#         return self.key

#     def setKey(self, value):
#         self.key = value

#     def maxDepth(self):
#         depth = 0
#         while True:
#             if self.leftnode is not None:
#                 depth += 1
#             else:
#                 return depth

#     def dictify(self):
#         return {
#             "key": self.getKey(),
#             "left": self.getLeftNode().dictify() if self.getLeftNode() else None,  # type: ignore
#             "right": self.getRightNode().dictify() if self.getRightNode() else None,  # type: ignore
#         }


# def makeTree(num, tree):
#     tree = [tree]
#     for _ in range(num):
#         r_node = choice(tree)
#         n = randint(0, 1000)
#         if r_node.getKey() < n:
#             r_node.insertRight(n)
#             tree.append(r_node.getRightNode())
#         elif r_node.getKey() > n:
#             r_node.insertLeft(n)
#             tree.append(r_node.getLeftNode())
#         else:
#             continue
#     return tree[0]


# def pre_order(tree):
#     if tree:
#         print(f"{tree.getKey()} > ", end="")
#         pre_order(tree.getLeftNode())
#         pre_order(tree.getRightNode())


# def in_order(tree):
#     if tree:
#         in_order(tree.getLeftNode())
#         print(f"{tree.getKey()} > ", end="")
#         in_order(tree.getRightNode())


# def post_order(tree):
#     if tree:
#         post_order(tree.getLeftNode())
#         post_order(tree.getRightNode())
#         print(f"{tree.getKey()} > ", end="")


# def print_tree(tree):
#     print(json.dumps(tree.dictify(), indent=4))


# def visual_test(test_times, tree_len, tree):
#     for i in range(1, test_times + 1):
#         print("*" * 200, f"VISUAL TEST :- {i}", "*" * 200, sep="\n")
#         tree = makeTree(tree_len, tree)
#         print_tree(tree)
#         print("*" * 200, f"ORDER TEST :- {i}", "*" * 200, sep="\n")
#         order_test(tree)
#         print()


# def order_test(tree):
#     pre_order(tree)
#     print()
#     in_order(tree)
#     print()
#     post_order(tree)


# bTree = BinaryTree(randint(0, 1000))

# visual_test(4, 30, bTree)

# # order_test(bTree)

# # class TreeNode:
# #     def __init__(self, key):
# #         self.key = key
# #         self.left = None
# #         self.right = None

# # def insert(root, key):
# #     if root is None:
# #         return TreeNode(key)
# #     else:
# #         if key < root.key:
# #             root.left = insert(root.left, key)
# #         else:
# #             root.right = insert(root.right, key)
# #     return root

# # def print_tree(root, level=0, prefix="Root:"):
# #     if root is not None:
# #         print(" " * (level * 4) + prefix + str(root.key))
# #         if root.left is not None or root.right is not None:
# #             print_tree(root.left, level + 1, "L--:")
# #             print_tree(root.right, level + 1, "R--:")

# # # Example usage:
# # if __name__ == "__main__":
# #     # Creating a binary tree
# #     root = None
# #     keys = [20, 10, 30, 5, 15, 25, 35]
# #     for key in keys:
# #         root = insert(root, key)


# #     # Printing the tree
# #     print_tree(root)
print("Hello, World!")
class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val


def levelOrderPrint(tree_root):
    monitor = [tree_root]
    while len(monitor):
        c = []
        for n in monitor:
            if n:
                if n.left:
                    monitor.append(n.left)
                if n.right:
                    monitor.append(n.right)
                c.append(n.val)
            else:
                continue
        if c:
            print(*c, sep=" ")
        monitor = []


n1 = Node(1)
n1.left = Node(2)
n1.right = Node(3)
n1.left.left = Node(4)
n1.left.right = Node(5)
n1.right.left = Node(6)
n1.right.right = Node(7)

levelOrderPrint(n1)
