autocomplete_trie.py was my first data structure and hook to look into more.

Here are 3 popular ways to do Depth First Search.
 * Inorder traversal:
```py
def inorder_traversal(self, new_root):
    current = new_root
    if current is None:
        return

    self.inorder_traversal(current.left)
    print(current.data)
    self.inorder_traversal(current.right)
```

 * Preorder traversal:
```py
def preorder_traversal(self, new_root):
    current = new_root
    if current is None:
        return 
    
    print(current.data)
    self.preorder_traversal(current.left)
    self.preorder_traversal(current.right)
```

More info soon
