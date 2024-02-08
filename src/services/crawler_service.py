import platform
import subprocess
import requests
import os


class Crawler:
    def run_command(self, url):
        system = platform.system()

        self.save_files()

        command = f"{url}"
        # command = f"echo {url} | docker run --rm -i hakluke/hakrawler -subs"

        if system == "Windows":
            # Use PowerShell to execute the command
            result = subprocess.run(
                ["powershell", "-Command", command],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
            )
        else:
            # Use Bash to execute the command
            result = subprocess.run(
                command,
                shell=True,
                executable="/bin/bash",
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
            )

        # Replace '\n' with array in the result.stdout
        cleaned_stdout = self.split_stdout(result.stdout)

        # for debugging
        response_data = {
            "stdout": cleaned_stdout,
            "stderr": result.stderr,
            "returncode": result.returncode,
        }

        return response_data

    def split_stdout(self, result):
        # Split the string based on '\n'
        json_objects = result.split("\n")

        # Initialize an empty array to store the parsed JSON objects
        parsed_data = []

        # Iterate through each JSON object string, parse it, and add to the array
        for json_str in json_objects:
            if json_str.strip():  # Check if the string is not empty or just whitespace
                parsed_data.append(json_str)

        return parsed_data

    def save_files(self):
        github_repo_url = "https://github.com/bartekspitza/dotfiles"
        save_directory = "~/dotfiles"
        self.download_github_repo_contents(github_repo_url, save_directory)

    def download_file(self, url, save_path):
        response = requests.get(url)
        if response.status_code == 200:
            with open(save_path, "wb") as f:
                f.write(response.content)
            print("File downloaded successfully.")
        else:
            print("Failed to download file.")

    def download_github_repo_contents(self, repo_url, save_dir):
        api_url = repo_url.replace("github.com", "api.github.com/repos") + "/contents"
        response = requests.get(api_url)
        if response.status_code == 200:
            contents = response.json()
            if not os.path.exists(save_dir):
                os.makedirs(save_dir)
            for item in contents:
                if item["type"] == "file":
                    file_url = item["download_url"]
                    file_name = os.path.join(save_dir, item["name"])
                    self.download_file(file_url, file_name)
                elif item["type"] == "dir":
                    dir_name = os.path.join(save_dir, item["name"])
                    self.download_github_repo_contents(item["url"], dir_name)
        else:
            print("Failed to fetch repository contents.")

