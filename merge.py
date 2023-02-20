import sys
if len(sys.argv) == 5:
    file1 = open(str(sys.argv[2]),'r')
    file2 = open(str(sys.argv[3]),'r')
    l1 = file1.readline()
    l2 = file2.readline()
    merged_file = open(str(sys.argv[4]),'a')
    while True:
        if not l1 and not l2:
            break
        elif l1 and not l2:
            merged_file.write(l1)
            l1=file1.readline()
        elif l2 and not l1:
            merged_file.write(l2)
            l2=file2.readline()
        elif l1.endswith(':'):
            merged_file.write(l1)
            l1=file1.readline()
        elif l2.endswith(':'):
            merged_file.write(l2)
            l2=file2.readline()
        else:
            lineC1 = l1.lower()
            lineC2 = l2.lower()
            if lineC1 < lineC2:
                merged_file.write(l1)
                l1=file1.readline()
            if lineC1 > lineC2:
                merged_file.write(l2)
                l2=file2.readline()
    merged_file.close()
else:
    file1 = open(str(sys.argv[1]), 'r')
    file2 = open(str(sys.argv[2]), 'r')
    l1 = file1.readline()
    l2 = file2.readline()
    merged_file = open(str(sys.argv[3]), 'a')
    while True:
        if not l1 and not l2:
            break
        elif l1 and not l2:
            merged_file.write(l1)
            l1 = file1.readline()
        elif l2 and not l1:
            merged_file.write(l2)
            l2 = file2.readline()
        elif l1.endswith(':'):
            merged_file.write(l1)
            l1=file1.readline()
        elif l2.endswith(':'):
            merged_file.write(l2)
            l2=file2.readline()
        else:
            if l1 < l2:
                merged_file.write(l1)
                l1 = file1.readline()
            if l1 > l2:
                merged_file.write(l2)
                l2 = file2.readline()
    merged_file.close()