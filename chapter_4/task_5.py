def decode(codes: dict, encodeed_str: str)->str:
    decode_str = ""
    code_cur = ""
    for b in encodeed_str:
        code_cur += b
        if code_cur in codes:
            decode_str += codes[code_cur]
            code_cur = ""
    return decode_str


def main():
    nl, str_bsize = map(int, input().split())
    codes_letter = dict()
    for _ in range(nl):
        l, c = input().split(": ")
        codes_letter[c] = l
    input_code = input()
    print(decode(codes_letter, input_code))


if __name__ == "__main__":
    main()