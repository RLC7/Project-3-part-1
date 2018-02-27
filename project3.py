from urllib.request import urlretrieve

URL_PATH = 'https://s3.amazonaws.com/tcmg476/http_access_log'
LOCAL_FILE = 'local_copy.log'

# Use urlretrieve() to fetch a remote copy and save into the local file path
local_file, headers = urlretrieve(URL_PATH, LOCAL_FILE)

# Alt.: supply an anonmymous callback function to print a simple progress bar to screen
#local_file, headers = urlretrieve(URL_PATH, LOCAL_FILE, lambda x,y,z: print('.', end='', flush=True))

# Alt. 2: a progress bar with reduced output (every 1000 blocks)
#local_file, headers = urlretrieve(URL_PATH, LOCAL_FILE, lambda x,y,z: print('.', end='', flush=True) if x % 100 == 0 else False)

fname = 'local_copy.log'
num_lines = 0
with open(fname, 'r') as f:
    for line in f:
        num_lines += 1
print(' ')
print("Total requests during this time period in the log:", num_lines)

file  = open('local_copy.log', 'r').read()
team1  = ('01/Jan')
count1 = file.count(team1)
print("Requests for Jan 1:", count1)

team2  = ('02/Jan')
count2 = file.count(team2)
print("Requests for Jan 2:", count2)

team3  = ('03/Jan')
count3 = file.count(team3)
print("Requests for Jan 3:", count3)

team4  = ('04/Jan')
count4 = file.count(team4)
print("Requests for Jan 4:", count4)
print("You would typically do a for loop for each month and day but I did not want to hard type the code")
#For each month
print(" ")
print("This is the amount of request for months")

team5  = ('Jan')
count5 = file.count(team5)
print("Requests for Janurary:", count5)

team6  = ('Feb')
count6 = file.count(team6)
print("Requests for February:", count6)

team7  = ('Mar')
count7 = file.count(team7)
print("Requests for March:", count7)

team8  = ('Apr')
count8 = file.count(team8)
print("Requests for April:", count8)

team9  = ('May')
count9 = file.count(team9)
print("Requests for May:", count9)

team10  = ('Jun')
count10 = file.count(team10)
print("Requests for June:", count10)

team11  = ('Jul')
count11= file.count(team11)
print("Requests for July:", count11)

team12  = ('Aug')
count12 = file.count(team12)
print("Requests for August:", count12)

team13  = ('Sep')
count13 = file.count(team13)
print("Requests for September:", count13)

team14  = ('Oct')
count14 = file.count(team14)
print("Requests for October:", count14)

team15  = ('Nov')
count15 = file.count(team15)
print("Requests for November:", count15)

team16  = ('Dec')
count16 = file.count(team16)
print("Requests for December:", count16)


print("I am sorry, this is the best I can do.")