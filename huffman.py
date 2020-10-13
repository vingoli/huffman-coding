import math


class Node:
    def __init__(self, symbols, percentage):
        self.name = symbols
        self.percentage = percentage
        self.left = None
        self.right = None
        self.father = None
        # every nodes has a huffman code
        self.code = ''


# Convert input data into nodes
def create_prim_nodes(symbols, percentage):
    if len(percentage) != len(symbols):
        raise Exception('Symbol and number of occurrences do not match！')
    # if sum(percentage) != 1:
    #     raise Exception('The input percentage is wrong!')
    nodes = []
    for i in range(len(symbols)):
        nodes.append(Node(symbols[i], percentage[i]))
    return nodes


# create the Binary(huffman) tree
def create_hf_tree(nodes):
    tree_nodes = nodes.copy()
    while len(tree_nodes) > 1:
        tree_nodes.sort(key=lambda node: node.percentage)

        new_left = tree_nodes.pop(0)
        new_right = tree_nodes.pop(0)
        new_node = Node(None, (new_left.percentage + new_right.percentage))
        new_node.left = new_left
        new_node.right = new_right
        new_left.father = new_right.father = new_node
        tree_nodes.append(new_node)

    return tree_nodes[0]  # 返回根节点


def make_dictionary(root):
    dic = {}
    stack = [root]

    while len(stack) != 0:
        root = stack.pop()

        if root.left:
            code = root.code + '0'
            stack.append(root.left)
            root.left.code = code
            if root.left.name is not None:
                dic[root.left.name] = code

        if root.right:
            code = root.code + '1'
            stack.append(root.right)
            root.right.code = code
            if root.right.name is not None:
                dic[root.right.name] = code
    return dic


# huffman efficiency
def coding_efficiency(symbols, percentage, dic):
    info_entropy = 0
    huffman_entropy = 0
    for i in range(len(symbols)):
        info_entropy += -percentage[i] * math.log2(percentage[i])
        huffman_entropy += percentage[i] * len(dic[symbols[i]])
    return info_entropy,huffman_entropy


if __name__ == '__main__':
    usr_input = input('Please choose the program. 1:Advanced mode 2:Simple mode')
    print('you have chosen:',usr_input )
    if usr_input == '1':
        a=input("Please input the sentence")
        print('you have input:',a)
        symbols = []
        percentage = []
        dic = {}
        for i in a:
            dic[i] = a.count(i)/len(a)
        for i in dic:
            symbols.append(i)
            percentage.append(dic[i])

    elif usr_input == '2':
        symbols = ['I', 'L', 'o', 'v', 'e', 'C', 'h', 'i', 'n', 'a']
        percentage = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]

    else:
        raise Exception('Please choose the right mode!')
    # Convert input data into nodes
    nodes = create_prim_nodes(symbols, percentage)
    # create the Binary(huffman) tree
    root = create_hf_tree(nodes)
    # create the Binary(huffman) tree
    dic = make_dictionary(root)

    for key in dic.keys():
        print(key, ': ', dic[key])

    print(coding_efficiency(symbols, percentage, dic))
