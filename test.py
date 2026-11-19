import pygame, random

pygame.init()


sys = pygame.cursors.Cursor(pygame.SYSTEM_CURSOR_CROSSHAIR)

# Create the game window
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Moving Square")

# Set up our colours
SKY_BLUE = (135, 206, 235)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

# Store the player's and enemenys starting position
player_x = 375
player_y = 275
enemy_x = 100
enemy_y = 200
bullet_x, bullet_y = pygame.mouse.get_pos()

selector1X = 225 
selector1Y = 420
selector2X = 525 
selector2Y = 420

direction = random.randint(0,360)


expRect = pygame.Rect(0, 540, 800, 40)

expBars = [
    pygame.Rect(0, 550, 800, 20), #Full Bar
    pygame.Rect(0, 550, 600, 20), #75% of bar
    pygame.Rect(0, 550, 400, 20), #50% of bar
    pygame.Rect(0, 550, 200, 20), #25% of bar
]

lvlBars = [
    pygame.Rect(150, 100, 200, 400),
    pygame.Rect(450, 100, 200, 400),
]

selector = [
    pygame.Rect(225, 420, 50, 50),
    pygame.Rect(525, 420, 50, 50)
]

upgrades = [

]





#bullet_x = player_y
#bullet_y = player_x
bullet_speed = 5  # Increased speed so it doesn't move at a crawl
bullet_active = False

enemy_killed = 0

selected = False

# Control how many pixels the square moves each frame
speed = 3
enemy_speed = 0.5

# Keep the game running
running = True

# Add a clock to regulate frame rate (prevents the game from running too fast)
clock = pygame.time.Clock()

while running:
    enemyActive = True
    bullet_active = False
    # Check for events, including closing the window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Check which keyboard keys are being pressed
    keys = pygame.key.get_pressed()




    # 1. HANDLE INPUT (Only handles the initial trigger)
    if event.type == pygame.MOUSEBUTTONDOWN:        
        if not bullet_active:
            # Reset bullet position to the player's position when fired
            #bullet_x = player_x + 17
            #bullet_y = player_y
            bullet_active = True 
            bullet_x, bullet_y = pygame.mouse.get_pos()
    elif event.type == pygame.MOUSEBUTTONUP:
        bullet_active = False
    # 2. UPDATE BULLET POSITION
    if bullet_active:
        bullet_y -= bullet_speed 

        # Check boundaries (If it goes off-screen, deactivate it)
        if bullet_x >= 800 or bullet_y >= 600 or bullet_y <= 0 or bullet_x <= 0:                      
            bullet_active = False


    # ================= DRAWING SECTION =================
    # Paint the background first to clear the previous frame
    screen.fill(SKY_BLUE)

    # Now draw the bullet if it's active
    if bullet_active:
        pygame.draw.rect(screen, BLUE, (bullet_x - 7, bullet_y, 1, 1)) # Made bullet smaller (15x15) so it looks like a bullet!

    # 1. Create rectangle objects for both the player and the enemy
    player_rect = pygame.Rect(player_x, player_y, 50, 50)
    enemy_rect = pygame.Rect(enemy_x, enemy_y, 30, 30)

    bullet_rect = pygame.Rect(bullet_x,bullet_y,1,1)
    selector1 = pygame.Rect(selector1X, selector1Y, 50, 50)
    selector2 = pygame.Rect(selector2X, selector2Y, 50, 50)
    # 2. Check if the rectangles overlap (collision)
    if player_rect.colliderect(enemy_rect):
        running = False  # Ends the game loop
    if bullet_rect.colliderect(enemy_rect):
        enemy_x = random.randint(0,800)
        enemy_y = random.randint(0,600)
        bullet_active = False
        enemy_killed += 1
    if bullet_rect.colliderect(selector1):
        selected = True
        enemy_killed = 0
    if bullet_rect.colliderect(selector2):
        selected = True
        enemy_killed = 0
    # Draw the player and enemy on top of the background
    #pygame.draw.rect(screen, BLUE, (player_x, player_y, 50, 50))
    pygame.draw.rect(screen, BLACK, expRect)

    if selected:
        enemyActive = True
        selected = False

    if enemy_killed == 5:
        font = pygame.font.SysFont(None, 48)
        message = font.render("Level up!", True, BLACK)
        screen.blit(message, (320, 25))
        enemyActive = False

        pygame.draw.rect(screen, BLACK, lvlBars[0])
        pygame.draw.rect(screen, BLACK, lvlBars[1])
        pygame.draw.rect(screen, RED, selector[0])
        pygame.draw.rect(screen, RED, selector[1])
    if enemy_killed == 4:
        pygame.draw.rect(screen, GREEN, expBars[0])
    if enemy_killed == 3:
        pygame.draw.rect(screen, GREEN, expBars[1])
    if enemy_killed == 2:
        pygame.draw.rect(screen, GREEN, expBars[2])
    if enemy_killed == 1:
        pygame.draw.rect(screen, GREEN, expBars[3])


    if enemyActive:
        pygame.draw.rect(screen, RED, (enemy_x, enemy_y, 30, 30))
    

    pygame.mouse.set_cursor(sys)
    
    # Show the updated screen
    pygame.display.flip()
    
    # Cap the game at 60 frames per second
    clock.tick(60)

pygame.quit()