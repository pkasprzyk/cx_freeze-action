import pygame


class Game:
    def __init__(self):
        dimensions = pygame.Vector2(640, 480)
        pygame.init()

        self.screen = pygame.display.set_mode(dimensions)
        self.font = pygame.font.SysFont(None, 30)

    def blit_text(self, text, location):
        self.screen.blit(self.font.render(text, False, pygame.Color("white")), location)

    def main(self):
        cat = pygame.image.load("resources/450px-Six_weeks_old_cat_aka.jpg")
        self.blit_text("It's alive!", (10, 20))
        self.blit_text("Press 'q' to quit.", (10, 50))
        self.screen.blit(cat, cat.get_rect().move(10, 80))
        self.blit_text(
            "Cat photo by André Karwath aka Aka - Own work, CC BY-SA 2.5,", (10, 400)
        )
        self.blit_text(
            "https://commons.wikimedia.org/w/index.php?curid=217417", (10, 430)
        )

        pygame.display.update()

        while True:
            events = pygame.event.get()
            for e in events:
                if e.type == pygame.QUIT:
                    return
                if e.type == pygame.KEYDOWN and e.key == pygame.K_q:
                    return

            pygame.display.update()


if __name__ == "__main__":
    Game().main()
