import platform
import subprocess


class Crawler:
    def __init__(self, url):
        # You can initialize any instance variables or perform setup here
        self.system = platform.system()
        self.command = f"echo {url} | hakrawler -subs"
        # self.command = f"echo {url} | docker run --rm -i hakluke/hakrawler -subs"

    def run_command(self):
        print(self.system)

        if self.system == "Windows":
            # Use PowerShell to execute the command
            result = subprocess.run(
                ["powershell", "-Command", self.command],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
            )
        else:
            # Use Bash to execute the command
            result = subprocess.run(
                self.command,
                shell=True,
                executable="/bin/bash",
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
            )

        # Replace '\n' with array in the result.stdout
        cleaned_stdout = self._split_stdout(result.stdout)

        # for debugging
        response_data = {
            "stdout": cleaned_stdout,
            "stderr": result.stderr,
            "returncode": result.returncode,
        }

        return response_data

    def _split_stdout(self, result):
        # Split the string based on '\n'
        json_objects = result.split("\n")

        # Initialize an empty array to store the parsed JSON objects
        parsed_data = []

        # Iterate through each JSON object string, parse it, and add to the array
        for json_str in json_objects:
            if json_str.strip():  # Check if the string is not empty or just whitespace
                parsed_data.append(json_str)

        return parsed_data

