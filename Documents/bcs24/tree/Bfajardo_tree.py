#Tree
'''
	Create a tree from python file that shows this tree structure based on Mini-activity tree figure

	And based on this python file, identify the following:

		- root
		- Leaves
		- ancestors of H
		- descendants of G
		- siblings of I
		- parent of K
		- children of D
		- height of the tree
		- height of node G
		- level of node H
		- level of node A
		- height of node E   
		- draw the subtrees of node H

'''
from bigtree import Node

def create_tree():
    root = Node("A")
    B = Node("B", parent=root)
    C = Node("C", parent=B)
    D = Node("D", parent=B)
    E = Node("E", parent=D)
    F = Node("F", parent=D)
    G = Node("G", parent=root)
    H = Node("H", parent=G)
    I = Node("I", parent=H)
    J = Node("J", parent=H)
    K = Node("K", parent=H)
    L = Node("L", parent=J)
    M = Node("M", parent=K)

    return root, B, C, D, E, F, G, H, I, J, K, L, M

def print_Tree(root):
    print("This is your tree: ")
    root.show()

def show_subtree(node):
    print(f"\nThis is the subtree of node {node.name}: ")
    node.show()

def find_information(root, B, C, D, E, F, G, H, I, J, K, L, M):
    print("Root: ", root.name)
    print("Leaves: ", [node.name for node in root.leaves])
    print("Ancestors of H: ", [node.name for node in H.ancestors])
    print("Descendants of G: ", [node.name for node in G.descendants])
    print("Siblings of I: ", [node.name for node in I.siblings])
    print("Parent of K: ", [K.parent.name])
    print("Children of D: ", [node.name for node in D.children])
    print("Depth of the tree: ", root.depth) 
    print("Depth of node G: ", G.depth) 
    print("Depth of node H: ", H.depth) 
    print("Depth of node E: ", E.depth) 


def main():
    root, B, C, D, E, F, G, H, I, J, K, L, M = create_tree()
    print_Tree(root)
    find_information(root, B, C, D, E, F, G, H, I, J, K, L, M)
    show_subtree(H)
   

main()

