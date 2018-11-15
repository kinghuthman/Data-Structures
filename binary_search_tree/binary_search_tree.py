class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    if value >= self.value:
      if self.right is None:
        self.right = BinarySearchTree(value)
      else:
        self.right.insert(value)
    else:
      if self.left is None:
        self.left = BinarySearchTree(value)
      else:
        self.left.insert(value)

  def contains(self, target):
    if self.value == target:
      return True
    elif target > self.value:
      if self.right == None:
        return False
      return self.right.contains(target)
    elif target < self.value:
      if self.left == None:
        return False
      return self.left.contains(target)
    else:
      return False

  def get_max(self):
    if self.right:
      return self.right.get_max()
    else:
      return self.value
