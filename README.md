![DALL·E 2023-03-17 02](https://user-images.githubusercontent.com/87335420/226064489-aa81fa26-95d9-4fdb-a988-fe44345e2247.png)

# Spishh Shodan

Spishh Shodan is a Python script that allows users to search Shodan more efficiently. With support for multiple API keys, IP address and search query searches, and the ability to save results to a file or display them in the terminal, Spishh Shodan aims to enhance the user's experience when interacting with the Shodan API. <- lol

## Features

- Search for IP addresses or search queries
- Support for multiple Shodan API keys
- Automatic proxy rotation for each search query (using a list of proxies provided in a text file)
- Save search results to a file or display them in the terminal

## Prerequisites

- Python 3.x
- Shodan Python library

## Installation

1. Clone the repository or download the script.
2. Install the required dependencies using pip:

```bash
pip install -r requirements.txt
```
## Usage

1. Add your Shodan API keys to the `api_keys.txt` file, one key per line.
2. (Optional) Add your proxy list to the `proxies.txt` file, one proxy per line in the format `IP:PORT`.
3. Run the script:

```bash
python Spishh_Shodan.py
```
## Disclaimer
Please ensure you follow Shodan's API usage policy while using this script. This script is for educational purposes only. The author is not responsible for any misuse or consequences resulting from the use of this script.

## License
This project is licensed under the MIT License - see the MIT-LICENSE.txt file for details.
