import signal, os, time

_timing = 0

def alarm_start(f):
    def _handler(signum, frame):
        f()

        global _timing
        _timing += 1
        if _timing == 3:
            _timing = 0
        signal.alarm(1)

    signal.signal(signal.SIGALRM, _handler)
    signal.alarm(1) # initial alarm

def alarm_get():
    return _timing

def alarm_end():
    signal.alarm(0)