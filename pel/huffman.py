# A Huffman Tree Node
class Node:
    def __init__(self, prob=None, symbol=None, left=None, right=None):
        # probability of symbol
        self.prob = prob

        # symbol
        self.symbol = symbol

        # left node
        self.left = left

        # right node
        self.right = right

        # tree direction (0/1)
        self.code = ''

#Huffman Tree Maker from Huffman Codes
class HuffTree():
    def __init__(self,huff_codes):
        characters = []
        self.head = Node()
        for key in huff_codes:
            characters = huff_codes[key]
            code = []
            for code_for_char in characters:
                code.append(code_for_char)
            self.nodeMaker(code, self.head, key)

    def get_head(self):
        return self.head


    def nodeMaker(self,code,head,symb):
        head = self.head
        depth_tree = len(code)
        current_lvl = 0
        while depth_tree>current_lvl:
            if code[current_lvl] == '0':
                if head.left is None:
                    if current_lvl == depth_tree-1:
                        head.left = Node(symbol=symb)
                    else:
                        head.left = Node()
                    head = head.left
                    current_lvl += 1
                    continue
                else:
                    head = head.left
                    current_lvl += 1
                    continue

            if code[current_lvl] == '1':
                if head.right is None:
                    if current_lvl == depth_tree-1:
                        head.right = Node(symbol=symb)
                    else:
                        head.right = Node()
                    head = head.right
                    current_lvl += 1
                    continue
                else:
                    head = head.right
                    current_lvl += 1
                    continue



class HuffMan():
    def __init__(self):
        self.codes = dict()


    def Calculate_Codes(self,node, val=''):
        newVal = val + str(node.code)
        if (node.left):
            self.Calculate_Codes(node.left, newVal)
        if (node.right):
            self.Calculate_Codes(node.right, newVal)

        if (not node.left and not node.right):
            self.codes[node.symbol] = newVal
        return self.codes


    def Calculate_Probability(self,data):
        symbols = dict()
        for element in data:
            if symbols.get(element) == None:
                symbols[element] = 1
            else:
                symbols[element] += 1
        return symbols


    def Output_Encoded(self,data,coding):
        encoding_output = []
        for c in data:
            encoding_output.append(coding[c])

        string = ''.join([str(item) for item in encoding_output])
        return string


    def Total_Gain(self,data, coding):
        before_compression = len(data) * 8
        after_compression = 0
        symbols = coding.keys()
        for symbol in symbols:
            count = data.count(symbol)
            after_compression += count * len(coding[symbol])
        return after_compression


    def Huffman_Encoding(self,data):
        symbol_with_probs = self.Calculate_Probability(data)
        symbols = symbol_with_probs.keys()
        probabilities = symbol_with_probs.values()

        nodes = []

        for symbol in symbols:
            nodes.append(Node(symbol_with_probs.get(symbol), symbol))

        while len(nodes) > 1:
            # sort all the nodes in ascending order based on their probability
            nodes = sorted(nodes, key=lambda x: x.prob)
            # pick 2 smallest nodes
            right = nodes[0]
            left = nodes[1]

            left.code = 0
            right.code = 1

            # combine the 2 smallest nodes to create new node
            newNode = Node(left.prob+right.prob, left.symbol +
                        right.symbol, left, right)

            nodes.remove(left)
            nodes.remove(right)
            nodes.append(newNode)
        
        huffman_encoding = self.Calculate_Codes(nodes[0])
        print("symbols with codes", huffman_encoding)
        outLen = self.Total_Gain(data, huffman_encoding)
        encoded_output = self.Output_Encoded(data, huffman_encoding)
        return encoded_output, nodes[0], outLen, huffman_encoding


    def Huffman_Decoding(self,encoded_data, huffman_tree):
        tree_head = huffman_tree
        decoded_output = []
        for x in encoded_data:
            if x == '1':
                huffman_tree = huffman_tree.right
            elif x == '0':
                huffman_tree = huffman_tree.left
            try:
                if huffman_tree.left.symbol == None and huffman_tree.right.symbol == None:
                    pass
            except AttributeError:
                decoded_output.append(huffman_tree.symbol)
                huffman_tree = tree_head

        string = ''.join([str(item) for item in decoded_output])

        return string