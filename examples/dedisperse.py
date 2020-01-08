from sys import argv
from sigpyproc.Readers import FilReader
fil = FilReader(argv[1])
tim = fil.dedisperse(float(argv[2])).toFile("{0}_DM{1}.tim".format(fil.header.basename,argv[2]))
