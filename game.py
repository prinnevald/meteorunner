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


    # updating bullets
    for bullet in bullets.sprites():
        if bullet.getPosition() > 0:
            bullet.move()
        else:
            bullets.remove(bullet)

    
    # meteors logic
    if meteorReload < 0:
        meteors.add(Meteor((randint(0, windowWidth), 0)))
        meteorReload = 100
    else:
        meteorReload -= meteorTick


    # updating meteors
    for meteor in meteors.sprites():
        if meteor.getPosition() < windowHeight:
            meteor.move()
        else:
            meteors.remove(meteor)


    # collisions
    for bullet in bullets:
        collided_bullets = pygame.sprite.spritecollide(bullet, meteors, True)
        if len(collided_bullets) > 0:
            # bullet.explode()
            bullets.remove(bullet)
        # bullet.explode()
        #for deleteIt in collided_bullets:
        #    bullets.remove(deleteIt)

    # displaying everything on screen
    screen.fill((0,0,0))

    meteors.draw(screen)
    bullets.draw(screen)
    group.draw(screen)

    pygame.display.flip()
    clock.tick(60)


