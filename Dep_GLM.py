#gets the Open GL Math library

import GitOperations

#clones GLM
def GetDep_GLM(vendersDir):
    GitOperations.GitClone("https://github.com/g-truc/glm.git", vendersDir + "/GLM")

#gets the include directory
def GetIncludeDirectory(vendersDir):
    return vendersDir + "/GLM"