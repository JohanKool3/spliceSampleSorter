def readConfig(parameter):
    
    filePath = "config.txt"

    source_path = None
    output_path = None
    
    with open(filePath, 'r') as file: 
        for line in file:
            parts = line.strip().split('=')
            if parts[0].strip() == parameter:
                value = parts[1].strip()
                
                if parameter == 'source':
                    source_path = value[1:-1]
                elif parameter == 'output':
                    output_path = value[1:-1]
                break
    
    if parameter == 'source':
        return source_path
    elif parameter == 'output':
        return output_path
    else:
        print("Error: Invalid Settings file, check example for correct")

