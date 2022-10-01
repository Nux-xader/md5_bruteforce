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
    pass


if __name__ == "__main__":
    main()