entry_code = '7512'


def code_lock(pin):
    attempt = input('Provide 4-digit entry code:\n')
    while attempt != pin:
        attempt = input('Incorrect code! Please try again:\n')
    print('Entry successful')


if __name__ == '__main__':
    code_lock(entry_code)
