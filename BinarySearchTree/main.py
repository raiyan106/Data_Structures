from Tree import Tree

if __name__ == '__main__':
    tree = Tree()
    tree.addValue(4)
    tree.addValue(2)
    tree.addValue(5)
    tree.addValue(1)
    tree.addValue(3)

    tree.printTree()

    print(tree.findValue(7))
