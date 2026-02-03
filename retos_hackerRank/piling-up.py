import sys


def can_stack(blocks: list[int]) -> str:
    left, right = 0, len(blocks) - 1
    top = float("inf")

    while left <= right:
        a = blocks[left]
        b = blocks[right]
        pick = a if a >= b else b

        if pick > top:
            pick = b if pick == a else a
            if pick > top:
                return "No"

        top = pick

        if pick == a:
            left += 1
        else:
            right -= 1

    return "Yes"


def main() -> None:
    data = sys.stdin.buffer.read().split()
    it = iter(data)

    t = int(next(it))
    out = []

    for _ in range(t):
        n = int(next(it))
        blocks = [int(next(it)) for _ in range(n)]
        out.append(can_stack(blocks))

    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()