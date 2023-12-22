from tree import BinaryTree
from prompt import get_integer

try:
  length = get_integer('Enter the number of elements you would like to add to the tree: ')

  binary_tree = BinaryTree()

  while binary_tree.length < length:
    binary_tree.add_element(get_integer('Enter the number: '))

  binary_tree.print_tree()

except Exception:
  print("Please try again")

