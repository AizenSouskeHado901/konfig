def main(xi):
    o_set = set([abs(x) for x in xi if ((x > -35) ^ (x <= 51))])
    upsilon = set([6*x for x in xi if -77 < x < 41])
    e_set = set(set(upsilon) | set(o_set))

    return len(o_set) * len(e_set) + sum(e_set)


if __name__ == "__main__":
    print(main({64, 97, -95, -63, 4, 74, 14, 83, 88}))
    print(main({33, -59, -37, 41, 10, 21, -74, 59, 93, 31}))