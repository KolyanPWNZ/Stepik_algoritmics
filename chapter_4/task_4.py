from collections import Counter,  namedtuple
import heapq

class Node(namedtuple("Node", ["left", "right"])):
    def walk(self, code: dict, acc: str):
        """
        :param code: dict - char : code
        :param acc: prefix code
        :return:
        """
        self.left.walk(code, acc + "0")
        self.right.walk(code, acc + "1")


class Leaf(namedtuple("Leaf", ["char"])):
    def walk(self, code: dict, acc: str):
        """
        :param code: dict - char : code
        :param acc: prefix code
        :return:
        """
        code[self.char] = acc or "0"


def huffman_encode(s: str) -> dict:
    # create heap
    h = []
    for ch, freq in Counter(s).items():
        h.append((freq, len(h), Leaf(ch)))
    heapq.heapify(h)

    count = len(h)
    while len(h) > 1:
        # get 2 node or leaf with min freq
        freq1, _count1, left = heapq.heappop(h)
        freq2, _count2, right = heapq.heappop(h)
        # create new element (node)
        heapq.heappush(h, (freq1+freq2, count, Node(left, right)))
        count += 1

    code = {}
    if h:
        [(_freq, _count, root)] = h
        root.walk(code, "")

    return code


def huffman_decode(codes: dict, encodeed_str: str)->str:
    decode_str = ""
    code_cur = ""
    codes_reverse = {v: k for k, v in codes.items()}
    for b in encodeed_str:
        code_cur += b
        if code_cur in codes_reverse:
            decode_str += codes_reverse[code_cur]
            code_cur = ""
    return decode_str


def test(n_iter = 5):
    print('testing startet')
    import random
    import string

    for i in range(n_iter):
        # generation test string
        lenght = random.randint(0, 50)
        s = "".join(random.choice(string.ascii_letters) for _ in range(lenght))
        code = huffman_encode(s)
        encoded = "".join(code[ch] for ch in s)
        decode = huffman_decode(code, encoded)
        if  decode != s:
            print("test", i+1)
            print(f"\tinput string: {s}", f"\tcode string: {encoded}", f"\tdecode string: {decode}", sep="\n")
    print('testing completed')


def main():
    s = input()
    code = huffman_encode(s)
    encoded = "".join(code[ch] for ch in s)
    print(len(code), len(encoded))
    for ch in sorted(code):
        print("{}: {}".format(ch, code[ch]))
    print(encoded)


if __name__ == "__main__":
    test()
    # main()