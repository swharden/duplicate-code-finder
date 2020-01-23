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
    "{", "}", "}else{", "else", "else{", "break;",
    "return;", "return true;", "return false;",
    "**/", "/**", "*/", "/*", ""
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
            if not line in seenLines:
                seenLines[line] = 0
            seenLines[line] += 1
    lineCounts = sorted(seenLines.items(), key=lambda x: x[1])
    return lineCounts

def DisplayLineCounts(lineCounts):
    assert isinstance(lineCounts, dict)
    print(f"Count\tLine")
    for line, count in sortedLines:
        if line.startswith("#") or line.startswith("//"):
            continue
        if line in IGNOREDLINES or line.replace(" ", "") in IGNOREDLINES:
            continue
        if count < 5:
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
    lineCounts = CountLines(sourceCodes)
    DisplayLineCounts(lineCounts)
