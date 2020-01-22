# mandalorian-terminal
Terminal based game, heavily inspired by Jetpack Joyride

# Requirements
Contained in requirements.txt\
To install enter the command:
```bash
pip install -r requirements.txt
```

# Running the game

In the terminal, run
```bash
python game.py
```

# Controls

1. **w** : Move player up
2. **a** : Move player left
3. **d** : Move player right
4. **b** : Shoot bullet
5. **spacebar** : Activate shield
6. **l** : Activate dragon
7. **q** : Quit the game

# OOPS concepts used
1. Inheritance:\
There is a class GameObject from which all the other classes except Board inherit.

2. Polymorphism:\
The class Mandalorian and other classes like Bullet have different methods like hit_right_edge which are called from the same place but do different things.\
In Mandalorian we stop the object from moving but in Bullet we deactivate the bullet.

3. Encapsulation:\
We have wrapped data and methods in one unit.

4. Abstraction:\
    We are calling methods to manipulate the hidden data of objects such as move_up in Mandalorian.


