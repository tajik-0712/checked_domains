import requests
import time

def draw_text(text):
    font = {
        'a': [
            '000',
            '000',
            '000',
            '000',
            '000',
        ],
        'c': ["1111",
                "1000",
                "1000",
                "1000",
                "1111"],
        'h': ["1001",
                "1001",
                "1111",
                "1001",
                "1001"],
        'e': ["1111",
                "1000",
                "1111",
                "1000",
                "1111"],
        'k': ["1001",
                "1010",
                "1100",
                "1010",
                "1001"],
        'd': ["1110",
                "1001",
                "1001",
                "1001",
                "1110"],
        'o': ["1111",
                "1001",
                "1001",
                "1001",
                "1111"],
        'm': ["10001",
                "11011",
                "10101",
                "10001",
                "10001"],
        'a': ["0110",
                "1001",
                "1111",
                "1001",
                "1001"],
        'i': ["111",
                "010",
                "010",
                "010",
                "111"],
        'n': ["1110",
                "1001",
                "1001",
                "1001",
                "1001"],
        's': ["0111",
                "1000",
                "0111",
                "0001",
                "1110"], 
        'd': [
            "1110",
            "1001",
            "1001",
            "1001",
            "1110"],
        'o': ["0110",
            "1001",
            "1001",
            "1001",
            "0110",
            ],
        'm': [ "10001",
            "11011",
            "10101",
            "10001",
            "10001"],
        'a': ["0110",
            "1001",
            "1111",
            "1001",
            "1001"],
        'i': ["111",
            "010",
            "010",
            "010",
            "111"],
        'n': [
            "1110",
            "1001",
            "1001",
            "1001",
            "1001"],
        's': ["0111",
            "1000",
            "0111",
            "0001",
            "1110"],
    }
    
    height = 5
    
    lines = [""] * height

    for char in text:
        if char in font:
            char_lines = font[char]
            for i in range(height):
                lines[i] += char_lines[i] + " "

    for line in lines:
        print(line.replace('1', '⬜').replace('0', ' '))



def check_domain_availability(site_name):
    domain_suffixes = [
        ".com", ".org", ".net", ".edu", ".gov", ".mil",
        ".info", ".biz", ".co", ".us", ".uk", ".de", ".cn", ".jp",
        ".fr", ".au", ".ca", ".in", ".ru", ".br", ".it", ".tj",
    ]

    available_domains = []
    checked_domains = []  

    start_time = time.time()

    for suffix in domain_suffixes:
        url = f"http://{site_name}{suffix}"
        checked_domains.append(url)
        print('  |' f" Проверка домена: | {url} |") 
        try:
            response = requests.get(url)
            if response.status_code == 200:
                available_domains.append(url)
        except requests.ConnectionError:
            continue

    end_time = time.time()
    work_time = end_time - start_time

    return available_domains, work_time, checked_domains
print('-' * 50)
draw_text("checked")
print('-' * 50)
site_name = input('  | Какой сайт хотите искать?: ')

domains, work_time, checked_domains = check_domain_availability(site_name)

if domains:
    print('-' * 50)
    print("  | Найденные домены: ")
    for domain in domains:
        print('  |', f'{domain} |')
else:
    print('-' * 50)
    print("  | Сайт с таким именем не найден. |")

print('-' * 50)
print(f'  | Время поиска: {work_time:.2f} секунд |')
