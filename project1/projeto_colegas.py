import argparse
import random
import string
import time
from collections import namedtuple
from pprint import pprint

# Define o namedtuple Input
Input = namedtuple('Input', ['requested', 'received', 'duration'])

def generate_random_word(length):
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))

def main():
    parser = argparse.ArgumentParser(description='Typing Test')
    parser.add_argument('-utm', '--use_time_mode', action='store_true', help='Use time mode')
    parser.add_argument('-mv', '--max_value', type=int, required=True, help='Max duration in seconds or max number of inputs')
    parser.add_argument('-uw', '--use_words', action='store_true', help='Use word typing mode instead of single character typing')
    args = parser.parse_args()

    print("Pressione qualquer tecla para iniciar o desafio...")
    input()

    test_start = time.strftime('%c')
    test_end = ''
    test_duration = 0
    number_of_types = 0
    number_of_hits = 0
    inputs = []

    if args.use_words:
        word_length = random.randint(3, 8)
    else:
        word_length = 1

    while True:
        if args.use_words:
            random_word = generate_random_word(word_length)
        else:
            random_word = random.choice(string.ascii_lowercase)

        print(f"Digite: {random_word} (ou pressione espaço para encerrar)")

        start_time = time.time()
        user_input = input()

        if user_input == ' ':
            break

        end_time = time.time()
        duration = end_time - start_time

        input_record = Input(random_word, user_input, duration)
        inputs.append(input_record)

        if user_input == random_word:
            print("Correto!")
            number_of_hits += 1
        else:
            print("Incorreto!")

        number_of_types += 1

        if args.use_time_mode:
            test_duration = end_time - start_time
            if test_duration >= args.max_value:
                break
        else:
            if number_of_types >= args.max_value:
                break

    test_end = time.strftime('%c')

    accuracy = number_of_hits / number_of_types if number_of_types > 0 else 0

    type_average_duration = sum(input_record.duration for input_record in inputs) / number_of_types if number_of_types > 0 else 0

    type_hit_average_duration = sum(input_record.duration for input_record in inputs if input_record.requested == input_record.received and number_of_hits > 0) / number_of_hits if number_of_hits > 0 else 0

    type_miss_average_duration = sum(input_record.duration for input_record in inputs if input_record.requested != input_record.received and number_of_types - number_of_hits > 0) / (number_of_types - number_of_hits) if number_of_types - number_of_hits > 0 else 0

    result_dict = {
        'accuracy': accuracy,
        'inputs': inputs,
        'number_of_hits': number_of_hits,
        'number_of_types': number_of_types,
        'test_duration': test_duration,
        'test_end': test_end,
        'test_start': test_start,
        'type_average_duration': type_average_duration,
        'type_hit_average_duration': type_hit_average_duration,
        'type_miss_average_duration': type_miss_average_duration
    }

    pprint(result_dict)