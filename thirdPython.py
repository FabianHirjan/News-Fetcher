import json


def ex1():
    with open("text.txt", "r") as f:
        lines = f.readlines()

    result = []
    for line in lines:
        for char in line:
            if char.isalpha():
                result.append(char.lower())

    frequency = {char: result.count(char) for char in set(result)}

    max_freq = max(frequency.values())
    graph_lines = []

    for i in range(max_freq, 0, -1):
        line = ""
        for char in sorted(frequency.keys()):
            if frequency[char] >= i:
                line += "o "
            else:
                line += "  "
        graph_lines.append(line)

    graph_lines.append(" ".join(sorted(frequency.keys())))

    with open("output.txt", "w") as f:
        for line in graph_lines:
            f.write(line + "\n")


def ex2(n):
    char_tuples = [(chr(i), i, 25 - (i - 65)) for i in range(65, 91)]
    print(char_tuples)




if __name__ == "__main__":
    firstHard("studenti.json")
