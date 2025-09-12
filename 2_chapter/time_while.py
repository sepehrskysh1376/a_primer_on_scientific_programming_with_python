import time
t0 = time.time()
while time.time() - t0 < 10:
    print(t0)
    print(time.time())
    print("... I like while loops!")
    time.sleep(2)
print("Oh, no - the loop is over.")


t0 = time.time()
while time.time() - t0 > 10:
    print(t0)
    print(time.time())
    print("... I like while loops!")
    time.sleep(2)
print("Oh, no - the loop is over.")
