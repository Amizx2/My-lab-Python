numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
missing_value = 4
numbers_dsa = numbers[:missing_value] + numbers[missing_value+1:]
total_sum = sum(numbers_dsa)
average_value = total_sum / len(numbers)
numbers[missing_value] = average_value
print("Измененный список:", numbers)
