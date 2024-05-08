from modules.readSettings import readConfig
import os
import shutil

def moveToOutput(inputPath,folderStructure):
    """ This function is responsible for moving files to the correct location """
    
    # Check to see if it contains a given substring
    outputPath = f"{readConfig("output")}\\Temp"
    fileName = os.path.basename(inputPath)
    
    if hasOutput(folderStructure, inputPath): ## Move to the correct folder
        moveToDestination(inputPath, outputPath, fileName)
        
    else: ## Move to temp, it is the safest place where manual sorting can happen
        moveToDestination(inputPath, outputPath, fileName)
    
def hasOutput(inputPath, folderStructure):
    """ Checks to see if there is a designated output folder for this type of file """
    return False
    

def moveToDestination(source, destination, fileName):
    """ Moves file from source path to destination path """
    shutil.copyfile(f"{source}",f"{destination}\\{fileName}")