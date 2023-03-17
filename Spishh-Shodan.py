import shodan
import sys
import re
from itertools import cycle
import pyfiglet

def read_api_keys(filename):
    with open(filename, 'r') as file:
        api_keys = [line.strip() for line in file.readlines()]
    return api_keys

def validate_proxies(proxies):
    valid_proxies = []
    proxy_pattern = re.compile(r'^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):(\d{1,5})$')

    for proxy in proxies:
        if proxy_pattern.match(proxy):
            valid_proxies.append(proxy)
        else:
            print(f"Invalid proxy format: {proxy}")
    return valid_proxies

def read_proxies(filename):
    with open(filename, 'r') as file:
        proxies = [line.strip() for line in file.readlines()]
    return validate_proxies(proxies)

def is_ip_address(input_string):
    ip_pattern = re.compile(r'\b((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)(\.|$)){4}\b')
    return bool(ip_pattern.match(input_string))

def print_or_save_result(output, save_to_file):
    if save_to_file:
        with open('results.txt', 'a', encoding='utf-8') as file:
            file.write(output)
    else:
        print(output)

def search_shodan(query, api_key, proxy, save_to_file):
    api = shodan.Shodan(api_key, proxies={"http": proxy, "https": proxy})
    
    if is_ip_address(query):
        try:
            result = api.host(query)
            output = f"IP: {result['ip_str']}\nHostnames: {result['hostnames']}\n"
            for item in result['data']:
                output += f"Port: {item['port']}\nData: {item['data']}\n{'-' * 80}\n"
            print_or_save_result(output, save_to_file)
        except shodan.APIError as e:
            print(f"Error: {e}")
    else:
        try:
            results = api.search(query)
            output = f"Results found: {results['total']}\n"
            
            for result in results['matches']:
                output += f"IP: {result['ip_str']}\nHostname: {result.get('hostnames', [])}\n"
                output += f"Port: {result['port']}\nData: {result['data']}\n{'-' * 80}\n"
            print_or_save_result(output, save_to_file)
        except shodan.APIError as e:
            print(f"Error: {e}")

def next_or_default(cycle_iterator, default=None):
    try:
        return next(cycle_iterator)
    except StopIteration:
        return default

if __name__ == '__main__':
    title = pyfiglet.figlet_format("Spishh Shodan", font="slant")
    print(title)

    api_keys = read_api_keys('api_keys.txt')
    api_key_cycle = cycle(api_keys)
    
    proxies = read_proxies('proxies.txt')
    proxy_cycle = cycle(proxies)

    save_to_file = input("Do you want to save results to 'results.txt' (y/n)? ").lower() == 'y'
    
    while True:
        search_query = input("Enter your search query or IP address (or type 'quit' to exit): ")
        if search_query.lower() == 'quit':
            break

        print(f"Input: {search_query}")
        search_shodan(search_query, next_or_default(api_key_cycle), next_or_default(proxy_cycle), save_to_file)
