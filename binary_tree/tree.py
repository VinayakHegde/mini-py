from node import Node

class BinaryTree:
  length = 0
  def __init__(self):
    self.root = None

  # Method to obtain the data
  def get_root(self):
    return self.root

  # Method to add the data
  def add_element(self, data):
    self.length += 1
    if self.root is None:
      self.root = Node(data)
    else:
      self._add(data, self.root)

  def _add(self, data, node):
    if data < node.data:
      if node.left is not None:
        self._add(data, node.left)
      else:
        node.left = Node(data)
    else:
      if node.right is not None:
        self._add(data, node.right)
      else:
        node.right = Node(data)

  # Method for find the data
  def find(self, data):
    if self.root is not None:
      return self._find(data, self.root)
    else:
      return None

  def _find(self, data, node):
    if data == node.data:
      return node
    elif (data < node.data and node.left is not None):
      return self._find(data, node.left)
    elif (data > node.data and node.right is not None):
      return self._find(data, node.right)

  # Method for delete tree
  def delete_tree(self):
    self.root = None
    self.length = 0

  # Method for print tree in terminal
  def print_tree(self):
    if self.root is not None:
      self._print_tree(self.root)

  def _print_tree(self, node):
    if node is not None:
      self._print_tree(node.left)
      print(str(node.data) + ' ')
      self._print_tree(node.right)

