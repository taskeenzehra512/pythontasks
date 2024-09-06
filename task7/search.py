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
        result = subprocess.check_output(['grep', pattern, file_path], text=True).strip()
        return result if result else f"{pattern} not found"
    except subprocess.CalledProcessError:
        return f"{pattern} not found"

def extract_info(file_path, patterns):
    """
    Extracts specific information from the file using grep.

    Args:
        file_path (str): The path to the file to be searched.
        patterns (dict): A dictionary of patterns to search for.

    Returns:
        dict: A dictionary with the extracted information.
    """
    results = {}
    for key, pattern in patterns.items():
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





if __name__ == "__main__":
    
    """
    Main function to process two files, search for keywords, 
    and write the results to a single output file.
    """
    # Define the file paths
    file1_path = '/home/emumba/Documents/pythontasks/task7/tmilt.0.231215.075551.6BT+.3FzgZTbd.log'  # Path to the first file
    file2_path = '/home/emumba/Documents/pythontasks/task7/controller.231215.075537.fpMs.8qpS7S5pG.log'  # Path to the second file
    output_file_path = '/home/emumba/Documents/pythontasks/task7/output.txt'  # Path for the output file
    
    # Define patterns for the first file
    file1_patterns = {
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
    
    # Define patterns for the second file
    file2_patterns = {
        "Start time": "Start time:",
        "Working Directory": "Working Directory:",
        "Installation location": "Installation location:",
        "Path to Log file": "Path to Log file:",
        "All Running Information": "All Running Information:",
        "All Build information": "All Build information:",
        "Ending time": "Ending time:",
        "Session Duration": "Session Duration:",
        "Fatal Count": "Fatal Count:",
        "Error Count": "Error Count:",
        "Warning Count": "Warning Count:",
        "Exit code with description": "Exit code with description:"
    }
    
    # Extract information from the first file
    results_file1 = extract_info(file1_path, file1_patterns)
    
    # Extract information from the second file
    results_file2 = extract_info(file2_path, file2_patterns)
    
    # Combine results from both files
    combined_results = {**results_file1, **results_file2}
    
    # Write the combined search results to the output file
    write_to_output(combined_results, output_file_path)


