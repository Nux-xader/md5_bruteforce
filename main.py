import hashlib, sys, os


clr = lambda: os.system('cls' if os.name == 'nt' else 'clear')

def banner():
    print(f"""
 █▀▄▀█ █▀▄ █▀   █░█ ▄▀█ █▀ █░█
 █░▀░█ █▄▀ ▄█   █▀█ █▀█ ▄█ █▀█
 
 █▄▄ █▀▀
 █▄█ █▀░  just for fun
 _______________________________
""")

def load_wordlist():
    clr()
    banner()
    while True:
        path = str(input(" [*] Enter wordlist (txt): "))
        try:
            wordlists = open(path, "r").read().split("\n")
            if len(wordlists) < 1:
                print(" [!] Your wordlists is empty")
                continue
            return wordlists
        except:
            print(f" [!] file {path} not found")


def main():
    wordlists = load_wordlist()
    while True:
        invalid = False
        md5hash = str(input(" [*] Enter your md5 hash : "))
        if len(md5hash) != 32: invalid = True
        if True in tuple(i.isupper() for i in md5hash): invalid = True
        if True in tuple(not i.isalnum() for i in md5hash): invalid = True
        if invalid:
            print(" [!] Invalid md5 hash")
            continue
        break
    
    print(" [+] Bruteforce started...")
    for word in wordlists:
        print(f" [+] Try using {word}")
        if hashlib.md5(word.encode()).hexdigest() == md5hash: break
    print(f" [+] Found match word {word} || {md5hash}")


if __name__ == "__main__":
    main()
