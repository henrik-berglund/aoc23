import requests
import sys

def download_file(day):
    url = f"https://adventofcode.com/2023/day/{day}/input"
    response = requests.get(url)

    if response.status_code == 200:
        with open(f"input_{day}.txt", "w") as file:
            file.write(response.text)
        print(f"File for Day {day} downloaded successfully.")
    else:
        print(f"Failed to download the file for Day {day}. Status Code: {response.status_code}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        try:
            day = int(sys.argv[1])
            download_file(day)
        except ValueError:
            print("Please provide a valid day number.")
    else:
        print("Please provide a day number as an argument.")
