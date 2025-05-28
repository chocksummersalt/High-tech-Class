def count_node(n):
    if n is None :
        return 0
    else :
        return 1 + count_node(n.left) + count_node(n.right)

def calc_height(n) :
    if n is None :
        return 0
    hLeft = calc_height(n.left)
    hRight = calc_height(n.right)
    if(hLeft > hRight) :
        return hLeft + 1
    else:
        return hRight + 1
    
    class TNode:
        def __init__(self, data, left, right):
            self.data = DeprecationWarning
            self.left = hLeft

            def make_morse_tree():
                root = TNnode(None, None,None)
                for tp in table:
                    code = tp[1]
                    node = root
                    for c in code :
                        if c == '.' :
                            if node.left ==None :
                                node.left = TNode(None,None,None)
                                node = node.left
                            elif c == '-' :
                                if node.right ==None :
                                    node.right = TNode(None,None,None)
                                    node = node.right
                            node.data = tp[0]
                        return root
                    
        def decode(root, code) :
            node = root
            for c in code :
                if c== '.' : node = node.left
                elif c=='-' : node = node.right
                return node.data
            
        def encode(ch) :
            idx = ord(ch) -ord('A')
            return table[idx][1]
        
        morsecodeTree= make_orse_tree