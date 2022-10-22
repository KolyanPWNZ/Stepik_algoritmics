class NodeLetter:
    def __init__(self, freq, value, childs = list()):
        self.freq = freq
        self.value = value
        self.childs = childs
        self.code = ""


s = input()

letters = dict()
value = 'value'
freq = 'freq'
childs = 'child'

for l in s:
    if l not in letters:
        letters[l] = dict()
        letters[l][freq] = 1
        letters[l][value] = l
    else:
        letters[l][freq] += 1

inpud_data = list()
for l in letters.values():
    inpud_data.append(NodeLetter(l[freq], l[value]))

inpud_data.sort(key=lambda l: l.freq, reverse=True)

nodes = list()

while len(inpud_data) > 1:
    # select letters with min frequency
    l_min_1 = min(inpud_data, key=lambda l: l.freq)
    inpud_data.remove(l_min_1)
    l_min_2 = min(inpud_data, key=lambda l: l.freq)
    inpud_data.remove(l_min_2)

    # create node with new childs

    nodes.append(NodeLetter(l_min_1.freq + l_min_2.freq, "node" + str(len(nodes)), [l_min_1, l_min_2]))

    inpud_data.append(nodes[-1])

if len(inpud_data) > 0 and len(inpud_data[0].childs) == 0:
    childs
    node = NodeLetter(inpud_data[0].freq, "node" + str(len(nodes)))
    node.childs = [inpud_data[0],]
    nodes.append(node)

# formating output data
num_letters = 0
base_code = ["", ""]
size = "size"
letters_code = dict()

# calculate letter code (node selection in ascending order of frequency)
for node in nodes[-1::-1]:
    for child_id in range(len(node.childs)):
        letter = node.childs[child_id].value
        if len(letter) == 1: # if not a node
            num_letters += 1
            letters_code[letter] = node.code + str(child_id)
        else:
            node.childs[child_id].code = node.code + str(child_id)

out_code = ""
for l in s:
    out_code += letters_code[l]
print(num_letters, len(out_code))
for l in letters_code:
    print(l+":", letters_code[l])
print(out_code)
