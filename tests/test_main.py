import pytest
from typing import List, Tuple

def test_difference():
    numbers = [1, 2, 3, 4]
    result = [numbers[i] - numbers[i+1] for i in range(0, len(numbers), 2)]
    assert result == [-1, -1]

def test_student_info():
    names = ["Ali", "Vali"]
    scores = [90, 80]
    result = [f"{name} — {score} ball" for name, score in zip(names, scores)]
    assert result == ["Ali — 90 ball", "Vali — 80 ball"]

def test_discounted_price():
    prices = [100, 200, 300]
    discounts = [10, 20, 30]
    result = [price * (1 - discount / 100) for price, discount in zip(prices, discounts)]
    assert result == [90.0, 160.0, 210.0]

def test_coordinate_sum():
    coordinates = [(1, 2), (3, 4), (5, 6)]
    result = [x + y for x, y in coordinates]
    assert result == [3, 7, 11]

def test_string_truncate():
    strings = ["hello", "world"]
    lengths = [3, 5]
    result = [s[:length].ljust(length) for s, length in zip(strings, lengths)]
    assert result == ["hel", "worl"]

def test_person_info():
    people = [("Ali", 25), ("Vali", 30)]
    result = [f"{name} {age} yoshda" for name, age in people]
    assert result == ["Ali 25 yoshda", "Vali 30 yoshda"]

def test_area():
    lengths = [10, 20, 30]
    widths = [5, 10, 15]
    result = [length * width for length, width in zip(lengths, widths)]
    assert result == [50, 200, 450]

def test_backup_name():
    file_names = ["file1.txt", "file2.txt"]
    result = [f"{name}.bak" for name in file_names]
    assert result == ["file1.txt.bak", "file2.txt.bak"]

def test_dict_from_lists():
    keys = ["a", "b", "c"]
    values = [1, 2, 3]
    result = dict(zip(keys, values))
    assert result == {"a": 1, "b": 2, "c": 3}

def test_temperature():
    temperatures = [20, 30, 40]
    cities = ["Tashkent", "Samarkand", "Bukhara"]
    result = [f"{city}: {temp}.0 °C (Farengeyt: {(temp * 9/5) + 32:.1f} °F)" for city, temp in zip(cities, temperatures)]
    assert result == ["Tashkent: 20.0 °C (Farengeyt: 68.0 °F)", "Samarkand: 30.0 °C (Farengeyt: 86.0 °F)", "Bukhara: 40.0 °C (Farengeyt: 104.0 °F)"]

def test_average():
    nested_list = [[1, 2, 3], [4, 5], [6]]
    result = [sum(inner_list) / len(inner_list) for inner_list in nested_list]
    assert result == [2.0, 4.5, 6.0]

def test_username():
    names = ["ali", "vali"]
    result = [f"@{name}_user" for name in names]
    assert result == ["@ali_user", "@vali_user"]

def test_product():
    numbers = [1, 2, 3, 4]
    result = [(numbers[i] * numbers[i+1]) / 10 for i in range(0, len(numbers), 2)]
    assert result == [0.2, 1.2]

def test_text():
    texts = ["hello123", "world456"]
    result = ["".join(filter(str.isalpha, text)).upper() for text in texts]
    assert result == ["HELLO", "WORLD"]

def test_rgb_to_hex():
    rgb = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]
    result = [f"#{r:02x}{g:02x}{b:02x}" for r, g, b in rgb]
    assert result == ["#ff0000", "#00ff00", "#0000ff"]

def test_word_frequency():
    words = ["apple", "banana", "apple"]
    frequencies = [2, 1, 2]
    result = [f"{word} ({frequency} marta)" for word, frequency in zip(words, frequencies)]
    assert result == ["apple (2 marta)", "banana (1 marta)", "apple (2 marta)"]

def test_element_type():
    elements = [1, "hello", 2, "world"]
    result = [x**2 if isinstance(x, int) else len(x) for x in elements]
    assert result == [1, 5, 4, 5]

def test_url_protocol():
    urls = ["https://example.com", "http://example.org"]
    result = [url.split("://")[0] for url in urls]
    assert result == ["https", "http"]

def test_grade():
    scores = [90, 80, 70, 60, 50]
    result = ["A" if score >= 90 else "B" if score >= 80 else "C" if score >= 70 else "D" if score >= 60 else "F" for score in scores]
    assert result == ["A", "B", "C", "D", "F"]

def test_full_name():
    first_names = ["Ali", "Vali"]
    last_names = ["Ivanov", "Petrov"]
    result = [f"{last_name}, {first_name}" for first_name, last_name in zip(first_names, last_names)]
    assert result == ["Ivanov, Ali", "Petrov, Vali"]

def test_bmi():
    weights = [70, 80, 90]
    heights = [1.7, 1.8, 1.9]
    result = [weight / (height ** 2) for weight, height in zip(weights, heights)]
    assert result == [24.22, 24.69, 25.21]

def test_title_case():
    strings = ["hello world", "python programming"]
    result = [s.title() for s in strings]
    assert result == ["Hello World", "Python Programming"]

def test_max_element():
    nested_list = [[1, 2, 3], [4, 5], [6]]
    result = [max(inner_list) for inner_list in nested_list]
    assert result == [3, 5, 6]

def test_stock_status():
    products = ["Product1", "Product2", "Product3"]
    quantities = [5, 15, 25]
    result = ["Kam stok" if quantity < 10 else "Normal" for product, quantity in zip(products, quantities)]
    assert result == ["Kam stok", "Normal", "Normal"]

