from collections import deque

def trebuchet2(inp):
    word_dict = {
        "o": ["one"],
        "t": ["two", "three"],
        "f": ["four", "five"],
        "s": ["six", "seven"],
        "e": ["eight"],
        "n": ["nine"],
    }

    str_to_number_dict = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }

    running_sum = 0

    for line in inp:
        dq = deque()
        for i in range(len(line)):
            char = line[i]
            if char.isnumeric():
                dq.append(char)

            elif char in word_dict:
                for number_in_string_form in word_dict[char]:
                    N = len(number_in_string_form)
                    # Avoids going out of bounds when checking array for number in word form
                    if i + N > len(line):
                        continue
                    str1 = line[i:i + N]
                    if str1 == number_in_string_form:
                        dq.append(str_to_number_dict[number_in_string_form])
                        i = i + N

        first_num = str(dq.popleft())
        last_num = first_num if (not dq) else str(dq.pop())
        final_num = int(first_num + last_num)
        running_sum += final_num

    return running_sum


def main():
    file1 = open("day1Trebuchet.txt", "r")
    inp = list(file1)
    for i in range(len(inp)):
        inp[i] = inp[i].strip()
    print(trebuchet2(inp))


if __name__ == "__main__":
    main()
