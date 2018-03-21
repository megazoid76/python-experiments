
def reverse(s):
    for l in s[::-1]:
        print(l)


def reverse_1(s):
    rl = ''
    for l in s[::-1]:
        rl = rl + l
    return rl


# if __name__ == '__main__':
s = "qwerty"
print(reverse_1(s))

print("reverse of " + s + " is " + reverse_1(s))