def test_sum_of_squares():
    a = [1, 2, 3]
    b = [4, 5, 6]
    result = [x**2 + y**2 for x, y in zip(a, b)]
    assert result == [17, 29, 45]

def test_domain_name():
    emails = ["example@example.com", "user@user.com"]
    result = [email.split("@")[1] for email in emails]
    assert result == ["example.com", "user.com"]

def test_digit_sum():
    numbers = [123, 456, 789]
    result = [sum(int(digit) for digit in str(number)) for number in numbers]
    assert result == [6, 15, 24]

def test_average_score():
    scores = [("Ali", 90, 80), ("Vali", 70, 60)]
    result = [(name, (score1 + score2) / 2) for name, score1, score2 in scores]
    assert result == [("Ali", 85.0), ("Vali", 65.0)]

def test_reversed_string():
    strings = ["hello", "world"]
    result = [s[::-1] + "!" for s in strings]
    assert result == ["olleh!", "dlrow!"]

def test_total_cost():
    prices = [10, 20, 30]
    quantities = [2, 3, 4]
    result = [price * quantity for price, quantity in zip(prices, quantities)]
    assert result == [20, 60, 120]

def test_clamped_number():
    numbers = [150, 50, 200]
    result = [min(100, max(0, number)) for number in numbers]
    assert result == [100, 50, 100]

def test_name_length():
    names = ["Ali", "Vali", "Alexander"]
    result = ["Qisqa ism" if len(name) < 5 else "Uzun ism" for name in names]
    assert result == ["Qisqa ism", "Qisqa ism", "Uzun ism"]

def test_circle_area():
    radii = [5, 10, 15]
    result = [3.14 * radius ** 2 for radius in radii]
    assert result == [78.5, 314.0, 706.5]

def test_space_count():
    texts = ["hello world", "python programming"]
    result = [text.count(" ") for text in texts]
    assert result == [1, 1]

def test_year_event():
    years = [2020, 2021, 2022]
    events = ["Event1", "Event2", "Event3"]
    result = [f"{year} — {event}" for year, event in zip(years, events)]
    assert result == ["2020 — Event1", "2021 — Event2", "2022 — Event3"]

def test_binary_number():
    numbers = [10, 20, 30]
    result = [bin(number)[2:] for number in numbers]
    assert result == ["1010", "10100", "11110"]

def test_name_age():
    people = [{"name": "Ali", "age": 25}, {"name": "Vali", "age": 30}]
    result = [(person["name"], person["age"]) for person in people]
    assert result == [("Ali", 25), ("Vali", 30)]

def test_vowel_replacement():
    strings = ["hello", "world"]
    result = ["".join("*" if char in "aeiou" else char for char in s) for s in strings]
    assert result == ["h*ll*", "w*rld"]

def test_power():
    numbers = [2, 3, 4]
    powers = [2, 3, 4]
    result = [number ** power for number, power in zip(numbers, powers)]
    assert result == [4, 27, 256]

def test_file_name():
    file_paths = ["/path/to/file1.txt", "/path/to/file2.txt"]
    result = [path.split("/")[-1] for path in file_paths]
    assert result == ["file1.txt", "file2.txt"]

def test_normalized_score():
    scores = [90, 80, 70]
    result = [score / 10 for score in scores]
    assert result == [9.0, 8.0, 7.0]

def test_title():
    names = ["Ali", "Vali"]
    genders = ["male", "female"]
    result = [f"Mr. {name}" if gender == "male" else f"Ms. {name}" for name, gender in zip(names, genders)]
    assert result == ["Mr. Ali", "Ms. Vali"]

def test_product_of_tuple():
    tuples = [(1, 2, 3), (4, 5, 6)]
    result = [t[0] * t[1] * t[2] for t in tuples]
    assert result == [6, 120]

def test_text_length():
    texts = ["hello", "world", "this is a long text"]
    result = ["Qisqa" if len(text.split()) < 3 else "O‘rta" if len(text.split()) < 6 else "Uzun" for text in texts]
    assert result == ["Qisqa", "Qisqa", "Uzun"]

def test_gcd():
    a = [12, 24, 36]
    b = [15, 30, 45]
    result = [gcd(x, y) for x, y in zip(a, b)]
    assert result == [3, 6, 9]

def test_color():
    colors = ["red", "green", "blue"]
    rgb = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]
    result = [f"{color}: {r},{g},{b}" for color, (r, g, b) in zip(colors, rgb)]
    assert result == ["red: 255,0,0", "green: 0,255,0", "blue: 0,0,255"]

def test_nearest_odd():
    numbers = [10, 20, 30]
    result = [number if number % 2 != 0 else number + 1 for number in numbers]
    assert result == [11, 21, 31]

def test_unicode_code():
    strings = ["hello", "world"]
    result = [ord(char) for s in strings for char in s]
    assert result == [104, 101, 108, 108, 111, 119, 111, 114, 108, 100]

def test_duration():
    start_times = [10, 20, 30]
    end_times = [15, 25, 35]
    result = [end - start for start, end in zip(start_times, end_times)]
    assert result == [5, 5, 5]

def test_user_info():
    users = [["Ali", "Ivanov", 25], ["Vali", "Petrov", 30]]
    result = [f"{last_name} {first_name} — {age} yosh" for first_name, last_name, age in users]
    assert result == ["Ivanov Ali — 25 yosh", "Petrov Vali — 30 yosh"]

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
