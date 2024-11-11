import heapq

# Node class for Huffman Tree
class Node:
    def __init__(self, freq, symbol='', left=None, right=None):
        self.freq = freq
        self.symbol = symbol
        self.left = left
        self.right = right

    # For heap comparisons
    def __lt__(self, other):
        return self.freq < other.freq

# Function to generate Huffman codes
def generate_huffman_codes(node, code='', code_map={}):
    if node:
        if not node.left and not node.right:  # Leaf node
            code_map[node.symbol] = code
        generate_huffman_codes(node.left, code + '0', code_map)
        generate_huffman_codes(node.right, code + '1', code_map)
    return code_map

# Main function to perform Huffman Encoding
def huffman_encoding(s):
    # Frequency map of characters
    freq_map = {char: s.count(char) for char in set(s)}
    print("Frequency:", freq_map)

    # Priority queue (min-heap) for nodes
    heap = [Node(freq, symbol) for symbol, freq in freq_map.items()]
    heapq.heapify(heap)

    # Build Huffman Tree using a greedy strategy
    while len(heap) > 1:
        n1 = heapq.heappop(heap)
        n2 = heapq.heappop(heap)
        merged_node = Node(n1.freq + n2.freq, left=n1, right=n2)
        heapq.heappush(heap, merged_node)

    # Generate Huffman codes
    code_map = generate_huffman_codes(heap[0])
    print("Huffman Codes:", code_map)

    # Encode the input string
    encoded_string = ''.join(code_map[char] for char in s)
    print("Encoded String:", encoded_string)

# Input string for encoding
s = input("Enter the string: ")
huffman_encoding(s)



"""
 the time complexity of Huffman Encoding is Huffman Encoding is a lossless compression algorithm that assigns shorter codes to more frequent characters to minimize data size. The program:

Counts character frequencies.
Builds a Huffman Tree using a greedy strategy.
Generates unique binary codes for each character.
Encodes the input string using these codesO(nlogn), where n is the length of the input string.

"""
# Huffman encoding is a compression algorithm that assigns variable-length codes to input characters based on their frequencies. Characters that occur more frequently are assigned shorter codes, while less frequent characters are assigned longer codes. This results in efficient data encoding and reduction in file size.

# Frequent characters are assigned shorter codes, while less frequent characters receive longer codes. This ensures that the overall size of the encoded data is minimized.

# The algorithm builds a binary tree called a Huffman tree. Each character is represented by a leaf node, and the path from the root to the leaf determines the character's code. The process involves:

# Creating nodes for each character and its frequency.
# Merging the two nodes with the smallest frequencies until only one node remains, which becomes the root of the tree.
# Assigning binary codes based on the tree structure (0 for left, 1 for right).
# Huffman coding is widely used in various compression formats like ZIP files, JPEG images, and MP3 audio files due to its efficiency in encoding data.
# Decoding Huffman Codes:

# The decode_huff function takes an encoded string and the Huffman tree, traversing the tree based on the bits (0 for left and 1 for right) to reconstruct the original characters.

# Huffman coding is a lossless data compression algorithm that is used to reduce the size of files without losing any information. It works by assigning variable-length codes to input characters based on their frequencies of occurrence in the data.

# How does Huffman coding ensure that no two codes are the same?

# By constructing a binary tree where each character is represented by a unique path, ensuring that prefix codes do not overlap.
# What are the advantages and disadvantages of using Huffman coding?

# Advantages include efficient compression and lossless encoding; disadvantages may include the need for a frequency table and inefficiency with small data sets.

# Can Huffman coding be used for real-time data compression? Why or why not?

# It can be used, but the overhead of building the frequency table and tree may introduce latency.


# What is the time complexity of building a Huffman tree?

# The time complexity is 
# 𝑂
# (
# 𝑛
# log
# ⁡
# 𝑛
# )
# O(nlogn), where 
# 𝑛
# n is the number of unique characters.

