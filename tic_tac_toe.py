{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [],
   "source": [
    "def display_board(board):\n",
    "    print(f' {board[6]} | {board[7]} | {board[8]} \\n'\n",
    "           '-----------\\n'\n",
    "          f' {board[3]} | {board[4]} | {board[5]} \\n'\n",
    "           '-----------\\n'\n",
    "          f' {board[0]} | {board[1]} | {board[2]} ')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "def get_input(board, player):\n",
    "    user_input = ''\n",
    "    while not user_input:\n",
    "        try:\n",
    "            user_input = int(input('Enter a number from 1-9: '))\n",
    "            if not user_input in range(1, 10):\n",
    "                user_input = ''\n",
    "                raise\n",
    "            if board[user_input - 1] != ' ':\n",
    "                user_input = ''\n",
    "                raise\n",
    "            return (player, user_input)\n",
    "        except:\n",
    "            print('Try again: Invalid input.')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "def update_board(board, player):\n",
    "    if player[0] == 'p1':\n",
    "        board[player[1] - 1] = 'O'\n",
    "    else:\n",
    "        board[player[1] - 1] = 'X'\n",
    "    \n",
    "    return board"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [],
   "source": [
    "def check_condition(board, winner):\n",
    "    p1_victory = ['O', 'O', 'O']\n",
    "    p2_victory = ['X', 'X', 'X']\n",
    "    if board[0:3] == p1_victory or \\\n",
    "       board[3:6] == p1_victory or \\\n",
    "       board[6:] == p1_victory or \\\n",
    "       board[::3] == p1_victory or \\\n",
    "       board[1::3] == p1_victory or \\\n",
    "       board[2::3] == p1_victory or \\\n",
    "       board[0::4] == p1_victory or \\\n",
    "       board[2::2] == p1_victory:\n",
    "        winner = 'p1'\n",
    "    elif board[0:3] == p2_victory or \\\n",
    "       board[3:6] == p2_victory or \\\n",
    "       board[6:] == p2_victory or \\\n",
    "       board[::3] == p2_victory or \\\n",
    "       board[1::3] == p2_victory or \\\n",
    "       board[2::3] == p2_victory or \\\n",
    "       board[0::4] == p2_victory or \\\n",
    "       board[2::2] == p2_victory:\n",
    "        winner = 'p2'\n",
    "    else:\n",
    "        winner = ''\n",
    "    \n",
    "    return winner\n",
    "        "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "cannot assign to conditional expression (<ipython-input-18-fde75bc447d1>, line 17)",
     "output_type": "error",
     "traceback": [
      "\u001b[0;36m  File \u001b[0;32m\"<ipython-input-18-fde75bc447d1>\"\u001b[0;36m, line \u001b[0;32m17\u001b[0m\n\u001b[0;31m    player_tracker = 1 if player_tracker == 0 else player_tracker = 0\u001b[0m\n\u001b[0m                     ^\u001b[0m\n\u001b[0;31mSyntaxError\u001b[0m\u001b[0;31m:\u001b[0m cannot assign to conditional expression\n"
     ]
    }
   ],
   "source": [
    "def setup():\n",
    "    winner = ''\n",
    "    players = ('p1', 'p2')\n",
    "    players_string = {\n",
    "        'p1': 'Player 1',\n",
    "        'p2': 'Player 2'\n",
    "    }\n",
    "    player_tracker = 0\n",
    "    board = [' '] * 9\n",
    "    while not winner:\n",
    "        display_board(board)\n",
    "        p1ayer = get_input(board, players[0])\n",
    "        board = update_board(board, p1ayer)\n",
    "        winner = check_condition(board, winner)\n",
    "        if not winner:\n",
    "            print(f'The winner is {player_string[winner]}!')\n",
    "        player_tracker = 1 if player_tracker == 0 else player_tracker = 0\n",
    "        \n",
    "    # Ask to replay"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "not 0"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "False"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "not 1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
