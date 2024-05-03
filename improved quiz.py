import pygame
import os

pygame.init()

# Define questions and options
questions = [
    "What is the national game of India?",
    "Total number of gold medals won by the Indian hockey team in Olympics?",
    "Year of the last Olympic gold medal won by the Indian Hockey Team?",
    "Who was the first individual Olympic medal winner from independent India?",
    "When were the Asian Games last held in India?",
    "Who among the following is known as the Flying Sikh of India?"
]

options = [
    ["Hockey", "Cricket", "Kabaddi", "None of these"],
    [8, 12, 6, 9],
    [1980, 1964, 1972, 1992],
    ["KD Jadhav", "Harihar Banerjee", "Pradip Bode", "None of the above"],
    [1982, 1990, 2010, 2014],
    ["Milkha Singh", "PT Usha", "Sachin Tendulkar", "Dhyan Chand"]
]

# Correct answers
answers = [0, 1, 0, 0, 1, 0]

# Colors
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
green = (1, 150, 96)

# Screen dimensions
screen_width = 1170
screen_height = 700

# Set up the game window
gameWindow = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Quiz")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 40)  # Adjusted font size

# Function to display text on screen
def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x, y])
def text_screen_in_mid(text,textcolor,y):
    text = font.render(text, True, textcolor, white)
    textRect = text.get_rect()
    # set the center of the rectangular object.
    textRect.center = (screen_width // 2,y)
    gameWindow.blit(text, textRect)
# Function for the welcome screen
def welcome_screen():
    exit_welcome = False
    while not exit_welcome:
        gameWindow.fill(white)
        text_screen_in_mid("Welcome to the Quiz!", black, 200)
        text_screen_in_mid("Press SPACE to start the quiz", black,600)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_welcome = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return

        pygame.display.update()
        clock.tick(30)

# Main function to run the game
def quiz_game():
    welcome_screen()
    
    exit_game = False
    current_question = 0
    score = 0
    attempted = 0
    incorrect = 0
    skipped = 0

    # Load high score
    if not os.path.exists("hiscore.txt"):
        with open("hiscore.txt", "w") as f:
            f.write("0")

    with open("hiscore.txt", "r") as f:
        hiscore = int(f.read())

    while not exit_game:
        gameWindow.fill(white)

        text_screen("Correct: " + str(score), green, 5, 5)
        text_screen("                     Incorrect: " + str(incorrect), red,5, 5)
        text_screen("                                             Skipped: " + str(skipped) , red, 5, 5)
        text_screen("                                                                    High Score: "+ str(hiscore), black,5, 5)
        # Display current question
        text_screen("Q" + str(current_question + 1)+")  "+questions[current_question], black, 5, 70)

        # Display options
        for i in range(4):
            text_screen(str(i + 1) + ") " + str(options[current_question][i]), black, 40, 110 + 50 * i)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    attempted += 1
                    if answers[current_question] == 0:
                        score += 1
                    else:
                        incorrect += 1
                    current_question += 1
                if event.key == pygame.K_2:
                    attempted += 1
                    if answers[current_question] == 1:
                        score += 1
                    else:
                        incorrect += 1
                    current_question += 1
                if event.key == pygame.K_3:
                    attempted += 1
                    if answers[current_question] == 2:
                        score += 1
                    else:
                        incorrect += 1
                    current_question += 1
                if event.key == pygame.K_4:
                    attempted += 1
                    if answers[current_question] == 3:
                        score += 1
                    else:
                        incorrect += 1
                    current_question += 1
                if event.key == pygame.K_ESCAPE:
                    skipped += 1
                    current_question += 1

        # Check if all questions are answered
        if current_question >= len(questions):
            exit_game = True

        pygame.display.update()
        clock.tick(30)

    # Update high score if needed
    if score > hiscore:
        hiscore = score
        with open("hiscore.txt", "w") as f:
            f.write(str(hiscore))

    # Display end screen with option to exit
    exit_end_screen = False
    while not exit_end_screen:
        gameWindow.fill(white)
        text_screen_in_mid("Quiz Over!", black, 150)
        text_screen("Questions Attempted: " + str(attempted), black, 304, 200)
        text_screen("Score: " + str(score), green, 304, 250)
        text_screen("High Score: " + str(hiscore), black, 651, 250)
        text_screen("Questions Incorrect: " + str(incorrect), red, 304, 300)
        text_screen("Questions Skipped: " + str(skipped), black, 304, 350)
        text_screen_in_mid("Press SPACE to play again or ESC to exit", black, 550)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_end_screen = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    quiz_game()  # Start a new game
                elif event.key == pygame.K_ESCAPE:
                    exit_game = True
                    exit_end_screen = True

        pygame.display.update()
        clock.tick(30)

    pygame.quit()
    quit()

# Run the quiz game
quiz_game()
