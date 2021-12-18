
from replit import db
import glob
from secrets import token_hex
from datetime import datetime
import time
import getpass
#import json
from random import randrange
#import hashlib
#import Crypto
#import cryptography
#import databases
import os
#from playsound import playsound
#import os.path
#importing colorama###
###connector socket###
port = 443
mode = "peer-to-peer"
server_status = "down"


# settings.py

#secret_token = os.getenv("q")

#if secret_token:
#  print("The secret TOKEN is:", secret_token)
#else:
#  print("Looks like you're not the owner")





global username
#########PRIVATE KEY GENERATOR##############

Put = open("where_to_start.txt")
# read the content of the file opened
content = Put.readlines()

t2 = int(content[1])

t1 = int(content[0])

Put.close()
t1 = ""
t2 = ""

#print(db)

"""

f = open("passwords.txt", "r")
passwords = f.readlines()
f.close()
db["passwords"] = passwords
"""
"""
db["keys"] = {}

for i in db["passwords"]:
    db["keys"][i] = i
"""
# okay, so what you're going to want to do is add RSA encryption. passwords and shit? useless. you want a public key and private key, named for reasons that are obvious. don't share ur private key, but you recieve coins from your public key. your public key IS your username, and also can be used to verify sending transactions. signing and verifying is functions of the message and public and private keys.

#tldr research RSA encryption

#https://bitcoin.org/bitcoin.pdf could be useful

#pickle file

###connecting to database to retrive encrypted private and public keys###

block_chain = []

###ADDING STUFF###

#men_coin_amount = 0

#################
# @2021 Om Silwal
# @2021 PDN
# @2021 garrison Better than you
# @2021 javi d funk
# @2021 ethan lee
# @2021 Matthew S.
# @2021 jiyoon chang
# @2021 Jacob Bolling
#################
# is this the list of the people who are ded
####list to string###

###list to string###

###webserver for keys###

#it will show global transactions, when pineapplecoin is added, subtracted or bought. Yeee
############################

#dir_path = os.path.dirname(os.path.realpath(__file__))

#print(str3.decode("UTF-32"))






#you can help in any way
#also we are trying to make a website i can send you    #are you gonna send it to me on email @OmSilwal


def get_men_coin_in_file():
    # open file in read mode
    with open("wallets/" + username + ".txt", 'r') as f:

        # store content of the file in a variable
        text = f.readlines()

    # using list comp
    num_pineapplecoin = 0
    checked_pineapplecoin = []
    for i in text:
        if len(i) == 65 and i.startswith("0000"):
            if i in checked_pineapplecoin:
                print("how do u have 2 pineapplecoin with the same hash lol")
                print("fixing your file...")
                with open("wallets/" + username + ".txt", 'w') as f:
                    text = list(set(text))
                    for i in text:
                        f.write(i)
                exit()
            num_pineapplecoin += 1
        checked_pineapplecoin.append(i)
    return num_pineapplecoin


def send(num_pineapplecoin, from_who, to_who):
    print("sending pineapplecoin...")
    file2 = open("wallets/" + to_who + ".txt", "a")
    with open("wallets/" + from_who + ".txt", "r+") as f:
        d = f.readlines()
        f.seek(0)
        pineapplecoin_indexes = [
            index for index, val in enumerate(d)
            if len(val) == 65 and val.startswith("0000")
        ]
        if len(pineapplecoin_indexes) < num_pineapplecoin:
            if from_who == username:
                print("you don't have enough pineapplecoin!")
            else:
                print(f"{from_who} doesn't have enough pineapplecoin!")
            exit()
        else:
            last_pineapplecoin_index = pineapplecoin_indexes[-num_pineapplecoin]
        for i in d[:last_pineapplecoin_index]:
            f.write(i)
        print(d[last_pineapplecoin_index:])
        f.truncate()
    #start placeholder
    print(list(range(last_pineapplecoin_index, len(d))))
    #end placeholder
    file2.write("\n".join(d[last_pineapplecoin_index:]))
    file2.close()
    with open("buy_sell_log.txt", "r") as f:
        debts_raw = f.readlines()
        debts = []
        for i in debts_raw:
            splitted = i.split(" ")
            debts.append([splitted[0], splitted[2], int(splitted[3])])
        for i in debts:
            if from_who == i[1] and to_who == i[0]:
                debt_val = i
                debt_index = debts.index(i)
                break
            elif from_who == i[0] and to_who == i[1]:
                debt_val = i
                debt_val[2] *= -1
                debt_index = debts.index(i)
                break
        try:
            debt_val
            debt_index
        except:
            debt_val = [username, from_who, 0]
            debt_index = None
    with open("buy_sell_log.txt", "w") as f:
        for i, v in enumerate(debts_raw):
            if i != debt_index:
                f.write(v)
            else:
                debt_amt = debt_val[2] + num_pineapplecoin
                print(debt_amt)
                print(debt_val[2], num_pineapplecoin)
                if debt_amt == 0:
                    pass
                else:
                    f.write(f"{to_who} owes {from_who} {debt_amt} pineapplecoin\n")
        if debt_index == None:
            f.write(f"{username} owes {from_who} {num_pineapplecoin} pineapplecoin\n")


