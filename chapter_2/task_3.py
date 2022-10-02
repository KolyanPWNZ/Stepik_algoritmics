import time
import sys

def test_fib_mod():
    check_list = [
        { "n": 9, "m": 2, "expected": 0 },
        { "n": 10, "m": 2, "expected": 1 },
        { "n": 1025, "m": 55, "expected": 5 },
        { "n": 12589, "m": 369, "expected": 89 },
        { "n": 1598753, "m": 25897, "expected": 20305},
        { "n": 60282445765134413, "m": 2263, "expected": 974}
    ]
    # print(fib_mod(100, 4))
    for v in check_list:
        start_time = time.time()
        print("n:", v['n'], "m:", v['m'], 'expected:', v['expected'], 'result:', fib_mod(v['n'], v['m']))
        print('sec:', time.time() - start_time)


def fib_mod(n, m):
    mod_values = [0, 1]
    f1 = 0
    f2 = 1
    f = 0
    per = 2
    for v in range(2, 6*m):
        per += 1
        f = (f1 + f2) % m
        mod_values.append(f)
        if [0, 1] == mod_values[-2:]:
            return mod_values[n % (per - 2)]
        f1, f2 = f2, f
    return mod_values[-3]


def main():
    test_fib_mod()
    # n, m = map(int, input().split())
    # print(fib_mod(n, m))


if __name__ == "__main__":
    main()