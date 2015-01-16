def find_large_pal():
    large_pal = 0
    for i in range(100, 1000):
        for j in range(100, 1000):
            number = i * j
            if str(number)[::-1] == str(number) and large_pal < number:
                large_pal = number
    return large_pal

if __name__ == "__main__":
    print find_large_pal()def find_smallest_multiple():
    tester = 20
    while True:
        important_var = False
        for i in range(1, 21):
            if tester % i != 0:
                important_var = True
                break
        if important_var:
            tester += 20
        else:
            return tester

