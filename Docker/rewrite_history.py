import sys, getopt

def rewrite_histfile(inputfile, outputfile):

    header_fields = ["IMAGE", "CREATED", "CREATED BY", "SIZE", "COMMENT"]

    file = open(inputfile)
    file = open("build_history.txt")
    line1 = file.readline()

    split_col = list()
    for item in header_fields:
        col_num = line1.find(item)
        print(line1.find(item))
        split_col.append(col_num)

    print(split_col)
    file.close()

    file = open(inputfile)
    outfile = open(outputfile, 'w')
    for lines in file:
        outstr = ""
        for i in range(0, len(split_col)):
            # print(i,end="")
            if i < len(split_col) - 1:
                # print(split_col[i],split_col[i+1])
                outstr = outstr + lines[split_col[i]:split_col[i + 1]] + ","
            else:
                # print(split_col[i])
                outstr = outstr + lines[split_col[i]:]
        outfile.write(outstr)

    file.close()
    outfile.close()
    print("Output is in file: ", outputfile)

def main(argv):
    inputfile = "build_history.txt"
    outputfile = 'out.csv'
    try:
        opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
    except getopt.GetoptError:
        print('rewrite_history.py -i <inputfile> -o <outputfile>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('rewrite_history.py -i <inputfile> -o <outputfile>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg
    print('Input file is ', inputfile)
    print('Output file is ', outputfile)

    rewrite_histfile(inputfile, outputfile)

if __name__ == "__main__":
    print('Number of arguments:', len(sys.argv), 'arguments.')
    print('Argument List:', str(sys.argv))
    main(sys.argv[1:])