def record(data):
    with open("block_chain_value.txt", "a") as f:
        current_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        f.write(data + f" ({current_time})\n")




#def keygenerator(byte_amount):
    #print(token_hex(nbytes=byte_amount))


account_option = input("Do you want to login or make an account>> ").lower()

if account_option == "login":

    username = getpass.getpass(prompt='private key (invisible): ')
    
    if username == 'coin':
      print("wtf stop stealing our PINEAPPLECOIN")
      exit()
    
    elif username == 'hi':
      private = getpass.getpass(prompt='private key (invisible): ')
      if private == 'wasd':
      
      



    
    
        
      
        with open('passwords.txt') as f:
          contents = f.read()
      

        
    #print(contents)

    if username + "\n" in contents:
        print("welcome back, " + username)
        for i in glob.glob("wallets/" + username + ".txt"):
            if i == "wallets/" + username + ".txt":
                pineapplecoin_from_session = 0
                pineapplecoin_total = get_men_coin_in_file()
                record(f"{username} has logged into their account.")
                print("\nwallet found!")
                print("your wallet has " + str(pineapplecoin_total) + " pineapplecoin!\n")
            else:
                print("\nwallet not found")
                exit()

    else:
        print("not an account sucks to suck")
        exit()

elif account_option == "account":
    print("---------------------------")
    print("choose a password ")
    print("---------------------------\n")
    accounter = input("password>> ")


    # checking condition for string found or not
    #if accounter in db["passwords"]:
        #print('password taken')
        #exit()
    if True:#else:
        print("\npassword updated\n")
        # closing a file
        db["passwords"].append(accounter)
        f = open("passwords.txt", "a")
        f.write(accounter)
        f.close()
        mywallet = open("wallets/" + accounter + ".txt", "x")
        mywallet.close()
        pineapplecoin_from_session = 0
        pineapplecoin_total = 0
        username = accounter
else:
    print("not a valid answer")
    exit()

mine_trade_buy_sell = input("mine, trade, buy or sell>  ").lower()
if mine_trade_buy_sell == 'mine':
    while True:
        random_nonce_bool = input("random nonce values? y n >> ").lower()
        if random_nonce_bool in {"yes", "y"}:
            random_nonce = True
            break
        elif random_nonce_bool in {'no', 'n'}:
            random_nonce = False
            break
        else:
            print("\ninvalid answer")
elif mine_trade_buy_sell == 'trade':
    print("\nin progress")
    print("send to which user: ")
    #finally something having to do with PK+SK encryption
    public_key_send = input("user public key>> ")
    file1 = open("passwords.txt", "r")

    # read file content
    readfile = file1.read()

    # close file
    file1.close()

    # checking condition for string found or not
    if public_key_send in readfile:

        # placeholder until om makes it better
        try:
            num_send = int(input("how many pineapplecoin would you like to send?>>"))
        except:
            print("your answer wasn't a number.")
            exit()
        send(num_send, username, public_key_send)
        record(f"{username} sent {str(num_send)} pineapplecoin to {public_key_send}")
    else:
        print("that account doesn't exist!")

    print(" ")
    print("pineapplecoin SENT")
    print(" ")
    exit()

elif mine_trade_buy_sell == 'buy':
    with open("market.txt", "r+") as f:
        d = f.readlines()
        print("sell offers:\n" + "".join(d))
        buy_order = input("which offer would you like to buy? (ENTER ID)>>")
        f.seek(0)
        order_index = [
            index for index, val in enumerate(d)
            if val.split(" ")[-1] in {buy_order, buy_order + "\n"}
        ]
        if len(order_index) == 1:
            order_index = order_index[0]
            order = d[order_index].split(" ")
        else:
            print("that's not a valid id!")
            exit()
        order_info = {}
        for i, v in enumerate(order[::2]):
            order_info[v] = order[i * 2 + 1]
        for i, v in enumerate(d):
            if i != order_index:
                f.write(v)
        f.truncate()
    send(int(order_info["amount:"][:-1]), order_info["seller:"][:-1], username)

    record(f"order with id {buy_order} was bought by {username}")
    print("transaction verified")
    exit()

elif mine_trade_buy_sell == 'sell':
    print("\nin progress")

    file1 = open("market.txt", "a")

    # read file content
    amt = input("how many pineapplecoin do you want to sell?>>")
    try:
        amt = int(amt)
    except:
        
    	order_id = token_hex(nbytes=2)
    file1.write(f"amount: {amt}, seller: {username}, ID: {order_id}")
    # close file
    file1.close()
    record(
        f"{username} put up a sell offer for {amt} pineapplecoin with an id of {order_id}"
    )
    print("pineapplecoin sell order put up")
    exit()
# opening a text file

#block chain thing # block chain thing # block chain thing # block chain thing#


def add_value(transaction_amount, last_transaction=[1]):
    block_chain.append([last_transaction, transaction_amount])


