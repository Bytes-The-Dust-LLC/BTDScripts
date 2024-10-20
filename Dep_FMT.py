#gets the FMT logging library

import GitOperations

#clones FMT
def GetDep_FMT(vendersDir):
    GitOperations.GitClone("https://github.com/fmtlib/fmt.git", vendersDir + "/FMT")

#gets the include directory
def GetIncludeDirectory(vendersDir):
    return vendersDir + "/FMT/include"