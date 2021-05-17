import os

disk_number = 3
towers = {}
t = []
solved = False


def setup(): # Set up variables
    global towers
    global t
    global space
    towers = {1: [], 2: [], 3: []}
    t = ['  |  ', '-----']

    space = ' ' * 3

    for i in range(disk_number):
        t.insert(0, t[0])
    for i in towers.keys():
        towers[i] = [0 for a in range(disk_number + 1)]
    towers[1] = [a for a in range(disk_number + 1)] # Set all the disks to Tower 1


def display_towers(): # Display towers and didks in console
    rows = []
    for r in range(disk_number + 2):
        rows.append('')
        for tower in towers.keys():
            disk = t[r]
            if r < disk_number + 1 and towers[tower][r] != 0:
                disk = disk.replace('|', str(towers[tower][r]))
            rows[r] += disk + space

    for i in range(len(rows)):
        print(rows[i])
    print('  1  ' + space + '  2  ' + space + '  3  ' + space)
    print()


def check(display): # Check if last tower (Tower 3) has all the disks in correct order
    global solved
    global towers
    correct = [a for a in range(disk_number + 1)]
    if towers[3] == correct:
        solved = True
    if display:
        print('Solved: ', solved)
        print()


def move(frm, to): # Move top-most disk from 'Tower frm' to 'Tower to'
    global towers
    if frm == to: return
    try:
        idx1 = 0
        while towers[frm][idx1] == 0: # Get the index of the element at the top of the 'frm' tower
            idx1 += 1

        idx2 = 0
        while towers[to][idx2] == 0: # Get the index above the top-most element in 'to' tower
            idx2 += 1
            if idx2 == len(towers[to]):
                break
        idx2 -= 1

        disk_to_move = towers[frm][idx1]
        if idx2 + 1 == len(towers[to]) or towers[to][idx2 + 1] > disk_to_move: # Check if the move is valid
            towers[frm][idx1] = 0
            towers[to][idx2] = disk_to_move
    except Exception as E:
        print(E)
        return


setup()
display_towers()
check(False)
move(1, 3)
move(1, 2)
move(3, 2)
move(1, 3)
move(2, 1)
move(2, 3)
move(1, 3)
display_towers()
