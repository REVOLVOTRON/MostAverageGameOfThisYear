import json

class Config:
    def __init__(self):
        with open('settings.json', 'r') as file:
            settings = json.load(file)

        self.width = settings['width']
        self.height = settings['height']
        self.title = settings['title']
        self.white = tuple(settings['white'])
        self.black = tuple(settings['black'])
        self.blue = tuple(settings['blue'])
        self.player_speed = settings['player_speed']
        self.enemy_speed = settings['enemy_speed']
        self.bullet_speed = settings['bullet_speed']
        self.enemy_spawn_interval = settings['enemy_spawn_interval']
        self.player_image = settings['player_image']
        self.enemy_image = settings['enemy_image']
        self.bullet_image = settings['bullet_image']
        self.player_health = settings['player_health']
        self.enemy_health = settings['enemy_health']
        self.bullet_damage = settings['bullet_damage']
        self.enemies_to_upgrade = settings['enemies_to_upgrade']
        self.damage_increase = settings['damage_increase']
        self.health_increase = settings['health_increase']
        self.enemies_to_upgrade_increase = settings['enemies_to_upgrade_increase']