q = input("how many hashes would you like to check ?>> ")
add_value(q)
print()

if q in {'sleep', 'infinite'}:

    print("------------------------")
    print("sleep_mining")
    print("WARNING PROLLY NOT TO GOOD 4 COMPUTER")
    print("------------------------")
    q = 10000**10000

vb = input("how much would you like to try and earn?>> ")
print("\n-----------------------")
if vb == 'sleep' 'infinite':
    print("------------------------")
    print("still_sleep_mining")
    print("WARNING STILL PROLLY NOT TO GOOD 4 COMPUTER")
    print("------------------------")
    vb = q

print("------------------")
print("blockchain: " + str(block_chain))
print("------------------")

if mine_trade_buy_sell == "afk":
    record(f"{username} went afk with {pineapplecoin_total} pineapplecoin.")
elif mine_trade_buy_sell == "mine":
    record(f"{username} started mining with {pineapplecoin_total} pineapplecoin.")

#wait noo that doesn't work
#dang :(
#list to string i tink, but why cant it write lists :(
#it should work https://www.w3schools.com/python/ref_file_writelines.asp
#but it doesn't lol


class pineapplecoin:
    def __init__(self, previous_chain, transaction_list):
        self.previous_chain = previous_chain
        self.transaction_list = transaction_list

        self.block_data = "-".join(transaction_list) + "-" + previous_chain
        self.block_hash = token_hex(nbytes=32)

    #def __str__(self):
    #  return "{}{}{}".format(self.previous_chain.hexdigest(),
    #               self.block_data, t1, t2)


time_started_mining = time.time()
for i in range(int(q)):
    start_time = time.time()

    initial_block = pineapplecoin("Initial String", [str(t1), str(t2)])

    if initial_block.block_hash.startswith("0000"):
        # opening a text file
        file1 = open("wallets/" + username + ".txt")
        # read file content
        readfile = file1.read()

        # checking condition for string found or not
        if not initial_block.block_hash in readfile:
            # play sound
            print('\a' * 500000000000000000000000000)
            print("-----------------")
            print("pineapplecoin found")
            print("you now have " + str(pineapplecoin_total) + " pineapplecoin")
            print("very nice kepp grinding tho")
            print("-----------------")
            pineapplecoin_from_session += 1
            pineapplecoin_total += 1
            p = open("wallets/" + username + ".txt", 'a')
            e = open("where_to_start.txt", "w")
            lines = [str(t1) + "\n", str(t2)]
            e.writelines(lines)
            p.write(str(initial_block.block_hash) + "\n")
            p.close()
            f = open("where_to_start.txt", "w")
            f.write(str(t1) + "\n")
            f.write(str(t2) + "\n")
            ##################################
            #write to global transaction file#
            record(username + " mined 1 pineapplecoin!")
            #################################
            f.close()
            print("\npineapplecoin REPORT:")
            print("---------------")
            print("scanned: " + str(q) + " hashes for pineapplecoin")
            print("found: " + str(pineapplecoin_from_session) + " pineapplecoin this run")
            print("the block chain is now: " + str(block_chain))
            print("\nblockchain info\n")
            print("Hash: \t\t" + initial_block.block_hash)
            print("nonce: \t\t" + str(t1) + str(t1))

            if pineapplecoin_from_session == vb:
                break
        # closing a file
        file1.close()

        #break

        #if found == False:
        #print("_________________________________")
        #print("NO pineapplecoin FOUND, KEEP TRYING")
        #print("_________________________________")
    if random_nonce_bool == False:
        t1 += 1
        t2 += 1
    else:
        t1 = randrange(0, 16**64)
        t2 = randrange(0, 16**64)
    _ = os.system('clear')
    print("public key: " + username)
    print("hashes checked: " + str(i + 1))
    print("pineapplecoin found in this run: " + str(pineapplecoin_from_session))
    print("your pineapplecoin: " + str(pineapplecoin_total))
    print()
    #time.sleep(1.5)
    print("-"*50)
    #real fps counter

    print("the hash is: " + initial_block.block_hash)
    print("the nonce value is: " + str(t1))
    print("hashes checked per second is: " + str(1.0 /
                                                 (time.time() - start_time)))
    print("the time since you started mining is: " +
          str(time.time() - time_started_mining))
    print("-"*50)

print("\n" * 3)
print("pineapplecoin MINING STOPPED")
print("----------------------\n")
print("pineapplecoin REPORT:")
print("---------------")
print("scanned: " + str(q) + " hashes for pineapplecoin")
print("found: " + str(pineapplecoin_total) + " pineapplecoin this run  ")
print("the block chain is now: " + str(block_chain))
print("\nblockchain info")
print("\nnonce: \t\t" + str(t1))
record(f"{username} stopped mining. They now have {pineapplecoin_total} pineapplecoin.")




"""
def __init___(new_func) {
  print("PineappleCoin wallet app")
}
"""
#fixed bug 5:36pm 12/10/21
#fixed bug 5:36pm 12/10/21
