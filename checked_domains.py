import requests
import time

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
