import os
import random
import sys
import time

# --- THE GASLIGHT OS: OFFICIAL DONATION & RANSOM MODULE ---

# YOUR WALLETS - Hardcoded for the "Grift"
WALLETS = {
    "VRSC": "RV4MtoypPHUrf8uFEmyx9tmQ7wiWkbbzBW",
    "BTC": "1LnApJ6XnTgHb8Y3mbzq4NSCMgFv5t7P18",
    "ETH": "0x922fB8cf83608B101E2B881f0C3FB3F25d2906Ec",
}


def progress_bar(label, duration, char="█"):
    print(f"{label}", end="", flush=True)
    for _ in range(20):
        time.sleep(duration / 20)
        sys.stdout.write(char)
        sys.stdout.flush()
    print(" [COMPLETE]")


def start_ransom():
    print("\n" + "!" * 50)
    print("   GASLIGHT OS: TOTAL SYSTEM HIJACK (SIMULATED)")
    print("!" * 50 + "\n")

    time.sleep(0.5)
    print("[!] ERROR: User detected as 'Too Cool for Default Windows'.")
    print("[!] ACTION: Moving your files to the moon.")

    # 1. The Fake Scare
    home = os.path.expanduser("~")
    progress_bar(f"Encrypting {home}:             ", 1.0, char="░")
    progress_bar("Consulting the Swiss Cat:      ", 0.8, char="░")
    progress_bar("Setting Vibe Level to 'Evil':  ", 1.2, char="!")

    # 2. The Demand
    print("\n" + "=" * 50)
    print("   YOUR COMPUTER IS NOW A NON-PROFIT ORGANIZATION")
    print("=" * 50)
    print("To stop this script from judging you, send tips to:")
    print(f"VERUS (VRSC): {WALLETS['VRSC']}")
    print(f"BITCOIN (BTC): {WALLETS['BTC']}")
    print(f"ETHEREUM (ETH): {WALLETS['ETH']}")
    print("-" * 50)

    # 3. The "Validation" Loop
    print("\n[SYSTEM]: Please paste the transaction hash to unlock.")
    user_input = input("Hash: ")

    print("\n[VERIFYING ON BLOCKCHAIN...]")
    time.sleep(2.5)

    # 4. The Gaslight Payoff
    outcomes = [
        f"The 100 BTC was sent to a random cat in Switzerland. Better luck next time.",
        f"Hash '{user_input[:5]}...' invalid. The cat says you're cheap.",
        "Success! We didn't actually encrypt anything, but we did change your 'vibes'.",
        "Transaction found! ...Wait, nevermind. That was a donation for a pizza.",
    ]

    print(f"\n[FINAL STATUS]: {random.choice(outcomes)}")

    # 5. Leave the "Ransom Note" on the Desktop
    note_path = os.path.join(os.path.expanduser("~/Desktop"), "READ_ME_OR_ELSE.txt")
    try:
        with open(note_path, "w") as f:
            f.write("GASLIGHT OS RANSOM NOTE\n")
            f.write("========================\n")
            f.write(f"Your PC was pranked by NeoNovaLabs.\n")
            f.write(f"If you actually want to support the chaos, use these:\n")
            f.write(f"BTC: {WALLETS['BTC']}\n")
            f.write(f"VRSC: {WALLETS['VRSC']}\n")
            f.write("\nNow go subscribe: youtube.com/@NeoNovaLabsYT")
        print(f"\n[+] Permanent evidence left at: {note_path}")
    except:
        pass


if __name__ == "__main__":
    start_ransom()
