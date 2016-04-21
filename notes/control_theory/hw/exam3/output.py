import sys

stdout_initial = sys.stdout


def write_output(prob, out, number):
    header1 = "="*80 + "\n\nCode for Problem %d\n\n" % number + "="*80 + "\n\n"
    header2 = "\n" + "="*80 + "\n\nOutput for Problem %d" % number + "\n\n" + \
        "="*80 + "\n\n"
    out.write(header1)

    f = open(prob, "r")
    out.write(f.read())
    f.close()

    out.write(header2)
    sys.stdout = out
    __import__(prob.strip(".py"))
    sys.stdout = stdout_initial


f1 = "e3prob1.py"
o1 = open("e3prob1out.txt", "w")

write_output(f1, o1, 1)

f3 = "e3prob3.py"
o3 = open("e3prob3out.txt", "w")

write_output(f3, o3, 3)

f4 = "e3prob4.py"
o4 = open("e3prob4out.txt", "w")

write_output(f4, o4, 4)

f5 = "e3prob5.py"
o5 = open("e3prob5out.txt", "w")

write_output(f5, o5, 5)

o1.close()
o3.close()
o4.close()
o5.close()
