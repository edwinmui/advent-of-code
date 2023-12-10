from collections import deque

def trebuchet(inp):
    running_sum = 0

    for line in inp:
        dq = deque()
        for char in line:
            if char.isnumeric():
                dq.append(char)
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
    print(trebuchet(inp))


if __name__ == "__main__":
    main()
