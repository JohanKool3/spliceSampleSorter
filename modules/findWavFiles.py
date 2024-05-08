import os
from modules.processWavFiles import processWavFiles

def isDirectory(folderPath) -> bool:
    """ Returns True if the given path is a Directory """
    return os.path.isdir(folderPath)

def sortWavFiles(folderPath, folderStructure):
    """ Given a folder path, locates wav files """
    if not isDirectory(folderPath):
        return
    
    directoryContents = os.listdir(folderPath)
    
    wavFilePresent = any(item.endswith('.wav') for item in directoryContents)
    
    if wavFilePresent:
        print("\n")
        print("Directory with .wav files:", folderPath)
        processWavFiles(folderPath, folderStructure)
    
    for item in directoryContents:
        itemPath = os.path.join(folderPath, item)
        
        # If it's a directory, recursively call the function to explore the directory
        if isDirectory(itemPath):
            sortWavFiles(itemPath, folderStructure)
