import os


def line_numbers(file_path, word_list):  # Defining line-numbers to each line from the file
    with open(file_path, 'r') as f:
        results = {word: [] for word in word_list}
        for num, line in enumerate(f, start=0):
            for word in word_list:
                if word in line:
                    results[word].append(num)
    return results


mylines = []  # appending list for lines from the file
with open("input1.txt", 'rt') as myfile:
    for myline in myfile:
        mylines.append(myline)


def get_block_range(filename, lookupValue):  # to get specific block range from input using look-up-value
    if not os.path.getsize(filename):
        return None, 0
    with open(filename, 'r') as file:
        lookup_position = None
        for num, line in enumerate(file, 1):
            if lookup_position is None and lookupValue in line:
                lookup_position = num
        return lookup_position, num


# Automatic simultaneous generation of statistics for multiple record Id’s
# running on an instance of an Access point, thus the automatic
# generation of multiple CSV, JSON and PDML files for numerous record Id’s
# can be done using the code from below


var1 = get_block_range("input.txt", '')  # assuming input file = input.txt
word = ['Frame ']
results = line_numbers('input.txt', word)
for word, lines in results.items():
    linum = (','.join(map(str, lines)))
linum = linum.split(',')

i, j, lastpt = 0
for i in range(0, len(linum)):
    firstpt = int(linum[i])
    try:
        lastpt = int(linum[i + 1])
    except IndexError:
        lastpt = int(var1[1])
    for j in range(firstpt, lastpt):
        print(mylines[j],
              file=open("FRAME_NO_" + str(i) + ".txt", "a+"))  # PARSED: Seperate output files for each frame number to
for i in range(0, len(linum)):
    q, j, l, p = 0
    Linnum, linesww, rntistring, lastlines, framestring, pdustring = ([] for i in range(6))
    var3 = get_block_range("FRAME_NO_" + str(i) + ".txt", '')
    with open("FRAME_NO_" + str(i) + ".txt", 'rt') as fileww:
        for lineww in fileww:
            linesww.append(lineww)
    with open("FRAME_NO_" + str(i) + ".txt", 'r+') as file:
        for linnum, line in enumerate(file, 0):
            if '    PDU[' in line:
                Linnum.append(linnum)
                q += 1
    for j in range(0, int(q)):
        added_done = 0
        firstpoint = int(Linnum[j])
        try:
            lastpoint = int(Linnum[j + 1])
        except IndexError:
            lastpoint = int(var3[1])
        for k in range(firstpoint, lastpoint):
            if added_done == 0:
                added_done = 1
                with open("FRAME_NO_" + str(i) + ".txt", 'r+') as filewww:
                    for l in range(int(var3[0]) - 1, Linnum[0]):
                        framestring = linesww[l]
                        print('\n'.join([p for p in framestring.split('\n') if len(p) > 0]),
                              file=open("PDU_" + str(j) + "_OF_FRAME_" + str(i) + ".txt",
                                        "a+"))  # PARSED: seperate text files for PDU entries for each frames
            pdustring = linesww[k]
            print('\n'.join([p for p in pdustring.split('\n') if len(p) > 0]),
                  file=open("PDU_" + str(j) + "_OF_FRAME_" + str(i) + ".txt", "a+"))
            file.close()
        var4 = 0
        var4 = get_block_range("PDU_" + str(j) + "_OF_FRAME_" + str(i) + ".txt", '')
        with open("PDU_" + str(j) + "_OF_FRAME_" + str(i) + ".txt", "r+") as lastfile:
            for lastlinenum, lastline in enumerate(lastfile, 0):
                if '            RNTI: ' in lastline:
                    rntistring = lastline
                    w = 0
                    w = int(re.search(r'\d+', rntistring).group())
                    # print(w)
                    oldfile = open("PDU_" + str(j) + "_OF_FRAME_" + str(i) + ".txt", "r+")
                    newfile = open("RNTI_" + str(w) + ".txt", 'a+')
                    newfile.write(oldfile.read())
                    oldfile.close()
                    newfile.close()

#