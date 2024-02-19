import pygame, sys

num_disks = int(input("PLEASE ENTER THE NUMBERS OF DISKS..."))
fps = 500
pygame.init()
BACKGROUND_COLOR = (255, 255, 255)  # White
BARS_COLOR_MOVE_FONT_COLOR = (0, 0, 0)  # Black
DISKS_COLOR = (255, 0, 0)  # Red
TITLE_FONT_COLOR = (0, 255, 0)  # Green
WINDOW_SIZE = WINDOW_WIDTH, WINDOW_HEIGHT = (650, 650)
counter = 0
BASIC_FONT = pygame.font.SysFont("freesansbold", 35)
BIG_FONT = pygame.font.SysFont("freesansbold", 50)
SCREEN = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Tower of Hanoi")
clock = pygame.time.Clock()
towers = []
HORIZONTAL_BAR_HEIGHT = DISK_HEIGHT = 10
DISK_BASE_DISTANCE = 15
S = [0, 0, 0, 0]
S[3] = pygame.Rect(20, WINDOW_HEIGHT - 20, WINDOW_WIDTH - 40, HORIZONTAL_BAR_HEIGHT)

for i in range(0, 3):
    towers.append(pygame.Rect(WINDOW_WIDTH / 3 * (i + 1) - 100, 100, 10, S[3].top - 100))

discs = [[], [], []]
top = S[3].top - HORIZONTAL_BAR_HEIGHT
disc_width = 150
reduced_disc_width = 30

while disc_width / num_disks <= reduced_disc_width:
    reduced_disc_width -= 1
    continue

for i in range(num_disks):
    discs[0].append(pygame.Rect(towers[0].centerx - disc_width / 2, top - HORIZONTAL_BAR_HEIGHT, disc_width, DISK_HEIGHT))
    top = top - DISK_HEIGHT - 5
    disc_width = disc_width - reduced_disc_width

def update_screen():
    check_events()
    SCREEN.fill(BACKGROUND_COLOR)

    for i in range(len(towers)):
        pygame.draw.rect(SCREEN, BARS_COLOR_MOVE_FONT_COLOR, towers[i], 0)

    for i in range(len(discs)):
        for j in range(len(discs[i])):
            pygame.draw.rect(SCREEN, DISKS_COLOR, discs[i][j], 0)

    text = "Moves: {0}".format(counter)
    surf = BASIC_FONT.render(text, True, BARS_COLOR_MOVE_FONT_COLOR)
    rect = surf.get_rect()
    rect.topleft = (WINDOW_WIDTH - rect.width - 10, 0)
    SCREEN.blit(surf, rect)

    surf = BIG_FONT.render("Tower of Hanoi", True, TITLE_FONT_COLOR)
    rect = surf.get_rect()
    rect.center = (towers[1].left, 30)
    SCREEN.blit(surf, rect)

    pygame.display.update()

def move():
    global counter
    for i in range(len(moves)):
        init = moves[i][0]
        dest = moves[i][1]

        if len(discs[dest]) != 0:
            dest_y = discs[dest][-1].top - DISK_BASE_DISTANCE
        else:
            dest_y = S[3].top - HORIZONTAL_BAR_HEIGHT

        while discs[init][-1].top > towers[init].top - 30:
            clock.tick(fps)
            discs[init][-1].move_ip([0, -1])
            update_screen()

        if discs[init][-1].centerx < towers[dest].centerx:
            while discs[init][-1].centerx < towers[dest].centerx:
                clock.tick(fps)
                discs[init][-1].move_ip([1, 0])
                update_screen()
        else:
            while discs[init][-1].centerx > towers[dest].centerx:
                clock.tick(fps)
                discs[init][-1].move_ip([-1, 0])
                update_screen()

        while discs[init][-1].centery < dest_y:
            clock.tick(fps)
            discs[init][-1].move_ip([0, 1])
            update_screen()

        discs[dest].append(discs[init].pop())
        counter += 1

def tower_of_hanoi(n, source, auxiliary, destination):
    if n == 1:
        moves.append([source, destination])
    else:
        tower_of_hanoi(n - 1, source, destination, auxiliary)
        moves.append([source, destination])
        tower_of_hanoi(n - 1, auxiliary, source, destination)

def check_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

if __name__ == "__main__":
    moves = []
    tower_of_hanoi(num_disks, 0, 1, 2)
    move()

    while True:
        check_events()
