import pygame
from characters import characters

pygame.init()

WIDTH, HEIGHT = 500, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tinder Mini Game")

font = pygame.font.SysFont("arial", 24)

heart_img = pygame.image.load("images/heart.png")
cross_img = pygame.image.load("images/cross.png")

heart_img = pygame.transform.scale(heart_img, (90, 90))
cross_img = pygame.transform.scale(cross_img, (90, 90))


def load_image(path):
    try:
        return pygame.image.load(path)
    except:
        return None


def draw_buttons():
    screen.blit(heart_img, (320, 560))
    screen.blit(cross_img, (90, 560))


def run_game():
    running = True
    index = 0
    liked = []

    while running and index < len(characters):
        screen.fill((245, 245, 245))

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

        img = load_image(char["image"])
        if img:
            w, h = img.get_size()
            target_w, target_h = 320, 420
            scale = min(target_w / w, target_h / h)
            new_w, new_h = int(w * scale), int(h * scale)
            img = pygame.transform.scale(img, (new_w, new_h))
            screen.blit(img, (90, 80))


        text = f"{char['name']} — {char['description']}"
        info = font.render(text, True, (0, 0, 0))
        screen.blit(info, (50, 520))

        draw_buttons()
        pygame.display.update()


    screen.fill((245, 245, 245))
    summary_text = "You liked:\n" + "\n".join([c["name"] for c in liked])
    lines = summary_text.split("\n")
    for i, line in enumerate(lines):
        info = font.render(line, True, (0, 0, 0))
        screen.blit(info, (50, 50 + i * 40))
    pygame.display.update()
    pygame.time.wait(5000)

    pygame.quit()
