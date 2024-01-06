# Функция для применения P-блока к входному тексту
def apply_p_box(input_text, p_box):
    return ''.join(input_text[i - 1] for i in p_box)  # Применение P-блока: выбор битов согласно таблице перестановки

# Функция для генерации раундовых ключей
def generate_round_keys(key):
    # Генерация двух раундовых ключей
    round_keys = []
    for i in range(2):
        key = key[1:] + key[0]  # Циклический сдвиг бит ключа
        round_keys.append(key)
    return round_keys

# Функция для применения S-блока к входному тексту
def apply_s_box(input_text, s_box):
    # Вычисление индексов строки и столбца в S-блоке
    row = int(input_text[0] + input_text[3], 2)
    col = int(input_text[1:3], 2)
    # Возвращение результата S-блока в двоичной форме
    return format(s_box[row][col], '02b')

# Основная функция для упрощенной версии DES
def des_simplified(plaintext, key, num_rounds=2):
    # Исходные таблицы для S-блоков и P-блока
    s_box = [
        [1, 0, 3, 2],
        [3, 2, 1, 0],
        [0, 2, 1, 3],
        [3, 1, 3, 2]
    ]
    p_box = [2, 4, 3, 1]

    # Генерация раундовых ключей
    round_keys = generate_round_keys(key)

    # Итерация по раундам
    for round_num in range(num_rounds):
        # Вывод текущего раундового ключа
        print(f"Round {round_num + 1} Key: {round_keys[round_num]}")

        # Раундовая функция
        expanded_text = plaintext[1:] + plaintext[0]  # Циклический сдвиг бит входного текста
        xor_result = bin(int(expanded_text, 2) ^ int(round_keys[round_num], 2))[2:].zfill(4)  # XOR с раундовым ключом
        s_box_result = apply_s_box(xor_result, s_box)  # Применение S-блока
        p_box_result = apply_p_box(s_box_result.zfill(4), p_box)  # Применение P-блока
        round_result = bin(int(plaintext, 2) ^ int(p_box_result, 2))[2:].zfill(4)  # Обновление входного текста

        # Вывод промежуточных результатов для текущего раунда
        print(f"Expanded Text: {expanded_text}")
        print(f"XOR Result: {xor_result}")
        print(f"S-Box Result: {s_box_result}")
        print(f"P-Box Result: {p_box_result}")
        print(f"Round {round_num + 1} Result: {round_result}")

        # Обновление для следующего раунда
        plaintext = round_result

    # Вывод окончательного зашифрованного текста
    print(f"Final Cipher: {round_result}")

# Пример использования
plaintext = "11011011"
key = "1011101101"
# Вызов функции с двумя раундами
des_simplified(plaintext, key, num_rounds=2)
