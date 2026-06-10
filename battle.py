import random
import copy
import os
from entity import player_party, MONSTER_TEMPLATES

def check_status():
    print("\n=== STATUS KARAKTER ===")
    for p in player_party:
        s = "Hidup" if p.alive else "MATI"
        print(f"{p.name}: HP {p.hp}/{p.max_hp} | MP {p.mp}/{p.max_mp} ({s})")
    print("=======================\n")

def pick_enemies():
    key = random.choice(list(MONSTER_TEMPLATES.keys()))
    return [copy.deepcopy(MONSTER_TEMPLATES[key])]

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def battle():
    clear()
    players = player_party
    enemies = pick_enemies()

    print("\nPERTARUNGAN DIMULAI!")
    print("Musuh:")
    e = enemies[0]
    print(f"- {e.name} HP:{e.hp}")

    while True:
        # Status singkat
        print("=== STATUS ===")
        for p in players:
            print(f"{p.name}: HP {p.hp}/{p.max_hp} MP {p.mp}/{p.max_mp}")
        print("---")
        for e in enemies:
            if e.alive:
                print(f"{e.name}: HP {e.hp}/{e.max_hp}")
        print("==============\n")
        input("\nTekan Enter...")

        # Giliran player
        for p in players:
            if not any(e.alive for e in enemies):
                break
            if not p.alive:
                print(f"{p.name} sudah mati, dilewati.")
                continue

            print(f"\n--- Giliran {p.name} ---")
            for i, s in enumerate(p.skills, 1):
                print(f"{i}. {s['name']} (MP:{s['cost']})")

            while True:
                c = input("Pilih skill (1-3): ")
                if c in ['1','2','3']:
                    clear()
                    print(p.use_skill(int(c)-1, enemies))
                    break
                else:
                    print("Input salah!")

        # Cek menang
        if not any(e.alive for e in enemies):
            print("\nSEMUA MUSUH KALAH! MENANG!")
            break

        # Giliran musuh
        print("\n-- Giliran Musuh --")
        if e.alive:
            print(e.act(players))

        # Cek kalah
        if not any(p.alive for p in players):
            print("\nSEMUA KARAKTER MATI. KALAH!")
            break

    input("\nTekan Enter untuk kembali ke menu...")

def menu():
    while True:
        clear()
        print("""
======================
    RPG TURN-BASED
======================
1. Mulai Bertarung
2. Cek Status
3. Keluar Game
======================
""")
        p = input("Pilih (1-3): ")
        if p == '1':
            battle()
        elif p == '2':
            check_status()
        elif p == '3':
            print("Bye!")
            break
        else:
            print("Pilihan salah!")

if __name__ == "__main__":
    menu()