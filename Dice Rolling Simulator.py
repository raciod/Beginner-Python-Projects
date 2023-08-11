import random

def get_dice_face(number):
    dice_faces = [
        '''
        -------
        |     |
        |  •  |
        |     |
        -------
        ''',
        '''
        -------
        | •   |
        |     |
        |   • |
        -------
        ''',
        '''
        -------
        | •   |
        |  •  |
        |   • |
        -------
        ''',
        '''
        -------
        | • • |
        |     |
        | • • |
        -------
        ''',
        '''
        -------
        | • • |
        |  •  |
        | • • |
        -------
        ''',
        '''
        -------
        | • • |
        | • • |
        | • • |
        -------
        '''
    ]
    
    return dice_faces[number - 1]

number = random.randint(1, 6)
dice_face = get_dice_face(number)

print(f"Rolling the dice... You rolled a {number}!")
print(dice_face)
