import os
from modules.determineOutputFolder import moveToOutput
from modules.readSettings import readConfig

def processWavFiles(folderPath, folderStructure):
    contents = os.listdir(folderPath)
    for currentFile in contents:
        itemPath = os.path.join(folderPath, currentFile)
        # If the file is a .wav, then print the file path
        if os.path.isfile(itemPath) and currentFile.endswith('.wav'):
            print("Found .wav file:", itemPath)

            moveToOutput(itemPath, folderStructure)

            # Pass into the function that will place the samples into a given folder structure

