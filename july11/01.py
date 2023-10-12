import urllib.parse


def parse_url(url):
    parsed_url = urllib.parse.urlparse(url)
    query_params = urllib.parse.parse_qs(parsed_url.query)

    result = {
        "протокол": parsed_url.scheme,
        "доменное имя": parsed_url.netloc,
        "путь": parsed_url.path,
        "параметры запроса": query_params
    }

    return result


with open('input1.txt', 'r', encoding='utf-8') as input_file:
    url = input_file.read()

parsed_result = parse_url(url)

with open('output1.txt', 'w', encoding='utf-8') as output_file:
    output_file.write("Результат разбора:\n")
    for key, value in parsed_result.items():
        output_file.write(f" - {key}: {value}\n")



