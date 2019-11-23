def constructCompileStatement(target, language, fileName):
    
    command = determineCompiler(target, language) + determineTarget(target)
    staticLinkParam = determineStaticLibraryLink(target, language)

    outputFileName = fileName
    outputFileName = outputFileName.strip("." + language)

    removeCommand = "rm -rf " + fileName

    return (str(command + " " + fileName + " -o " + outputFileName).strip(), removeCommand.strip())

def constructInterpretStatement(language, fileName):

    command = determineInterpreter(language);
    removeCommand = "rm " + fileName

    #Not sure if we should be using the booleanity (?) of python. 
    #But if the language isnt on the approved list, this should prevent that from happening.
    #Ignore the lisp-like nature of the tuple below. It doesn't exist if you can't see it, right?
    return (str((command if not command else "") + " " + fileName).strip(), removeCommand.strip())

def determineCompiler(target, language):

    if (language == "cpp") and ("win" in target):
        return "g++-mingw-"

    elif (language == "c") and ("win" in target):
        return "gcc-mingw-"

    elif (language == "cpp") and ("linux" in target):
        return "g++"

    elif (language == "c") and ("linux" in target):
        return "gcc"
    
    else:
        return ""

def determineInterpreter(language):
    if language == "py":
        return "python3 -u"

    elif language == "rb":
        return "ruby"

    else: 
        return ""

def determineTarget(target):

    if target == "win64":
        return "w64-x86-64"

    elif target == "win32":
        return "w64-i686"

    else:
        return ""

def determineStaticLibraryLink(target, language):
    if target == "linux":
        return ""

    if language == "cpp":
        return "-static-libstdc++"
    
    elif language == "c":
        return "-static-libstdc"
    
    else:
        return ""