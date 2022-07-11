import copy

import pygame
from tkinter import *

record = [
    ['b2', 'b3', 'b4', 'b5', 'b6', 'b4', 'b3', 'b2'],
    ['b1', 'b1', 'b1', 'b1', 'b1', 'b1', 'b1', 'b1'],
    ['0', '0', '0', '0', '0', '0', '0', '0'],
    ['0', '0', '0', '0', '0', '0', '0', '0'],
    ['0', '0', '0', '0', '0', '0', '0', '0'],
    ['0', '0', '0', '0', '0', '0', '0', '0'],
    ['w1', 'w1', 'w1', 'w1', 'w1', 'w1', 'w1', 'w1'],
    ['w2', 'w3', 'w4', 'w5', 'w6', 'w4', 'w3', 'w2']]

mid_r = copy.deepcopy(record)
true_mid_r = copy.deepcopy(record)

# Create the screen
pygame.init()

# Set the screen
screen = pygame.display.set_mode((456, 456))
pygame.display.set_caption('Chess')
pygame.display.set_icon(pygame.image.load('icon.png'))

# Chess pieces
# - White
w_pawn = pygame.image.load('white/pawn.png')
w_knight = pygame.image.load('white/knight.png')
w_rook = pygame.image.load('white/rook.png')
w_bishop = pygame.image.load('white/bishop.png')
w_queen = pygame.image.load('white/queen.png')
w_king = pygame.image.load('white/king.png')

# - Black
b_pawn = pygame.image.load('black/pawn.png')
b_knight = pygame.image.load('black/knight.png')
b_rook = pygame.image.load('black/rook.png')
b_bishop = pygame.image.load('black/bishop.png')
b_queen = pygame.image.load('black/queen.png')
b_king = pygame.image.load('black/king.png')

# Set the background
bg = pygame.image.load('background.png')

N_pawn = str


def promotion(pt):
    global N_pawn

    if pt[0] == 'w':
        type = 'white'
    elif pt[0] == 'b':
        type = 'black'

    root = Tk()
    root.title('Promotion')
    root.iconbitmap('s_icon.ico')

    r = StringVar()
    r.set(f'{pt[0]}5')

    def clicked(r):
        global N_pawn
        N_pawn = r
        root.destroy()

    Label(root, text=f'Choose what will your {type} pawn be promoted to: ').pack()

    Radiobutton(root, text='Queen', variable=r, value=f'{pt[0]}5').pack(anchor='w')
    Radiobutton(root, text='Rook', variable=r, value=f'{pt[0]}2').pack(anchor='w')
    Radiobutton(root, text='Bishop', variable=r, value=f'{pt[0]}4').pack(anchor='w')
    Radiobutton(root, text='Knight', variable=r, value=f'{pt[0]}3').pack(anchor='w')

    Button(root, text='Choose', command=lambda: clicked(r.get())).pack()

    mainloop()


black_turn = False
using_white = bool
running = True
is_w_king_moved, is_b_king_moved, is_w_lrook_moved, is_b_lrook_moved, is_w_rrook_moved, is_b_rrook_moved = [False] * 6

