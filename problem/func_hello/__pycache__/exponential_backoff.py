import time
attempts = 0
wait = 1
retries = 5
while attempts < retries:
    time.sleep(wait)
    wait = wait*2
    attempts = attempts +1
    print(attempts,wait)