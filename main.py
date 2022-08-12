import pygame
import os
pygame.init()
q1 = "what is the national game of india"
q2 = "total no of gold medals won by indian hockey team in olympics"
q3 = "Last Olympic gold medal won Indian Hockey Team at"
q4 = "First Individual Olympic medal winner from independent India"
q5 = "Asian Games Last held in India"
q6 = "Who among the following is known as Flying Sikh of India"
questions = [[q1,["hockey","cricket","kabaddi","none of these"],], [q2,[8,12,6,9]], [q3,[1980,1964,1972,1992]], [q4,["kd jadav","harihar banerjee","pradip bode","none of tha above" ]], [q5,[]], [q6,[]]]
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
green = (1, 150, 96)
screen_width = 1280
screen_height = 800
gameWindow = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("quiz")
pygame.display.update()
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 55)
def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x,y])
def welcome():
    exit_game = False
    while not exit_game:
        gameWindow.fill((233,210,229))
        text_screen("WELCOME TO QUIZ", black, 235, 100)
        text_screen("RULES:", black, 235, 250)
        text_screen("PRESS 1 FOR FIRST OPTION", black, 235, 300)
        text_screen("PRESS 2 FOR SECOND OPTION", black, 235, 350)
        text_screen("PRESS 3 FOR THIRD OPTION", black, 235, 400)
        text_screen("PRESS 4 FOR FORTH OPTION", black, 235, 450)
        text_screen("PRESS SPACE TO PLAY", black, 235, 640)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    gameloop()
        pygame.display.update()
        clock.tick(60)
def gameloop():
    exit_game = False
    game_over = False
    n=0
    if not os.path.exists("hiscore.txt"):
        with open("hiscore.txt", "w") as f:
            f.write("0")
    with open("hiscore.txt", "r") as f:
        hiscore = f.read()
    score = 0
    attempted=0
    incorrect=0
    skipped=0
    fps = 60
    while not exit_game:
        if game_over:
            with open("hiscore.txt", "w") as f:
                f.write(str(hiscore))
            gameWindow.fill(white)
            text_screen("Score: " + str(score)+"attempted"+str(attempted) +"skipped"+str(skipped) + "  Hiscore: "+str(hiscore), black, 100, 100)
            text_screen("Quiz Over! Press Enter To Continue", red, 100, 250)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome()
        else:

            gameWindow.fill(white)
            text_screen("Score: " + str(score) + "attempted:" + str(attempted)+"skipped:"+ str(skipped)+"incorrect:"+str(incorrect), black, 5, 5)
            text_screen("Q)"+str(questions[n][0]), black, 5, 45)
            text_screen("1)"+str(questions[n][1][0]), black, 5, 105)
            text_screen("2)"+str(questions[n][1][1]), black, 5, 145)
            text_screen("3)"+str(questions[n][1][2]), black, 5, 185)
            text_screen("4)"+str(questions[n][1][3]), black, 5, 225)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        text_screen("question correct", black, 5, 5)
                        score +=1
                        attempted+=1
                        n+=1
                        clock.tick(fps)
                        continue
                    if event.key == pygame.K_ESCAPE:
                        text_screen("question skipped", black, 5, 5)
                        clock.tick(fps)
                        skipped+=1
                        n+=1
                        continue
                    else:
                        n+=1
                        clock.tick(fps)
                        attempted+=1
                        incorrect+=1
                        continue
            text_screen("Score: " + str(score) + "attempted:" + str(attempted) + "skipped:" + str(skipped), black, 5, 5)
        pygame.display.update()
        clock.tick(fps)
    pygame.quit()
    quit()
welcome()
