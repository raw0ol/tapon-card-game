# Tapon Card Game

Tapon is a single player card game that can be played using the command line interface. This game was created using Python 3.8.1, and was one of my first projects when I was learning about object-oriented programming.

## How to Play

To start the game, navigate to the directory where the game files are located and run the following command:

```python tapon.py```

The game will begin, and you will be prompted to enter table size (between 2-4), coins per player (between 2-6), and username. Follow the on-screen instructions to play the game.

* Dealer distrubutes a card to each player including to self. Upon each users turn, the CPU or user chooses whether to keep or change a card with the next player in line.

* The goal is to avoid having the lowest card in each round.

* There are a few restrictions though, users are unable to change if the player next in line holds a king(12). If you hold a King(12), you are automatically saved and can play the next round.

* Play smart, such as staying and holding a card if the previous user in line exchanged a higher card than what you had/gave back.

* Dearler goes last in each round but can draw a card from deck if they choose to do so.

* Player or players with the lowest card in each round lose a coin.

* Last player standing collects all coins and wins!


## Requirements

In order to run this game, you will need to have Python 3.8.1 or higher installed on your system. You can check which version of Python you have installed by running the following command:

```python --version```


If you need to install Python, you can download it from the [official Python website](https://www.python.org/).

## Issues and Contributions

If you encounter any bugs or issues while playing the game, please open an issue in the GitHub repository. Contributions to the code are also welcome - please fork the repository and submit a pull request if you have any improvements to suggest.

## License

This game is released under the MIT license. See the [LICENSE](LICENSE) file for more details.
