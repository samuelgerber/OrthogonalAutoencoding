import os
import argparse
from subprocess import call
parser = argparse.ArgumentParser(description='Tmp')
parser.add_argument('--folders', metavar='N', type=str, nargs='*',
                   help='folders')
args = parser.parse_args()



for f in args.folders:
    print f
    for i in range(1,100) :
        try:
            #os.rename("./" + f + "/iteration-" + str(i*200) + ".pdf", "./" + f + "/iteration-{:0>5d}.pdf".format(i*200) )
            os.rename("./" + f + "/xy-iteration-" + str(i*200) + ".pdf", "./" + f + "/xy-iteration-{:0>5d}.pdf".format(i*200) )
            os.rename("./" + f + "/xz-iteration-" + str(i*200) + ".pdf", "./" + f + "/xz-iteration-{:0>5d}.pdf".format(i*200) )
        except:
            print "error"
            break
    #call(["convert", "-delay", "120", "-loop",  "0", "./" + f + "/iteration-*.pdf", "./" + f + "/animation.gif"])
    call(["convert", "-delay", "120", "-loop",  "0", "./" + f + "/xy-iteration-*.pdf", "./" + f + "/xy-animation.gif"])
    call(["convert", "-delay", "120", "-loop",  "0", "./" + f + "/xz-iteration-*.pdf", "./" + f + "/xz-animation.gif"])
