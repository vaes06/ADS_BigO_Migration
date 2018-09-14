import random
def LogReader():
    counter = 0
    N = 100000
    uniqueIPs = 90001
    logReader = []
    while counter < 90001:
        logReader = logReader + [counter]
        counter = counter + 1

    counter2 = 0
    while counter2 < (100000-90001):
        counter2 = counter2 + 1
        logReader = logReader + [counter2]
    return logReader

def ReadAllLogs():
    logReader =LogReader()
    linesSeen = 0
    for line in logReader:
        linesSeen = linesSeen + 1
    return linesSeen

def CountUniqueIPs():
    logReader = LogReader()
    ipsSeen = {}
    for line in logReader:
        if line not in ipsSeen:
            ipsSeen[line] = 1
    return len(ipsSeen)

print("Reading log items:")
linecount = ReadAllLogs()
print(linecount, "items read")
print("Step 2: Counting unique ips...")
ipcount = CountUniqueIPs()
print("Number of unique IPs: ", ipcount)