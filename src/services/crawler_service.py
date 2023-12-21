import platform
import subprocess

class Crawler:
    def run_command(self, url):
        system = platform.system()
        
        command = f"echo {url} | hakrawler -subs"
        # command = f"echo {url} | docker run --rm -i hakluke/hakrawler -subs"      

        if system == 'Windows':
            # Use PowerShell to execute the command
            result = subprocess.run(["powershell", "-Command", command], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        else:
            # Use Bash to execute the command
            result = subprocess.run(command, shell=True, executable='/bin/bash', stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        # Replace '\n' with array in the result.stdout
        cleaned_stdout = self.split_stdout(result.stdout)

        # for debugging
        response_data = {
            'stdout': cleaned_stdout,
            'stderr': result.stderr,
            'returncode': result.returncode
        }
        
        return response_data
    
    def split_stdout(self, result):
        # Split the string based on '\n'
        json_objects = result.split('\n')

        # Initialize an empty array to store the parsed JSON objects
        parsed_data = []

        # Iterate through each JSON object string, parse it, and add to the array
        for json_str in json_objects:
            if json_str.strip():  # Check if the string is not empty or just whitespace
                parsed_data.append(json_str)

        return parsed_data

