from sys import stdout

log_silent = False


def log(*args, **kwargs):
    if not log_silent:
        kwargs['end'] = ''
        print(*args, **kwargs)
        stdout.flush()
    else:
        lognone(*args, **kwargs)


def logn(*args, **kwargs):
    if not log_silent:
        kwargs['end'] = '\n'
        print(*args, **kwargs)
        stdout.flush()
    else:
        lognone(*args, **kwargs)


def lognone(*args, **kwargs):
    pass
