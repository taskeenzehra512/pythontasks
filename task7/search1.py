import subprocess

def search_with_grep(file_path, pattern):
    """
    Searches for a pattern in a file using grep.

    Args:
        file_path (str): The path to the file to be searched.
        pattern (str): The pattern to search for.

    Returns:
        str: The first matching line or a 'not found' message.
    """
    try:
        # Run the grep command and get the output
        result = subprocess.check_output(['grep', pattern, file_path], text=True).strip()
        return result if result else f"{pattern} not found"
        
    except subprocess.CalledProcessError:
        return f"{pattern} not found"
        
        
        

def extract_info(file_path):
    """
    Extracts specific information from the file using grep.

    Args:
        file_path (str): The path to the file to be searched.

    Returns:
        dict: A dictionary with the extracted information.
    """
    # Define patterns to search for
    search_patterns = {
        "Working dir": "Initial working dir:",
        "Installation Location": "Location of the installation:",
        "Log file Path": "This log file is:",
        "Host": "Host:",
        "Current OS": "Current OS:",
        "Uptime": "Uptime:",
        "RAM": "RAM:",
        "Build information": "Build information:",
        "Release": "Release:",
        "Build": "Build:",
        "Revision": "Revision:",
        "Sandbox": "Sandbox:",
        "MBF exec time": "MBF output generation exec time",
        "QTM exec time": "QTM exec time"
    }
    
    # Dictionary to store the results
    results = {}
    
    # Loop through each pattern and search for it using grep
    for key, pattern in search_patterns.items():
        results[key] = search_with_grep(file_path, pattern)
    
    return results
    
    
    

def write_to_output(results, output_file):
    """
    Writes the search results to an output file.

    Args:
        results (dict): A dictionary of search results.
        output_file (str): The path to the output file.
    """
    with open(output_file, 'w') as f:
        for key, value in results.items():
            f.write(f"{key}: {value}\n")
            
            
            

def main():
    """
    Main function to load the tmilt file, search for keywords, 
    and write the results to an output file.
    """
    # Define the file paths
    tmilt_file_path = '/home/emumba/Documents/pythontasks/task7/tmilt.0.231215.075551.6BT+.3FzgZTbd.log'  # Replace with your file path
    output_file_path = '/home/emumba/Documents/pythontasks/task7/output.txt'  # Path to store the results
    
    # Extract information from the file
    results = extract_info(tmilt_file_path)
    
    # Write the search results to the output file
    write_to_output(results, output_file_path)

# Call the main function when the script is run
if __name__ == "__main__":
    main()
