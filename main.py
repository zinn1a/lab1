import os
import time

def show_flag():
    print("\033[41m          \033[0m")
    print("\033[7m          \033[0m")
    print("\033[44m          \033[0m")
    print()

def show_pattern():
    for _ in range(3):
        print(r"\ / \ /")
        print(r" X   X ")
        print("/ \\ / \\")
    print()

def show_animation():
    frames = [
        "O---",
        "-O--",
        "--O-",
        "---O",
        "--0-",
        "-0--",
        "0---"
    ]

    for frame in frames:
        os.system("cls" if os.name == "nt" else "clear")
        print(frame)
        time.sleep(0.6)
    print()

def analyze_sequence():
    with open("sequence.txt", "r", encoding="utf-8") as file:
        numbers = [float(line.strip()) for line in file if line.strip()]

    odd_sum = 0
    even_sum = 0

    for position, number in enumerate(numbers, start=1):
        if position % 2 == 0:
            even_sum += abs(number)
        else:
            odd_sum += abs(number)

    total = odd_sum + even_sum
    p1 = round(odd_sum / total * 100)
    p2 = 100 - p1
    c1 = f"\x1b[48;2;168;85;247m{' ' * p1}\x1b[0m"
    c2 = f"\x1b[48;2;6;182;212m{' ' * p2}\x1b[0m"
    print(c1 + c2, f"Фиолетовый - нечетные числа: {p1}%. Бирюзовый - четные числа: {p2}%")
    print(f"Сумма модулей на нечётных позициях: {odd_sum:.2f}")
    print(f"Сумма модулей на чётных позициях: {even_sum:.2f}")
    print(f"Доля нечётных позиций: {p1}%")
    print(f"Доля чётных позиций: {p2}%")
    print()

def show_graph():
    print("График y = 2x:")
    for y in range(16, -1, -1):
        row = [" "] * 9

        if y % 2 == 0:
            x = y // 2
            row[x] = "*"

        print(f"{y:2} |" + " ".join(row))

    print("   +" + "--" * 9 + "> x")
    print("    " + " ".join(str(x) for x in range(9)))


def main():
    show_animation()
    show_flag()
    show_pattern()
    analyze_sequence()
    show_graph()

if __name__ == "__main__":
    main()
