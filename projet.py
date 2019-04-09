# -*- coding: utf-8 -*-


import pygame

import math

import time

import random

from pygame.locals import *

from math import *



# Initialisation du module

if __name__ == '__main__':

    pygame.init()

    width = 1000
    height = 800

    # paramètrage de la fenêtre du jeu (couple pixels)

    window = pygame.display.set_mode((width, height))
    
    # police
    font_big = pygame.font.SysFont("Lucida Console", 40, 1)
    font_medium = pygame.font.SysFont("Lucida Console",30)
    font_small = pygame.font.SysFont("Lucida Console", 15)
    font_small_bold = pygame.font.SysFont("Lucida Console",15,1)
    
    # Icone de fenêtre
    icone_fenetre = pygame.image.load('Gloupi.png')
    pygame.display.set_icon(icone_fenetre)

    # Titre de fenêtre
    pygame.display.set_caption('Julius et Martin')

    # Récupération des images
    wall = pygame.image.load('brique_neutre.png').convert()
    
    hero_down = pygame.image.load('julius_down.png').convert()
    hero_down.set_colorkey((0, 0, 0))

    hero_up = pygame.image.load('julius_up.png').convert()
    hero_up.set_colorkey((0, 0, 0))

    hero_left = pygame.image.load('julius_left.png').convert()
    hero_left.set_colorkey((0, 0, 0))

    hero_right = pygame.image.load('julius_right.png').convert()
    hero_right.set_colorkey((0, 0, 0))

    hero_down_walking1 = pygame.image.load('julius_down_walking1.png').convert()
    hero_down_walking1.set_colorkey((0, 0, 0))

    hero_down_walking2 = pygame.image.load('julius_down_walking2.png').convert()
    hero_down_walking2.set_colorkey((0, 0, 0))

    hero_up_walking1 = pygame.image.load('julius_up_walking1.png').convert()
    hero_up_walking1.set_colorkey((0, 0, 0))

    hero_up_walking2 = pygame.image.load('julius_up_walking2.png').convert()
    hero_up_walking2.set_colorkey((0, 0, 0))

    hero_right_walking1 = pygame.image.load('julius_right_walking1.png').convert()
    hero_right_walking1.set_colorkey((0, 0, 0))

    hero_right_walking2 = pygame.image.load('julius_right_walking2.png').convert()
    hero_right_walking2.set_colorkey((0, 0, 0))

    hero_left_walking1 = pygame.image.load('julius_left_walking1.png').convert()
    hero_left_walking1.set_colorkey((0, 0, 0))

    hero_left_walking2 = pygame.image.load('julius_left_walking2.png').convert()
    hero_left_walking2.set_colorkey((0, 0, 0))

    halo1 = pygame.image.load('halo1.png').convert()
    halo1.set_colorkey((255, 255, 255))

    halo2 = pygame.image.load('halo2.png').convert()
    halo2.set_colorkey((255, 255, 255))

    halo3 = pygame.image.load('halo3.png').convert()
    halo3.set_colorkey((255, 255, 255))

    entrance = pygame.image.load('entrance.png').convert()
    entrance.set_colorkey((255, 255, 255))

    exit1 = pygame.image.load('exit.png').convert()
    exit1.set_colorkey((255, 255, 255))

    chest1 = pygame.image.load('chest1.png').convert()
    chest1.set_colorkey((255, 255, 255))

    chest2 = pygame.image.load('chest2.png').convert()
    chest2.set_colorkey((255, 255, 255))

    chest3 = pygame.image.load('chest3.png').convert()
    chest3.set_colorkey((255, 255, 255))
    
    chest4 = pygame.image.load('chest4.png').convert()
    chest4.set_colorkey((255, 255, 255))
    
    heart = pygame.image.load('heart.png').convert()
    
    heart2 = pygame.image.load('heart2.png').convert()

    Big_title = pygame.image.load('Title.png').convert()
    Big_title.set_colorkey((0,0,0))

    rules = pygame.image.load('rules.png').convert()
    rules.set_colorkey((255,255,255))

    return_key = pygame.image.load('return_key.png')
    return_key.set_colorkey((0,0,0))

    arrow_keys = pygame.image.load('arrow_keys.png')
    arrow_keys.set_colorkey((0,0,0))
    
    main_menu=pygame.image.load('main_menu.png').convert()
    main_menu.set_colorkey((0,0,0))
    
    Shop_menu = pygame.image.load('Shop.png').convert()
    Shop_menu.set_colorkey((0,0,0))
    
    coin = pygame.image.load('coin.png').convert()
    coin.set_colorkey((0,0,0))

    end = pygame.image.load('End.png').convert()
    

    #Méthode permettant de vérifier si le personnage a atteint la sortie (renvoie un booléen)

    def check_exit(position_hero):

        # Conversion position hero en matrice

        x = int(position_hero[0]/50)
        y = int(position_hero[1]/50)

        alignx = position_hero[0] % 50
        aligny = position_hero[1] % 50

        if alignx == 0:

            if aligny == 0:

                if int(niveau[y][0][x]) == 4:

                    return True

                else:

                    return False

            else:

                return False
    

    #Méthode permettant de vérifier si le personnage a atteint un coffre (renvoie un booléen)

    def check_chest(position_hero):
        # Conversion position hero en matrice

        x = int(position_hero[0]/50)
        y = int(position_hero[1]/50)

        alignx = position_hero[0] % 50
        aligny = position_hero[1] % 50

        if alignx == 0:

            if aligny == 0:

                if int(niveau[y][0][x]) == 5:
                    niveau[y][0]=niveau[y][0][:x]+"0"+niveau[y][0][x+1:]
                    return True

                else:

                    return False

            else:

                return False


    #Méthode permettant de vérifier si le personnage a atteint un coeur (renvoie un booléen)

    def check_lives(position_hero):
        # Conversion position hero en matrice

        x = int(position_hero[0]/50)
        y = int(position_hero[1]/50)

        alignx = position_hero[0] % 50
        aligny = position_hero[1] % 50

        if alignx == 0:

            if aligny == 0:

                if int(niveau[y][0][x]) == 3:
                    niveau[y][0]=niveau[y][0][:x]+"0"+niveau[y][0][x+1:]
                    return True

                else:

                    return False

            else:

                return False


    #Méthode permettant de vérifier si le déplacement vers le haut est possible (renvoie un booléen)

    def checkmoveup(position_hero):

        # Conversion position hero en matrice

        x = int(position_hero[0]/50)
        y = int(position_hero[1]/50)

        alignx = position_hero[0] % 50
        aligny = position_hero[1] % 50

        # checkmoveup

        if alignx == 0:

            if aligny == 0:

                if int(niveau[y-1][0][x]) == 1:

                    return False

                else:

                    return True

            else:

                if int(niveau[y][0][x]) == 1:

                    return False

                else:

                    return True

        else:

            if aligny == 0:

                if int(niveau[y-1][0][x]) == 1 or int(niveau[y-1][0][x+1]) == 1:

                    return False

                else:

                    return True

            else:

                if int(niveau[y][0][x]) == 1 or int(niveau[y][0][x+1]):

                    return False

                else:

                    return True


    #Même chose vers le bas

    def checkmovedown(position_hero):

        x = int(position_hero[0]/50)
        y = int(position_hero[1]/50)

        alignx = position_hero[0] % 50
        aligny = position_hero[1] % 50

        # checkmovedown

        if alignx == 0:

            if aligny == 0:

                if int(niveau[y+1][0][x]) == 1:

                    return False

                else:

                    return True

            else:

                if int(niveau[y+1][0][x]) == 1:

                    return False

                else:

                    return True

        else:

            if aligny == 0:

                if int(niveau[y+1][0][x]) == 1 or int(niveau[y+1][0][x+1]) == 1:

                    return False

                else:

                    return True

            else:

                if int(niveau[y+1][0][x]) == 1 or int(niveau[y+1][0][x+1] == 1):

                    return False

                else:

                    return True

    #Même chose vers la gauche

    def checkmoveleft(position_hero):

        # Conversion position hero en matrice

        x = int(position_hero[0]/50)
        y = int(position_hero[1]/50)

        alignx = position_hero[0] % 50
        aligny = position_hero[1] % 50

        # checkmoveright

        if alignx == 0:

            if aligny == 0:

                if int(niveau[y][0][x-1]) == 1:

                    return False

                else:

                    return True

            else:

                if int(niveau[y][0][x-1]) == 1 or int(niveau[y+1][0][x-1]) == 1:

                    return False

                else:

                    return True

        else:

            if aligny == 0:

                if int(niveau[y][0][x+1]) == 1:

                    return False

                else:

                    return True

            else:

                if int(niveau[y][0][x+1]) == 1 or int(niveau[y+1][0][x+1] == 1):

                    return False

                else:

                    return True



    #Même chose vers la gauche

    def checkmoveright(position_hero):

        # Conversion position hero en matrice

        x = int(position_hero[0]/50)
        y = int(position_hero[1]/50)

        alignx = position_hero[0] % 50
        aligny = position_hero[1] % 50

        # checkmoveright

        if alignx == 0:

            if aligny == 0:

                if int(niveau[y][0][x+1]) == 1:

                    return False

                else:

                    return True

            else:

                if int(niveau[y][0][x+1]) == 1 or int(niveau[y+1][0][x+1]) == 1:

                    return False

                else:

                    return True

        else:

            if aligny == 0:

                if int(niveau[y][0][x]) == 1:

                    return False

                else:

                    return True

            else:

                if int(niveau[y][0][x]) == 1 or int(niveau[y+1][0][x] == 1):

                    return False

                else:

                    return True


    def Title():
        title = True
        compteur = 0

        while title:
            txt_title_white = font_small.render("Appuyez sur n'importe quelle touche pour continuer ",1 , (255, 255, 255))
            window.blit(txt_title_white, (280, 700))

            if compteur%3==0:

                window.fill((0,0,0))

            window.blit(Big_title,(1,1))   
            pygame.display.update()   
            compteur = compteur +1 
            clock.tick(4)

            for event in pygame.event.get():

                if event.type==pygame.QUIT:

                    pygame.quit()

                elif event.type==pygame.KEYDOWN:
                    window.fill((0,0,0))
                    title = False



    #Méthode d'affichage de la petite histoire
    def Story():
        story = open("story.txt")
        
        for line in story:
            Story = True
            story_message = font_small.render(line.strip(),1,(255,255,255))
            window.fill((0,0,0))
            while Story == True:
                txt_title_white = font_small.render("Appuyez sur n'importe quelle touche pour continuer ",1 , (255, 255, 255))
                window.blit(txt_title_white, (280, 700))
                window.blit(story_message,(100,400)) 
                pygame.display.update()
                for event in pygame.event.get():

                    if event.type==pygame.QUIT:
        
                        pygame.quit()
    
                    elif event.type==pygame.KEYDOWN:
                        Story = False

        story.close()
        


    def SubMenu_Rules():
        submenu_Rules=True
                    
        while submenu_Rules:

            window.blit(rules,(120,1))
            
            rules_message1=font_small_bold.render("Utiliser les fleches pour se deplacer",1,(255,255,255))
            window.blit(rules_message1,(370,330))
            window.blit(arrow_keys,(120,250))
            
            rules_message2=font_small_bold.render("Ouvrir pour obtenir des pieces d'or",1,(255,255,255))
            window.blit(rules_message2,(200,470))
            window.blit(chest4,(560,380))
            
            rules_message3=font_small_bold.render("+1 VIE",1,(255,255,255))
            window.blit(rules_message3,(350,600))
            window.blit(heart2,(450,570))
            
            rules_message4= font_small_bold.render("Pour revenir au menu, appuyer sur ENTREE",1,(255,255,255))
            window.blit(rules_message4,(200,700))
            window.blit(return_key,(670,650))
        
            pygame.display.update()
            
            for event in pygame.event.get():
                
                if event.type==pygame.QUIT:
                    pygame.quit()
                    
                elif event.type==pygame.KEYDOWN:
                    
                    if event.key==pygame.K_RETURN:
                        submenu_Rules=False      


    def Menu():
        Title()
        menu = True
        while menu:
            window.fill((0,0,0))
            window.blit(main_menu,(160,50))
            instructions_start=font_big.render("1. Start",1,(255,255,255))
            instructions_rules=font_big.render("2. Rules",1,(255,255,255))
            instructions_exit=font_big.render("3. Exit",1,(255,255,255))
            window.blit(instructions_start,(300,400))
            window.blit(instructions_rules,(300,500))
            window.blit(instructions_exit,(300,600))
            pygame.display.update() 
            
            for event in pygame.event.get():
                
                if event.type==pygame.QUIT:
                    pygame.quit()
                    
                elif event.type==pygame.KEYDOWN:
                    
                    if event.key == pygame.K_1 or event.key == pygame.K_KP1:
                        Story()
                        menu=False
                        
                    elif event.key==pygame.K_2 or event.key == pygame.K_KP2: 
                        window.fill((0,0,0))
                        SubMenu_Rules()
                                        
                    elif event.key==pygame.K_3 or event.key == pygame.K_KP3:
                        pygame.quit()
                    

    def Shop(gold,speed):
        
        while Shop:
            window.fill((0,0,0))
            window.blit(Shop_menu,(130,50))
            PO = font_big.render(str(gold), 1, (255, 255, 255))
            window.blit(coin,(400,250))
            window.blit(PO,(460,250))
            shop_message1 = font_medium.render("1. Acheter des bottes de vitesse (100 PO)", 1, (255, 255,255))
            window.blit(shop_message1,(100,380))
            shop_message2 = font_medium.render("2. Acheter des bottes de super-vitesse (400 PO)", 1, (255, 255,255))
            window.blit(shop_message2,(100,480))
            shop_message3 = font_medium.render("3. Exit",1,(255,255,255))
            window.blit(shop_message3,(400,580))
            pygame.display.update()
            
            for event in pygame.event.get():
                
                if event.type == pygame.KEYDOWN:
                    
                    if event.key == pygame.K_1 or event.key == pygame.K_KP1:
                        
                        if gold < 100:
                            fonds_insuffisants = font_small_bold.render("Trop cher pour toi", 1, (255, 0,0))
                            window.blit(fonds_insuffisants,(400,700))
                            pygame.display.update()
                            pygame.time.delay(500)
                            
                        else:
                            bottes_vitesse = font_small_bold.render("Bottes de vitesse obtenues", 1, (0, 255,0))
                            window.blit(bottes_vitesse,(350,700))
                            pygame.display.update()
                            gold = gold -100
                            speed = 30
                            pygame.time.delay(1000)
                            
                    elif event.key==pygame.K_2 or event.key == pygame.K_KP2 :
                        
                        if gold < 400:
                            fonds_insuffisants_2 = font_small_bold.render("Tu te fous de moi?", 1, (255, 0,0))
                            window.blit(fonds_insuffisants_2,(400,700))
                            pygame.display.update()
                            pygame.time.delay(500)
                            
                        else:
                            gold = gold -200
                            speed = 40
                            bottes_super_vitesse = font_small_bold.render("Wahou! Tu vas aller super vite", 1, (0, 255,0))
                            window.blit(bottes_super_vitesse,(350,700))
                            pygame.display.update()
                            pygame.time.delay(1000)
                            
                            
                    if event.key==pygame.K_3 or event.key == pygame.K_KP3 :

                        return gold,speed


    #Initialisation de l'horloge
    clock = pygame.time.Clock()  

    #Lancement du menu
    Menu()

    #Initialisation de la vitesse de déplacement du personnage
    speed = 20

    #Initialisation du nombre de pièces d'or du personnage
    gold=0

    #Initialisation du nombre de coeur du personnage
    lives = 0
    
    # Récupération du niveau
    for nv in range(1,11):

        lvl = open("level"+str(nv)+".txt")

        niveau = [ligne.split() for ligne in lvl]

        lvl.close()

        # Affichage du niveau

        for i in range(len(niveau)):

            ligne = niveau[i]

            for j in range(len(ligne[0])):

                if int(ligne[0][j]) == 2:

                    hero = hero_down

                    starting_position = hero.get_rect(topleft=(j*50, i*50))

                    position_hero = starting_position

                    window.blit(hero, position_hero)

        

        game = True
        compteur =0
        light = False
            

        walk = 0
        gameover= False
        shop=True


        try:

            while game:
                if shop == True:
                    if nv%3==0:
                        #Variable permettant de récupérer les nouvelles valeurs de gold et speed
                        a = Shop(gold,speed)
                        speed = a[1]
                        gold = a[0]
                        shop = False


                while light==False:

                    txt_intro_white = font_small.render("Appuyez sur espace pour allumer la lumiere " , 1, (255, 255, 255))
                    window.blit(txt_intro_white, (300, 400))

                    if compteur%3==0:
                        window.fill((0,0,0))

                    hero = hero_down
                    window.blit(hero, position_hero)
                        
                    pygame.display.update()   
                    compteur = compteur +1 
                    clock.tick(4)
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_SPACE:
                                light = True
                                pause = 0
                                start = pygame.time.get_ticks()
                                

                #Calcule le timer
                countdown = (20000-nv*1000 - pygame.time.get_ticks()+start+pause)/1000

                #Déplacement du personnage quand la touche est pressée
                pressed = pygame.key.get_pressed()

                #si la touche pressée est la flèche du bas
                if pressed[pygame.K_DOWN]:

                    #on vérifie que le déplacement est possible
                    if checkmovedown(position_hero) == True:

                        if walk % 3 == 0:

                            hero = hero_down_walking1

                        elif walk % 3 == 1:

                            hero = hero_down_walking2

                        elif walk % 3 == 2:

                            hero = hero_down

                        position_hero = position_hero.move(0, 10)

                if pressed[pygame.K_UP]:

                    if checkmoveup(position_hero) == True:

                        if walk % 3 == 0:

                            hero = hero_up_walking1

                        elif walk % 3 == 1:

                            hero = hero_up_walking2

                        elif walk % 3 == 2:

                            hero = hero_up

                        position_hero = position_hero.move(0, -10)

                if pressed[pygame.K_LEFT]:

                    if checkmoveleft(position_hero) == True:

                        if walk % 3 == 0:

                            hero = hero_left_walking1

                        elif walk % 3 == 1:

                            hero = hero_left_walking2

                        elif walk % 3 == 2:

                            hero = hero_left

                        position_hero = position_hero.move(-10, 0)

                if pressed[pygame.K_RIGHT]:

                    if checkmoveright(position_hero) == True:

                        if walk % 3 == 0:

                            hero = hero_right_walking1

                        elif walk % 3 == 1:

                            hero = hero_right_walking2

                        elif walk % 3 == 2:

                            hero = hero_right

                        position_hero = position_hero.move(10, 0)

                # Changement de l'etat de marche

                walk += 1

                # Gestion des évenements
                for event in pygame.event.get():

                    if event.type == pygame.QUIT:

                        game = False
                        gameover=True

                    if event.type == pygame.KEYDOWN:

                        if event.key == pygame.K_ESCAPE:

                            game = False

                        if event.key == pygame.K_UP:

                            hero = hero_up_walking1

                        if event.key == pygame.K_DOWN:

                            hero = hero_down_walking1

                        if event.key == pygame.K_LEFT:

                            hero = hero_left_walking1

                        if event.key == pygame.K_RIGHT:

                            hero = hero_right_walking1

                    # Changement d'image du hero lorsqu'on relache les touches de direction

                    if event.type == pygame.KEYUP:

                        if event.key == pygame.K_ESCAPE:

                            game = False

                        if event.key == pygame.K_UP:

                            hero = hero_up

                        if event.key == pygame.K_DOWN:

                            hero = hero_down

                        if event.key == pygame.K_LEFT:

                            hero = hero_left

                        if event.key == pygame.K_RIGHT:

                            hero = hero_right

                # Chargement du background

                window.fill((0, 0, 0))

                # Chargement des murs, des coffres, des coeurs et de leurs animations

                for i in range(len(niveau)):

                    ligne = niveau[i]

                    for j in range(len(ligne[0])):

                        if (int(ligne[0][j])) == 1:

                            window.blit(wall, (j*50, i*50))

                        if (int(ligne[0][j])) == 2:

                            window.blit(entrance, (j*50, i*50))

                        if (int(ligne[0][j])) == 3:

                            if walk % 3 == 0:

                                window.blit(halo1, (j*50, i*50))

                            elif walk % 3 == 1:

                                window.blit(halo2, (j*50, i*50))

                            else:

                                window.blit(halo3, (j*50, i*50))

                        if (int(ligne[0][j])) == 4:

                            window.blit(exit1, (j*50, i*50))

                        if (int(ligne[0][j])) == 5:

                            if walk % 3 == 0:

                                window.blit(chest1, (j*50, i*50))

                            elif walk % 3 == 1:

                                window.blit(chest2, (j*50, i*50))

                            else:

                                window.blit(chest3, (j*50, i*50))

                # Affichage du hero
                window.blit(hero, position_hero)

                # Affichage du level
                label = font_big.render("Niveau " + str(nv), 1, (255, 255, 255))
                window.blit(label, (750, 5))

                # Affichage du timer
                timer = font_big.render(str(countdown), 1, (255, 255, 255))
                window.blit(timer, (400, 5))

                # Affichage des golds
                PO = font_big.render(str(gold), 1, (255, 255, 255))
                window.blit(coin,(200,0))
                window.blit(PO,(260,5))
                
                
                #Affichage du nombre de vies
                if lives == 1:
                    window.blit(heart,(0,0))
                elif lives ==2:
                    window.blit(heart,(0,0))
                    window.blit(heart,(50,0))
                elif lives ==3:
                    window.blit(heart,(0,0))
                    window.blit(heart,(50,0))
                    window.blit(heart,(100,0))


                #Rafraichissement de la fenêtre
                pygame.display.update()

                #Appelle check_chest, si le personnage est sur un coffre, le coffre lui donne un montant d'or aléatoire entre 1 et 100
                if check_chest(position_hero)==True:
                    value = random.randint(1,100)
                    gold = gold + value
                    chest_message = font_big.render("+" + str(value) + " PO", 1, (255, 255,0))
                    window.blit(chest_message,(380,380))
                    pygame.display.update()   
                    pygame.time.delay(1500)
                    pause = pause + 1500

                #Appelle check_lives, seulement si le personnage a moins de 3 vies et ajoute au compteur de vies
                if lives <3:
                     if check_lives(position_hero)==True:
                        heart_message = font_big.render("+1 Life", 1, (255, 0,0))
                        lives +=1
                        window.blit(heart_message,(380,380))
                        pygame.display.update() 
                        pygame.time.delay(1500)
                        pause =pause + 1500
                    
                # Appelle check_exit, si le personnage se trouve sur la sortie, affiche un message de réussite du niveau
                if check_exit(position_hero)==True:
                    window.fill((0,0,0))
                    success_message = font_big.render("SUCCESS", 1, (0, 255,0))
                    window.blit(success_message,(380,380))
                    pygame.display.update()   
                    pygame.time.delay(1500)
                    #Si le joueur est au dernier niveau, affiche l'image de fin
                    if nv == 10:
                        window.blit(end,(0,0))
                        pygame.display.update() 
                        pygame.time.delay(2000)
                    game=False

                # Si le timer arrive à 0, affiche un message de défaite et retire une vie
                if countdown <=0:
                    lives = lives -1
                    window.fill((0,0,0))
                    # Le jeu continue si le personnage a encore une vie
                    if lives >=0:
                        failure_message = font_big.render("FAILURE", 1, (255, 0,0))
                        window.blit(failure_message,(380,380))
                    # Sinon le jeu s'arrête, on affiche game over
                    else:
                        game_over_message = font_big.render("GAME OVER", 1, (255, 0,0))
                        window.blit(game_over_message,(380,380))
                        gameover = True
                        game = False

                    # Dans le cas où on a échoué, et qu'il nous reste au moins une vie, on retroune dans la boucle light, on reinitialise le compteur à 0 et la position de Julius est celle de départ
                    pygame.display.update()
                    pygame.time.delay(2000)
                    compteur = 0
                    position_hero=starting_position
                    light = False
                  

                # Permet de boucler un nombre de fois par seconde = speed, plus ce nombre est élevé, plus le personnage bougera rapidement puisque la fréquence de son déplacement est plus rapide.
                clock.tick(speed)

            if gameover==True:
                pygame.quit()


                


        except SystemExit:

            pygame.quit()
