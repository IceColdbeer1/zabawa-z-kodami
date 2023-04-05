import pygame
from utils import draw_text


class Home:
    def __init__(self, player):
        self.player = player
        self.item_box = []

    def add_item_to_box(self, item):
        self.item_box.append(item)

    def remove_item_from_box(self, item):
        if item in self.item_box:
            self.item_box.remove(item)

    def heal_player(self):
        self.player.heal(self.player.max_hp)
        self.player.restore_mp(self.player.max_mp)

    def save_game(self):
        pass  # Tutaj można zaimplementować zapisywanie stanu gry.

    def draw_home_ui(self, screen, menu_selected_option):
        screen.fill((0, 0, 0))

        draw_text(screen, self.player.name, 20, 20, 30)
        draw_text(screen, "Home", 400, 20, 30)

        draw_home_menu(screen, menu_selected_option)

        draw_item_box(screen, self.item_box, 20, 100)


def draw_home_menu(screen, selected_option):
    menu_options = ["Rest", "Item Box", "Save Game", "Leave Home"]
    x = 540
    y = 500

    for index, option in enumerate(menu_options):
        if index == selected_option:
            color = (255, 255, 0)
        else:
            color = (255, 255, 255)

        draw_text(screen, option, x, y, 24, color)
        y += 24


def draw_item_box(screen, item_box, x, y):
    draw_text(screen, "Item Box:", x, y, 30)
    y += 40

    for item in item_box:
        draw_text(screen, item.name, x, y, 24)
        y += 24
