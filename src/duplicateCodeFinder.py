import sys
import os
import glob


def showHelp(error=True):
    fileName = os.path.basename(__file__)
    if (error):
        print("ERROR: invalid arguments.")
    print(f"USAGE: python {fileName} source/code/folder/")
    if (error):
        exit()


def GetSourceFiles(folderPath):
    """Return a list of source code file paths in the folder."""
    assert os.path.isdir(folderPath)
    sourceCodeExtensions = ["C", "CPP", "CS", "PY"]
    sourceCodePaths = []
    for filePath in glob.glob(folderPath+"/*.*"):
        baseName = os.path.basename(filePath)
        extension = baseName.split(".")[-1].upper()
        if extension in sourceCodeExtensions:
            sourceCodePaths.append(filePath)
    return sourceCodePaths


def LoadSourceCode(sourceFiles):
    """Return a dictionary with file paths (key) and contents (value)."""
    assert isinstance(sourceFiles, list)
    sourceCodes = {}
    for sourceFilePath in sourceFiles:
        with open(sourceFilePath) as f:
            sourceCodes[sourceFilePath] = f.read()
    return sourceCodes


IGNOREDLINES = [
    "{", "}", "break;", "try {", "};",
    "}else{", "else", "else{", "} else", 
    "return;", "return true;", "return false;",
    "**/", "/**", "*/", "/*", "", "continue;"
]


def GetLineCounts(sourceCodes):
    """Identify unique source code lines."""
    assert isinstance(sourceCodes, dict)
    seenLines = {}
    for filePath, sourceCode in sourceCodes.items():
        baseName = os.path.basename(filePath)
        lines = sourceCode.split("\n")
        for lineNumber, line in enumerate(lines):
            line = line.strip()
            line = line.replace("\t", " ")

            # add spacing to special characters
            specialChars = list("{}'\"();=")
            for char in specialChars:
                line = line.replace(char, " " + char + " ")

            # ensure all padding is a single space
            while "  " in line:
                line = line.replace("  ", " ")

            # add padding back to some characters
            line = line.replace(" ;", ";")
            line = line.replace(" (", "(")
            line = line.replace(") ", ")")
            line = line.replace("( ", "(")
            line = line.replace(" )", ")")
            line = line.strip()

            if not line in seenLines:
                seenLines[line] = 0
            seenLines[line] += 1
    lineCounts = sorted(seenLines.items(), key=lambda x: x[1])
    return lineCounts

def DisplayLineCounts(lineCounts, minimumRepeats = 10):
    assert isinstance(lineCounts, list)
    print(f"Count\tCode")
    print("-----\t" + "-"*50)
    for line, count in lineCounts[::-1]:
        if line.startswith("#") or line.startswith("//"):
            continue
        if line in IGNOREDLINES or line.replace(" ", "") in IGNOREDLINES:
            continue
        if count < minimumRepeats:
            continue
        print(f"{count}\t{line}")


if __name__ == "__main__":

    if (len(sys.argv) != 2):
        showHelp()

    folderPath = os.path.abspath(sys.argv[1])
    if (not os.path.isdir(folderPath)):
        print("ERROR: path is not valid folder")
        print(folderPath)
        exit()
    else:
        print(f"Finding duplicate code in: {folderPath}")

    sourceFiles = GetSourceFiles(folderPath)
    sourceCodes = LoadSourceCode(sourceFiles)
    lineCounts = GetLineCounts(sourceCodes)
    DisplayLineCounts(lineCounts)
