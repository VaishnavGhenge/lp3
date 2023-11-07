import heapq
from collections import defaultdict

class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def generate_tree(map):
    tree = [HuffmanNode(char, freq) for char, freq in map.items()]
    heapq.heapify(tree)

    while len(tree) > 1:
        left = heapq.heappop(tree)
        right = heapq.heappop(tree)
        node = HuffmanNode(None, left.freq + right.freq)
        node.left = left
        node.right = right
        heapq.heappush(tree, node)
    return tree[0]

def generate_code(root, current_code, huffman_codes):
    if root is None:
        return

    if root.char is not None:
        huffman_codes[root.char] = current_code
    generate_code(root.left, current_code + '0', huffman_codes)
    generate_code(root.right, current_code + '1', huffman_codes)

def encode(data):
    map = defaultdict(int)
    for char in data:
        map[char] += 1

    root = generate_tree(map)
    huffman_codes = {}
    generate_code(root, '', huffman_codes)

    encoded_data = ''.join(huffman_codes[char] for char in data)
    
    return encoded_data

if __name__ == '__main__':
    data = 'my name is vaishnav'
    encoded_string = encode(data)
    print(encoded_string)
