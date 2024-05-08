import os

DEFAULT = ['Temp',['Drums', ['Kicks', 'Snares', 'Hats','Top Loops', 'Full Loops']], 'Bass',['FX',['Impacts','Glitch','Misc']],'Vocals']

def generateFolders(folderPath, folderStructure=None):
    
    if folderStructure is None:
        folderStructure = DEFAULT
    try:
        # Check if the provided path is a directory
        if not os.path.isdir(folderPath):
            print(f"Error: The provided path is not a directory. {folderPath}")
            return
        
        for subFolderName in folderStructure:
            
            if isinstance(subFolderName,str):
                newFolderPath = os.path.join(folderPath, subFolderName)
                # Create the folder
                os.mkdir(newFolderPath)
            else:
                
                if isinstance(subFolderName[0],str):
                    # Make a folder for this, then recurse down to make the sub folders
                    newFolderPath = os.path.join(folderPath, subFolderName[0])
                    os.mkdir(newFolderPath)
                    
                    generateFolders(newFolderPath, subFolderName[1])
                    
    except FileExistsError:
        print("Folders already exist, skipping step.")
        
    return folderStructure

if __name__ == "__main__":
    # Example usage:
    parentFolder = './test'

    generateFolders(parentFolder)
