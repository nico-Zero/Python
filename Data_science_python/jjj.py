from random import randint, choice
import faker


class TreeNode:
    def __init__(self, key, payload, left_child=None, right_child=None, parent=None):
        self.key = key
        self.payload = payload
        self.leftChild: TreeNode | None = left_child
        self.rightChild: TreeNode | None = right_child
        self.parent: TreeNode | None = parent

    def hasLeftChild(self):
        return self.leftChild is not None

    def hasRightChild(self):
        return self.rightChild is not None

    def isLeftChild(self):
        return self.parent and self.parent.leftChild == self

    def isRightChild(self):
        return self.parent and self.parent.rightChild == self

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not (self.rightChild or self.leftChild)

    def hasAnyChildren(self):
        return self.rightChild or self.leftChild

    def hasBothChildren(self):
        return self.rightChild and self.leftChild


class BinarySearchTree:
    def __init__(self, root_key, root_value):
        self.root = TreeNode(root_key, root_value)
        self.size = 1

    def __put(self, key, value, currentNode: TreeNode):
        if currentNode.key == key:
            currentNode.payload = value
        elif currentNode.key > key:
            if currentNode.hasLeftChild():
                self.__put(key, value, currentNode.leftChild)  # type: ignore
            else:
                currentNode.leftChild = TreeNode(key, value, parent=currentNode)
        else:
            if currentNode.hasRightChild():
                self.__put(key, value, currentNode.rightChild)  # type: ignore
            else:
                currentNode.rightChild = TreeNode(key, value, parent=currentNode)

    def put(self, key, value):
        if self.root is None:
            self.root = TreeNode(key, value)
        else:
            self.__put(key, value, self.root)
        self.size += 1

    def __setitem__(self, key, value):
        self.put(key, value)

    def __get(self, key, currentNode) -> TreeNode | None:
        print(f"{currentNode.key}---{key}")
        if not currentNode:
            return None
        elif currentNode.key == key:
            return currentNode
        elif currentNode.key > key:
            return self.__get(key, currentNode.leftChild)
        else:
            return self.__get(key, currentNode.rightChild)

    def get(self, key) -> TreeNode | None:
        if self.root:
            return self.__get(key, self.root)
        else:
            return None

    def __getitem__(self, key):
        node = self.get(key)
        if node:
            return node.payload
        else:
            return None

    def __findMinNode(self, node):
        while node.hasLeftChild():
            node = node.leftChild
        return node

    def __findSuccessor(self, node):
        if node.rightChild.hasLeftChild():
            currentNode = node.rightChild.leftChild
            return self.__findMinNode(currentNode)
        else:
            return node.rightChild

    def __delete(self, node):
        if not node.hasAnyChildren():
            if node.isLeftChild():
                node.parent.leftChild = None
            else:
                node.parent.rightChild = None

        elif node.hasBothChildren():
            successor = self.__findSuccessor(node)
            node.key = successor.key
            node.payload = successor.payload
            self.delete(successor)

        else:
            if node.hasLeftChild():
                node.leftChild.parent = node.parent
                if node.isLeftChild():
                    node.parent.leftChild = node.leftChild
                else:
                    node.parent.rightChild = node.leftChild
            else:
                node.rightChild.parent = node.parent
                if node.isRightChild():
                    node.parent.rightChild = node.rightChild
                else:
                    node.parent.rightChild = node.rightChild
        del node

    def delete(self, key):
        if self.size >= 1:
            node = self.get(key)
            if not node:
                raise ValueError("Key doesn't exist.")
            elif node is self.root:
                del self.root
                self.root = None
            else:
                self.__delete(node)
                self.size -= 1
        else:
            raise ValueError("Key doesn't exist.")

    def __delitem__(self, key):
        self.delete(key)

    # def __traversal(self,node):

    def traversal(self, order):
        in_order = list()

        def helper(current_node, order):
            if order == "pre":
                in_order.append(current_node)
                if current_node.hasLeftChild():
                    helper(current_node.leftChild, order)
                if current_node.hasRightChild():
                    helper(current_node.rightChild, order)
            elif order == "in":
                if current_node.hasLeftChild():
                    helper(current_node.leftChild, order)
                in_order.append(current_node)
                if current_node.hasRightChild():
                    helper(current_node.rightChild, order)
            elif order == "post":
                if current_node.hasLeftChild():
                    helper(current_node.leftChild, order)
                if current_node.hasRightChild():
                    helper(current_node.rightChild, order)
                in_order.append(current_node)

        helper(self.root, order)
        return in_order

    def __contains__(self, key):
        if self.get(key):
            return True
        else:
            return False

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()  # type: ignore


fake = faker.Faker()


def generateNode(tree: BinarySearchTree, n):
    for _ in range(n):
        tree.put(randint(1, 1000), fake.name())


def print_tree(tree):
    in_order_objs = tree.traversal("in")
    for node in in_order_objs:
        print(f"Key:- {node.key:^5}    Value:- {node.payload:^20}")

    return in_order_objs


tree = BinarySearchTree(randint(300, 1000), fake.name())

generateNode(tree, 20)

jj = print_tree(tree)

tree.delete(choice(jj).key)

print()
print()

# print_tree(tree)
