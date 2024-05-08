import os
from modules.findWavFiles import sortWavFiles
from modules.readSettings import readConfig
from modules.generateFolderStructure import generateFolders

def isDirectory(folderPath) -> bool:
    return os.path.isdir(folderPath)


SEARCHFOLDER = readConfig("source")
TARGETFOLDER = readConfig("output")
folderStructure = generateFolders(TARGETFOLDER) # Generates Folder Structure
sortWavFiles(SEARCHFOLDER, folderStructure) # Sorts Wav Files to Folder Structure

# print(f"Complete Transfer from {searchFolder} to {targetFolder}")