while running:
    is_b_king, is_w_king = [False] * 2

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            mouse_x = mouse_pos[0] // 57
            mouse_y = mouse_pos[1] // 57
            if record[mouse_y][mouse_x][0] == 'w':
                using_white = True
            if record[mouse_y][mouse_x][0] == 'b':
                using_white = False

        if event.type == pygame.MOUSEBUTTONUP:
            mouse_pos = pygame.mouse.get_pos()
            mouse_x_2 = mouse_pos[0] // 57
            mouse_y_2 = mouse_pos[1] // 57
            if (mouse_y != mouse_y_2 or mouse_x != mouse_x_2) and (record[mouse_y][mouse_x] != '0'):
                if record[mouse_y_2][mouse_x_2][0] != record[mouse_y][mouse_x][0]:
                    if (record[mouse_y][mouse_x][0] == 'w' and not black_turn) or (
                            record[mouse_y][mouse_x][0] != 'w' and black_turn):
                        can_move = False

                        # If player is moving a pawn
                        if record[mouse_y][mouse_x][1] == '1':
                            first_go = False

                            # If player is moving a white pawn
                            if using_white:
                                # Checking if the white pawn is having its first move or not
                                if mouse_y == 6:
                                    first_go = True

                                # If it is the white pawn first move
                                if first_go:
                                    # Checking if player can put the white pawn at destination or not
                                    if mouse_y_2 == mouse_y - 2:
                                        if mouse_x_2 == mouse_x:
                                            for i in range(mouse_y_2 - 1, mouse_y):
                                                can_move = True
                                                if record[i][mouse_x][0] != '0':
                                                    can_move = False
                                                    break

                                    elif mouse_y_2 == mouse_y - 1:
                                        if mouse_x_2 == mouse_x - 1 or mouse_x_2 == mouse_x + 1:
                                            if record[mouse_y_2][mouse_x_2][0] == 'b':
                                                can_move = True
                                        elif mouse_x == mouse_x_2 and record[mouse_y_2][mouse_x_2] == '0':
                                            can_move = True

                                # If it is not the white pawn first move
                                elif not first_go:

                                    # Checking if player can put the white pawn at destination or not
                                    if mouse_y_2 == mouse_y - 1:
                                        if mouse_x_2 == mouse_x:
                                            if record[mouse_y_2][mouse_x][0] == '0':
                                                can_move = True

                                        elif mouse_x_2 == mouse_x - 1 or mouse_x_2 == mouse_x + 1:
                                            if record[mouse_y_2][mouse_x_2][0] == 'b':
                                                can_move = True

                                            elif mouse_y_2 == 2:
                                                if record[mouse_y_2 + 1][mouse_x_2] == 'b1':
                                                    if mid_r[mouse_y_2 - 1][mouse_x_2] == 'b1':
                                                        record[mouse_y_2 + 1][mouse_x_2] = '0'
                                                        can_move = True

                                        if mouse_y_2 == 0:
                                            promotion(record[mouse_y][mouse_x])
                                            record[mouse_y][mouse_x] = N_pawn
                                            can_move = True

                            # If player is moving a black pawn
                            elif not using_white:

                                # Checking if the black pawn is having its first move or not
                                if mouse_y == 1:
                                    first_go = True

                                # If it is the black pawn first move
                                if first_go:

                                    # Checking if player can put the black pawn at destination or not
                                    if mouse_y_2 == mouse_y + 2:
                                        if mouse_x_2 == mouse_x:
                                            for i in range(mouse_y + 1, mouse_y_2 + 1):
                                                can_move = True
                                                if record[i][mouse_x][0] != '0':
                                                    can_move = False
                                                    break

                                    elif mouse_y_2 == mouse_y + 1:
                                        if mouse_x_2 == mouse_x - 1 or mouse_x_2 == mouse_x + 1:
                                            if record[mouse_y_2][mouse_x_2][0] == 'w':
                                                can_move = True
                                        elif mouse_x == mouse_x_2 and record[mouse_y_2][mouse_x_2] == '0':
                                            can_move = True

                                # If it is not the black pawn first move
                                elif not first_go:

                                    # Checking if player can put the black pawn at destination or not
                                    if mouse_y_2 == mouse_y + 1:
                                        if mouse_x_2 == mouse_x:
                                            if record[mouse_y_2][mouse_x][0] == '0':
                                                can_move = True

                                        elif mouse_x_2 == mouse_x - 1 or mouse_x_2 == mouse_x + 1:
                                            if record[mouse_y_2][mouse_x_2][0] == 'w':
                                                can_move = True

                                            elif mouse_y_2 == 5:
                                                if record[mouse_y_2 - 1][mouse_x_2] == 'w1':
                                                    if mid_r[mouse_y_2 + 1][mouse_x_2] == 'w1':
                                                        record[mouse_y_2 - 1][mouse_x_2] = '0'

                                                        can_move = True

                                        if mouse_y_2 == 7:
                                            promotion(record[mouse_y][mouse_x])
                                            record[mouse_y][mouse_x] = N_pawn
                                            can_move = True

                        # If player is moving a rook
                        elif record[mouse_y][mouse_x][1] == '2':

                            # If the rook is moving lengthwise (Up down)
                            if mouse_x_2 == mouse_x:
                                can_move = True
                                # If the rook is moving up, check if it can be put at destination or not
                                if mouse_y_2 < mouse_y:
                                    for i in range(mouse_y_2 + 1, mouse_y):
                                        if record[i][mouse_x][0] != '0':
                                            can_move = False

                                # If the rook is moving down, check if it can be put at destination or not
                                elif mouse_y_2 > mouse_y:
                                    for i in range(mouse_y + 1, mouse_y_2):
                                        if record[i][mouse_x][0] != '0':
                                            can_move = False

                            # If the rook is moving horizontally (Left right)
                            elif mouse_y_2 == mouse_y:
                                can_move = True

                                # If the rook is moving left, check if it can be put at destination or not
                                if mouse_x_2 < mouse_x:
                                    for i in range(mouse_x_2 + 1, mouse_x):
                                        if record[mouse_y_2][i][0] != '0':
                                            can_move = False

                                # If the rook is moving right, check if it can be put at destination or not
                                elif mouse_x_2 > mouse_x:
                                    can_move = True
                                    for i in range(mouse_x + 1, mouse_x_2):
                                        if record[mouse_y_2][i][0] != '0':
                                            can_move = False
                                if can_move:
                                    if mouse_y == 0 and mouse_x == 0:
                                        is_b_lrook_moved = True
                                    elif mouse_y == 0 and mouse_x == 7:
                                        is_b_rroot_moved = True

                                    elif mouse_y == 7 and mouse_x == 0:
                                        is_w_lrook_moved = True
                                    elif mouse_y == 7 and mouse_x == 7:
                                        is_w_rroot_moved = True

                        # If player is moving a knight
                        elif record[mouse_y][mouse_x][1] == '3':

                            # Check if player can put the knight at destination or not
                            if ((mouse_y_2 == mouse_y - 2 and mouse_x_2 == mouse_x + 1) or (
                                    mouse_y_2 == mouse_y - 2 and mouse_x_2 == mouse_x - 1) or (
                                        mouse_y_2 == mouse_y + 2 and mouse_x_2 == mouse_x + 1) or (
                                        mouse_y_2 == mouse_y + 2 and mouse_x_2 == mouse_x - 1)) \
                                    or \
                                    ((mouse_y_2 == mouse_y - 1 and mouse_x_2 == mouse_x + 2) or (
                                            mouse_y_2 == mouse_y - 1 and mouse_x_2 == mouse_x - 2) or (
                                             mouse_y_2 == mouse_y + 1 and mouse_x_2 == mouse_x - 2) or (
                                             mouse_y_2 == mouse_y + 1 and mouse_x_2 == mouse_x + 2)):
                                can_move = True

                        # If player is moving a bishop
                        elif record[mouse_y][mouse_x][1] == '4':

                            # Check if the bishop's movement is correct or not
                            if abs(mouse_y_2 - mouse_y) == abs(mouse_x_2 - mouse_x):
                                can_move = True

                                # Down right
                                if mouse_y_2 > mouse_y and mouse_x_2 > mouse_x:
                                    i = 1
                                    while mouse_y + i < mouse_y_2 and mouse_x + 1 < mouse_x_2:
                                        if record[mouse_y + i][mouse_x + i][0] != '0':
                                            can_move = False
                                            break
                                        i += 1

                                # Up left
                                elif mouse_y_2 < mouse_y and mouse_x_2 < mouse_x:
                                    i = 1
                                    while mouse_y - i > mouse_y_2 and mouse_x - 1 > mouse_x_2:
                                        if record[mouse_y - i][mouse_x - i][0] != '0':
                                            can_move = False
                                            break
                                        i += 1

                                # Down left
                                elif mouse_y_2 > mouse_y and mouse_x_2 < mouse_x:
                                    i = 1
                                    while mouse_y + i < mouse_y_2 and mouse_x - 1 > mouse_x_2:
                                        if record[mouse_y + i][mouse_x - i][0] != '0':
                                            can_move = False
                                            break
                                        i += 1

                                # Up right
                                elif mouse_y_2 < mouse_y and mouse_x_2 > mouse_x:
                                    i = 1
                                    while mouse_y - i > mouse_y_2 and mouse_x + 1 < mouse_x_2:
                                        if record[mouse_y - i][mouse_x + i][0] != '0':
                                            can_move = False
                                            break
                                        i += 1

                        # If player is moving a queen
                        elif record[mouse_y][mouse_x][1] == '5':

                            # Move like a rook

                            # Check if the queen is moving lengthwise (Up down) or not
                            if mouse_x_2 == mouse_x:

                                # Up
                                if mouse_y_2 < mouse_y:
                                    can_move = True
                                    for i in range(mouse_y_2 + 1, mouse_y):
                                        if record[i][mouse_x][0] != '0':
                                            can_move = False

                                # Down
                                elif mouse_y_2 > mouse_y:
                                    can_move = True
                                    for i in range(mouse_y + 1, mouse_y_2):
                                        if record[i][mouse_x][0] != '0':
                                            can_move = False

                            # Check if the queen is moving horizontally (left right) or not
                            elif mouse_y_2 == mouse_y:
                                can_move = True

                                # Left
                                if mouse_x_2 < mouse_x:
                                    for i in range(mouse_x_2 + 1, mouse_x):
                                        if record[mouse_y_2][i][0] != '0':
                                            can_move = False

                                # Right
                                elif mouse_x_2 > mouse_x:
                                    can_move = True
                                    for i in range(mouse_x + 1, mouse_x_2):
                                        if record[mouse_y_2][i][0] != '0':
                                            can_move = False

                            # Move like a bishop
                            if abs(mouse_y_2 - mouse_y) == abs(mouse_x_2 - mouse_x):
                                can_move = True

                                # Down right
                                if mouse_y_2 > mouse_y and mouse_x_2 > mouse_x:
                                    i = 1
                                    while mouse_y + i < mouse_y_2 and mouse_x + 1 < mouse_x_2:
                                        if record[mouse_y + i][mouse_x + i][0] != '0':
                                            can_move = False
                                            break
                                        i += 1

                                # Up left
                                elif mouse_y_2 < mouse_y and mouse_x_2 < mouse_x:
                                    i = 1
                                    while mouse_y - i > mouse_y_2 and mouse_x - 1 > mouse_x_2:
                                        if record[mouse_y - i][mouse_x - i][0] != '0':
                                            can_move = False
                                            break
                                        i += 1

                                # Down left
                                elif mouse_y_2 > mouse_y and mouse_x_2 < mouse_x:
                                    i = 1
                                    while mouse_y + i < mouse_y_2 and mouse_x - 1 > mouse_x_2:
                                        if record[mouse_y + i][mouse_x - i][0] != '0':
                                            can_move = False
                                            break
                                        i += 1

                                # Up right
                                elif mouse_y_2 < mouse_y and mouse_x_2 > mouse_x:
                                    i = 1
                                    while mouse_y - i > mouse_y_2 and mouse_x + 1 < mouse_x_2:
                                        if record[mouse_y - i][mouse_x + i][0] != '0':
                                            can_move = False
                                            break
                                        i += 1

                        # If player is moving a king
                        elif record[mouse_y][mouse_x][1] == '6':
                            # Basic movement
                            if (mouse_y_2 == mouse_y + 1 or mouse_y_2 == mouse_y - 1 or mouse_y_2 == mouse_y) \
                                    and (mouse_x_2 == mouse_x + 1 or mouse_x_2 == mouse_x - 1 or mouse_x_2 == mouse_x):
                                can_move = True
                                if record[mouse_y][mouse_x][0] == 'w':
                                    is_w_king_moved = True
                                if record[mouse_y][mouse_x][0] == 'b':
                                    is_b_king_moved = True

                            # Castling
                            if mouse_y == mouse_y_2:
                                # Black side
                                if record[mouse_y][mouse_x] == 'b6' and not is_b_king_moved:
                                    if mouse_x_2 == mouse_x + 2:
                                        if not is_b_rrook_moved:
                                            if record[mouse_y][mouse_x + 1] == '0' and record[mouse_y][
                                                mouse_x + 2] == '0' \
                                                    and record[0][7] == 'b2':
                                                record[mouse_y_2][mouse_x + 1] = record[0][7]
                                                record[0][7] = '0'

                                                can_move = True

                                    elif mouse_x_2 == mouse_x - 2:
                                        if not is_b_lrook_moved:
                                            if record[mouse_y][mouse_x + 1] == '0' and record[mouse_y][
                                                mouse_x + 2] == '0' \
                                                    and record[0][0] == 'b2':
                                                record[mouse_y_2][mouse_x - 1] = record[0][0]
                                                record[0][0] = '0'

                                                can_move = True

                                # White side
                                elif record[mouse_y][mouse_x] == 'w6' and not is_w_king_moved:
                                    if mouse_x_2 == mouse_x + 2:
                                        if not is_w_rrook_moved:
                                            if record[mouse_y][mouse_x + 1] == '0' and record[mouse_y][
                                                mouse_x + 2] == '0' \
                                                    and record[7][7] == 'w2':
                                                record[mouse_y_2][mouse_x + 1] = record[7][7]
                                                record[7][7] = '0'

                                                can_move = True

                                    elif mouse_x_2 == mouse_x - 2:
                                        if not is_w_lrook_moved:
                                            if record[mouse_y][mouse_x + 1] == '0' and record[mouse_y][
                                                mouse_x + 2] == '0' \
                                                    and record[7][0] == 'w2':
                                                record[mouse_y_2][mouse_x - 1] = record[7][0]
                                                record[7][0] = '0'

                                                can_move = True

                        # Moving the pieces
                        if can_move:
                            # Save a copy of the record before change it
                            mid_r = copy.deepcopy(record)

                            # Change the record value
                            record[mouse_y_2][mouse_x_2] = record[mouse_y][mouse_x]
                            record[mouse_y][mouse_x] = '0'
                            black_turn = not black_turn
                            can_go_back = True

    # Display the background
    screen.fill((225, 225, 225))
    screen.blit(bg, (0, 0))

    for i in range(0, 8):
        for j in range(0, 8):
            # White
            if record[i][j] == 'w1':
                screen.blit(w_pawn, (j * 57, i * 57))
            if record[i][j] == 'w2':
                screen.blit(w_rook, (j * 57, i * 57))
            if record[i][j] == 'w3':
                screen.blit(w_knight, (j * 57, i * 57))
            if record[i][j] == 'w4':
                screen.blit(w_bishop, (j * 57, i * 57))
            if record[i][j] == 'w5':
                screen.blit(w_queen, (j * 57, i * 57))
            if record[i][j] == 'w6':
                screen.blit(w_king, (j * 57, i * 57))
                is_w_king = True

            # Black
            if record[i][j] == 'b1':
                screen.blit(b_pawn, (j * 57, i * 57))
            if record[i][j] == 'b2':
                screen.blit(b_rook, (j * 57, i * 57))
            if record[i][j] == 'b3':
                screen.blit(b_knight, (j * 57, i * 57))
            if record[i][j] == 'b4':
                screen.blit(b_bishop, (j * 57, i * 57))
            if record[i][j] == 'b5':
                screen.blit(b_queen, (j * 57, i * 57))
            if record[i][j] == 'b6':
                screen.blit(b_king, (j * 57, i * 57))
                is_b_king = True

    # If a king was eaten, print the winner
    if not is_b_king:
        print('White win!')
        running = False
    elif not is_w_king:
        print('Black win!')
        running = False

    pygame.display.update()
