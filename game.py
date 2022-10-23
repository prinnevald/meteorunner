import pygame

from classes.player import Player
from classes.meteor import Meteor
from classes.star import Star

from random import randint

# initialize Pygame and globals
pygame.init()

windowWidth, windowHeight = 400, 700
screen = pygame.display.set_mode((windowWidth,windowHeight))
pygame.display.set_caption('Meteorunner')
clock = pygame.time.Clock()


# adding all sprites to displaygroup
group = pygame.sprite.Group()
player = Player((windowWidth/2, windowHeight - 100), group)
group.add(player)


# bullets group. Separate to delete if needed
# and to not cycle over all of them when needed
# to update (movement or whatever)
bullets = pygame.sprite.Group()

# meteors group. Created for the same reason as bullets
meteors = pygame.sprite.Group()
meteorReload = 100
meteorTick = 1

# explosions group to cycle through frames
explosions = pygame.sprite.Group()
explosionFrame = 120
explosionTick = 6


# the Game Loop
while True:

    # check one-time buttons
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                player.setAutofire()
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()


    # check player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        if(player.getPosition()[0] >= player.getWidth()/2):
            player.move(-5)
    if keys[pygame.K_RIGHT]:
        if(player.getPosition()[0] <= windowWidth - player.getWidth()/2):
            player.move(5)


    # check shooting
    player.reloadTick()
    if player.isAutofire() or keys[pygame.K_SPACE]:
        if player.ready():
            bullets.add(player.shoot())
    

    # meteors logic
    if meteorReload < 0:
        meteors.add(Meteor((randint(0, windowWidth), 0)))
        meteorReload = 100
    else:
        meteorReload -= meteorTick


    # updating meteors, explosions and bullet movement
    for meteor in meteors.sprites():
        if meteor.move(windowHeight):
            meteors.remove(meteor)

    for explosion in explosions.sprites():
        if explosion.update():
            explosions.remove(explosion)

    for bullet in bullets.sprites():
        if bullet.move():
            bullets.remove(bullet)


    # collisions
    for bullet in bullets:
        ifcollided = pygame.sprite.spritecollide(bullet, meteors, True)
        if len(ifcollided) > 0:
            explosions.add(bullet.explode())
            bullets.remove(bullet)


    # displaying everything on screen
    screen.fill((0,0,0))

    explosions.draw(screen)
    meteors.draw(screen)
    bullets.draw(screen)
    group.draw(screen)

    pygame.display.flip()
    clock.tick(60)


