class Trie:
  def __init__(self, value=None):
    self.value = value
    self.children = {}

##  def __repr__(self, level=0):
##    # HELPER METHOD TO PRINT TREE!
##    ret = "--->" * level + repr(self.value) + "\n"
##    for child in self.children.items():
##      ret += child.__repr__(level+1)
##    return ret

  def print_this(self, level=0):
    # HELPER METHOD TO PRINT TREE!
    ret = "--->" * level + str(self.value) + "\n"
    for child, child_node in self.children.items():
      ret += child_node.print_this(level+1)
    #print(ret)
    return ret

  def add_child(self, child_value):
    self.children[child_value] = Trie(child_value)

  def get_value(self):
    return self.value

  def get_child_node(self, value):
    if value in self.children:
        return self.children[value]
    else:
        return False

  def add_value(self, string):
    parent = self
    for letter in string:
      if not parent.get_child_node(letter):
        parent.add_child(letter)
        parent = parent.get_child_node(letter)
      else:
        parent = parent.get_child_node(letter)
        #print("child already exists " + parent.get_value())
    #print(string + " added successfully")

  def add_list_values(self, lis):
    for item in lis:
      self.add_value(item)
      #print("list added successfully = " + str(lis))

  def list_words(self, trie_node):
    my_list = []
    if not trie_node.children:
        my_list.append('')
    for k, v in trie_node.children.items():
        for el in self.list_words(v):
            my_list.append(k+el)
    return my_list

  def return_possibilities(self, prefix):
    if not self.children:
      print("No nodes exist in the tree!")
      return False
    parent = self
    for letter in prefix:
      if parent.get_child_node(letter):
        parent = parent.get_child_node(letter)
      else:
        #print("No results found for input!")
        return False
    #print(str(len(parent.children)) + " results found for input!")
    return [prefix + suffix for suffix in self.list_words(parent)]

def main():
    string_list = ["chance", "charge", "choice", "chore", "cory", "abc", "aids"]
    test = Trie()
    print(test.print_this())
    test.add_list_values(string_list)
    print(test.print_this())
    print(test.list_words(test))
    print(test.return_possibilities("ch"))
