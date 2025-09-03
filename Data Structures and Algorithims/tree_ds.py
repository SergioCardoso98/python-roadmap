#elements of the tree = node
#path connecting 2 nodes = edge
#nodes without children= leaf
#1st node = root node
#parent node de outro node = parent node
    # also there is grandparent node, is self explanatory
#max number of edges from root node to a leaf = tree height
#same login but from a parent node = node height

#types of tree
    #binary tree
        #maximum number of children a node can have is 2
    #binary search tree
        #the the more left the node is the smaller its is value


#         8                <- Root node
#        / \
#       3   10             <- Left and right children of root
#      / \    \
#     1   6    14          <- Subtrees of 3 and 10
#        / \   /
#       4   7 13           <- Leaves and internal nodes

#transversing tree
# Node 1
# ├── Node 2 (left)
# ├── Node 3 (right)

    #inorder
        #left -> root -> right
    #preorder
        #root -> left -> right
    #postorder
        #left -> right -> root
