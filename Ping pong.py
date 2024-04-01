import pygame as pg, sys, random, time

pg.init()

def reset():
    global speed_x, speed_y
    ball.x = WIDTH/2 - 10
    ball.y = random.randint(10,100)
    speed_x *= random.choice([-1, -1])
    speed_y *= random.choice([-1, -1])

def won(winner):
    global score1, score2
    if winner == 'player1':
        score1 += 1
    else:
        score2 += 1
    reset()
def ball_move():
    global speed_x, speed_y

    ball.x += speed_x
    ball.y += speed_y
    screen.fill('black')
    if ball.bottom >= HEIGHT or ball.top <= 0:
        speed_y *= -1
    if ball.left <= 0:
        won("player2")
    if ball.right >= WIDTH:
        won("player1")
    if ball.colliderect(player1) or ball.colliderect(player2) :
        speed_x *= -1
def move_players():
    global player1_speed, player2_speed

    player1.y += player1_speed
    # player2.y += player2_speed
    if player1.top <= 0:
        player1.top = 0
    if player1.bottom >= HEIGHT:
        player1.bottom = HEIGHT
    """if player2.top <= 0:
        player2.top = 0
    if player2.bottom >= HEIGHT:
        player2.bottom = HEIGHT """
def cpu_move():
    global  player2_speed

    player2.y += player2_speed
    if ball.centery <= player2.centery:
        player2_speed = -6
    if ball.centery >= player2.centery:
        player2_speed = 6
    if player2.top <= 0:
        player2.top = 0
    if player2.bottom >= HEIGHT:
        player2.bottom = HEIGHT

WIDTH , HEIGHT = 800, 500
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Ping Pong - By Shafi")

clock = pg.time.Clock()
ball = pg.Rect(0, 0, 30, 30)
ball.center = (WIDTH/2, HEIGHT/2)

player1 = pg.Rect(0, 0, 20, 100)
player1.centery = HEIGHT/2
player2 = pg.Rect(HEIGHT, WIDTH, 20, 100)
player2.midright = (WIDTH, HEIGHT/2)

score1 , score2 = 0, 0

speed_x = 9
speed_y = 6

player1_speed = 0
player2_speed = 6

score_font = pg.font.Font(None, 100)

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_z:
                player1_speed = -8
            if event.key == pg.K_s:
                player1_speed = 8
            if event.key == pg.K_UP:
                player2_speed = -8
            if event.key == pg.K_DOWN:
                player2_speed = 8
        if event.type == pg.KEYUP:
            if event.key == pg.K_z:
                player1_speed = 0
            if event.key == pg.K_s:
                player1_speed = 0
            if event.key == pg.K_UP:
                player2_speed = 0
            if event.key == pg.K_DOWN:
                player2_speed = 0
    ball_move()
    move_players()
    cpu_move()

    player1_surface = score_font.render(str(score1), True, 'white')
    player2_surface = score_font.render(str(score2), True, 'white')

    screen.blit(player1_surface,(WIDTH/4, 20))
    screen.blit(player2_surface, (3*WIDTH/4, 20))

    pg.draw.aaline(screen, 'white', (WIDTH/2, 0), (WIDTH/2, HEIGHT))
    pg.draw.ellipse(screen, 'green', ball)
    pg.draw.rect(screen, 'blue', player1)
    pg.draw.rect(screen, 'red', player2)

    ok = False
    if score1 >= 10:
        ok = True
        win_text = "Player 1 won."
    if score2 >= 10:
        ok = True
        win_text = "Player 2 won."
    if ok:
        text = score_font.render(win_text, 1, 'brown')
        screen.blit(text, (WIDTH//2 - text.get_width()//2, HEIGHT//2 - text.get_height()//2))
        pg.display.update()
        pg.time.delay(1000)
        break
    pg.display.update()
    clock.tick(60)