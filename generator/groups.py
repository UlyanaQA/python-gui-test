from comtypes.client import CreateObject
import getopt
import string
import random
import sys
import os

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 10
f = "groups.xlsx"

for opt, val in opts:
    if opt == "-n":
        n = int(val)
    elif opt == "-f":
        f = val


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits #+ string.punctuation + " " * 10
    return prefix + ''.join([random.choice(symbols) for i in range(random.randrange(maxlen))])


project_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

xl = CreateObject("Excel.Application")
xl.Visible = 1
wb = xl.Workbooks.Add()
xl.Range["A1"].Value[()] = "Random_groups"
for i in range(10):
    xl.Range["A%s" % (i + 2)].Value[()] = random_string("group", 10)
wb.SaveAs(os.path.join(project_dir, "groups.xlsx"))
xl.Quit()
