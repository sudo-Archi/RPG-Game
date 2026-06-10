import random

class Entity:
    def __init__(self, name, hp, mp):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.max_mp = mp
        self.mp = mp
        self.alive = True
        self.guard = False

    def take_damage(self, damage):
        if self.guard:
            damage //= 2
            self.guard = False
        self.hp -= damage

        if self.hp <= 0:
            self.hp = 0
            self.alive = False

class Player(Entity):
    def __init__(self, name, hp, mp, skills):
        super().__init__(name, hp, mp)
        self.skills = skills

    def use_skill(self, idx, enemies):
        skill = self.skills[idx]
        if self.mp < skill['cost']:
            return "MP tidak cukup!"
        self.mp -= skill['cost']
        
        if skill['type'] == 'guard':
            self.guard = True
            return f"""
{self.name} pakai {skill['name']}! 
Bersiap menahan serangan!
"""
        else:
            target = enemies[0]
            target.take_damage(skill['power'])
            return f"""
{self.name} pakai {skill['name']}! 
{target.name} kena {skill['power']} damage!
HP {target.name} sekarang: {target.hp}/{target.max_hp}
"""

class Enemy(Entity):
    def __init__(self, name, hp, skills):
        super().__init__(name, hp, 0)
        self.skills = skills

    def act(self, players):
        if not self.alive:
            return ""
        
        skill = random.choice(self.skills)
        target = random.choice([p for p in players if p.alive])
        target.take_damage(skill['power'])
        return f"""
{self.name} pakai {skill['name']}! 
{target.name} kena {skill['power']} damage!
HP {target.name} sekarang: {target.hp}/{target.max_hp}
"""


# ========== KARAKTER PLAYER ==========
warrior_skills = [
    {'name': 'Valiant Blow',    'type': 'damage', 'cost': 4,  'power': 25},
    {'name': 'Vanguard Thrust', 'type': 'damage', 'cost': 6,  'power': 30},
    {'name': 'Bulwark',         'type': 'guard',  'cost': 0,  'power': 0},
]

mage_skills = [
    {'name': 'Soul Arrow',      'type': 'damage', 'cost': 15, 'power': 50},
    {'name': 'Storm Ruler',     'type': 'damage', 'cost': 12, 'power': 40},
    {'name': 'Ruinous Storm',   'type': 'damage', 'cost': 20, 'power': 65},
]

assassin_skills = [
    {'name': 'Phantom Slash',   'type': 'damage', 'cost': 15, 'power': 55},
    {'name': 'Dark Side Moon',  'type': 'damage', 'cost': 18, 'power': 65},
    {'name': 'Crimson Tragedy', 'type': 'damage', 'cost': 20, 'power': 75},
]

player_party = [
    Player('Knight Archi', 150, 20, warrior_skills),
    Player('Fairy Leaf',   75,  50, mage_skills),
    Player('Red Hood',     60,  45, assassin_skills),
]

# ========== MUSUH ==========
monster_a_skills = [
    {'name': 'Acid Spit',     'type': 'damage', 'power': 10},
    {'name': 'Sticky Wrap',   'type': 'damage', 'power': 13},
    {'name': 'Corrosive Gel', 'type': 'damage', 'power': 15},
]

monster_b_skills = [
    {'name': 'Shadow Bolt',   'type': 'damage', 'power': 18},
    {'name': 'Wicked Whisper','type': 'damage', 'power': 23},
    {'name': 'Fey Curse',     'type': 'damage', 'power': 25},
]

monster_c_skills = [
    {'name': 'Soul Rend',     'type': 'damage', 'power': 22},
    {'name': 'Grave Grasp',   'type': 'damage', 'power': 30},
    {'name': 'Hollow Scream', 'type': 'damage', 'power': 35},
]

MONSTER_TEMPLATES = {
    'A': Enemy('Slime',      55,  monster_a_skills),
    'B': Enemy('Dark Fairy', 100,  monster_b_skills),
    'C': Enemy('Hollow',     200, monster_c_skills),
}