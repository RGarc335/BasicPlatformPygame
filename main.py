import pygame
pygame.init()
_display_surf = pygame.display.set_mode((500, 500))
pygame.display.set_caption("First Game")

walkRight = [pygame.image.load('Sprites/WalkingRight/Armature_Walking_00.png'),
             pygame.image.load('Sprites/WalkingRight/Armature_Walking_01.png'),
             pygame.image.load('Sprites/WalkingRight/Armature_Walking_02.png'),
             pygame.image.load('Sprites/WalkingRight/Armature_Walking_03.png'),
             pygame.image.load('Sprites/WalkingRight/Armature_Walking_04.png'),
             pygame.image.load('Sprites/WalkingRight/Armature_Walking_05.png'),
             pygame.image.load('Sprites/WalkingRight/Armature_Walking_06.png'),
             pygame.image.load('Sprites/WalkingRight/Armature_Walking_07.png'),
             pygame.image.load('Sprites/WalkingRight/Armature_Walking_08.png')]
walkLeft = [pygame.image.load('Sprites/WalkingLeft/Armature_Walking_00.png'),
            pygame.image.load('Sprites/WalkingLeft/Armature_Walking_01.png'),
            pygame.image.load('Sprites/WalkingLeft/Armature_Walking_02.png'),
            pygame.image.load('Sprites/WalkingLeft/Armature_Walking_03.png'),
            pygame.image.load('Sprites/WalkingLeft/Armature_Walking_04.png'),
            pygame.image.load('Sprites/WalkingLeft/Armature_Walking_05.png'),
            pygame.image.load('Sprites/WalkingLeft/Armature_Walking_06.png'),
            pygame.image.load('Sprites/WalkingLeft/Armature_Walking_07.png'),
            pygame.image.load('Sprites/WalkingLeft/Armature_Walking_08.png')]
bg = pygame.image.load('Background/spaceBg.png')
char = pygame.image.load('Sprites/WalkingRight/Armature_Walking_00.png')

clock = pygame.time.Clock()
x = 50
y = 400
width = 64
height = 64
jumpImage = pygame.image.load("venv/images/jump.png")
vel = 5
isJump = False
jumpCount = 10
attemptJumps = 2
left = False
right = False
walkCount = 0

def redrawgamewindow():
    global walkCount
    _display_surf.blit(bg, (0, 0))
    if walkCount + 1 >= 27:
        walkCount = 0
    if left:
        _display_surf.blit(walkLeft[walkCount//3], (x, y))
        walkCount += 1
    elif right:
        _display_surf.blit(walkRight[walkCount//3], (x, y))
        walkCount += 1
    else:
        _display_surf.blit(char, (x, y))
        walkCount = 0
    pygame.display.update()
run = True
while run:
    clock.tick(27)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if event.type == pygame.KEYDOWN:
        print(str(pygame.key.name(event.key)) + " is pressed")
    if keys[pygame.K_LEFT] and x > vel:
        x -= vel
        left = True
        right = False
    elif keys[pygame.K_RIGHT] and x < 500 - width - vel:
        x += vel
        right = True
        left = False
    else:
        right = False
        left = False
        walkCount = 0
    if not (isJump):
        if keys[pygame.K_SPACE]:
            isJump = True
            right = False
            left = False
            walkCount = 0
    else:
        if jumpCount >= -10 and attemptJumps > 0:
            neg = 1
            if jumpCount < 0:
                neg = -1
            y -= (jumpCount ** 2) * .5 * neg
            # attemptJumps -= 1
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10
            attemptJumps = 1

    redrawgamewindow()
pygame.quit()
