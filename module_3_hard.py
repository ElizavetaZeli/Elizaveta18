def sum_numbers_and_count_strings(data):
    total_sum = 0
    total_length = 0
    if isinstance(data, dict):
        for key, value in data.items():
            if isinstance(key, str):
                total_length += len(key)
            total_sum, count_length = sum_numbers_and_count_strings(value)
            total_length += count_length
    elif isinstance(data, list):
        for item in data:
            sum_result, length_result = sum_numbers_and_count_strings(item)
            total_sum += sum_result
            total_length += length_result
    elif isinstance(data, tuple):
        for item in data:
            sum_result, length_result = sum_numbers_and_count_strings(item)
            total_sum += sum_result
            total_length += length_result
    elif isinstance(data, str):
        total_length += len(data)
    elif isinstance(data, (int, float)):
        total_sum += data
    return total_sum, total_length
data_structure = [[1, 2, 3], {'a': 4, 'b': 5}, (6, {'cube': 7, 'drum': 8}), "Hello", ((), [{(2, 'Urban', ('Urban2', 35))}])]

total_sum, total_length = sum_numbers_and_count_strings(data_structure)
print(f"Сумма всех чисел: {total_sum}")
print(f"Сумма длин всех строк: {total_length}")
