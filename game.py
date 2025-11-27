import pygame
from characters import characters
import requests
import os
from dotenv import load_dotenv
load_dotenv()
key = os.getenv('WEATHER_API_KEY')

pygame.init()

WIDTH, HEIGHT = 500, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tinder Mini Game")

font = pygame.font.SysFont("arial", 24)

heart_img = pygame.image.load("images/heart.jpg")
cross_img = pygame.image.load("images/cross.png")

heart_img = pygame.transform.scale(heart_img, (90, 90))
cross_img = pygame.transform.scale(cross_img, (90, 90))


def get_temp():
    city = "Barcelona"
    try:
        data = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={key}").json()
        return str(round(data["main"]["temp"])) + "°C"
    except:
        return "No °C"

def load_image(path):
    try:
        return pygame.image.load(path)
    except:
        return None
    
def main_menu():
    menu_running = True
    title_font = pygame.font.SysFont("arial", 40)
    button_font = pygame.font.SysFont("arial", 30)

    while menu_running:
        screen.fill((255, 182, 193))

        title = title_font.render("Welcome to Tinder", True, (0, 0, 0))
        screen.blit(title, (70, 150))
        
        subtitle_font = pygame.font.SysFont("arial", 30)
        subtitle = subtitle_font.render("( from Temu )", True, (50, 50, 50))
        screen.blit(subtitle, (150, 200))
        
        
        subtitle_font = pygame.font.SysFont("arial", 30)
        subtitle = subtitle_font.render("Press start!", True, (50, 50, 50))
        screen.blit(subtitle, (180, 300))

        start_button = pygame.Rect(150, 350, 200, 80)
        pygame.draw.rect(screen, (255, 105, 180), start_button, border_radius=20)

        start_text = button_font.render("Start", True, (255, 255, 255))
        screen.blit(start_text, (215, 375))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN and start_button.collidepoint(event.pos):
                menu_running = False

        pygame.display.update()

def draw_buttons():
    screen.blit(heart_img, (320, 560))
    screen.blit(cross_img, (90, 560))

def run_game():
    liked = []
    running = True
    index = 0
    temp_font = pygame.font.SysFont("arial", 20)
    while running and index < len(characters):
        screen.fill((255, 255, 255))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if 320 < x < 410 and 560 < y < 650:
                    liked.append(characters[index])
                    index += 1
                if 90 < x < 180 and 560 < y < 650:
                    index += 1

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    liked.append(characters[index])
                    index += 1
                if event.key == pygame.K_LEFT:
                    index += 1

        if index >= len(characters):
            break

        char = characters[index]

        screen.blit(char.image, (90, 80))

        text = f"{char.name} — {char.description}"
        info = font.render(text, True, (0, 0, 0))
        screen.blit(info, (50, 520))

        draw_buttons()
        
        temp_text = temp_font.render("Barcelona: " + get_temp(), True, (0, 0, 0))
        screen.blit(temp_text, (WIDTH - 150, HEIGHT - 40)) 
        
        pygame.display.update()


    screen.fill((245, 245, 245))
    if len(liked) == 0:
        summary_text = "You liked:\n" + "You liked no one\n" + "Who are you? Apalon?"
        lines = summary_text.split("\n")
    else:
        summary_text = "You liked:\n" + "\n".join([c["name"] for c in liked])
        lines = summary_text.split("\n")
    y = 50  
    for line in lines:
        info = font.render(line, True, (0, 0, 0))
        screen.blit(info, (50, y))
        y += 40  
    pygame.display.update()
    pygame.time.wait(4000)
    pygame.quit()
