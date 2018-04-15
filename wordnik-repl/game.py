import random
import pdb

def pick_ten(game_dictionary):
    """will return 10"""

    print(type(game_dictionary))
    # FIXME: cleaner method for dictionary
    temp_dict = {}
    for w in game_dictionary:
        temp_dict[w] = game_dictionary[w]
    # pdb.set_trace()
    play_dict = {}
    for w in random.sample(list(temp_dict), 10):
        play_dict[w] = temp_dict[w]
    return play_dict

def other_defs(play_dict, game_dictionary):
    """return all other definitions"""
    bad_defs = []
    for w in game_dictionary:
        if w in play_dict:
            continue
        bad_defs.append(game_dictionary[w])
    return bad_defs

class Game(object):
    """this class runs the game"""
    
    def __init__(self, game_dictionary):
        """set up game"""
        self.words = pick_ten(game_dictionary)
        self.distract = other_defs(self.words, game_dictionary)
        self.score = 0.0

    def play(self):
        """Actually play the game."""
        for i in range(2):
            # this is the round
            for w in self.words:
                # this is the play within the round
                all_defs = random.sample(self.distract, 3)
                correct = self.words[w]
                all_defs.append(correct)
                random.shuffle(all_defs)
                print('the word is: {}'.format(w))
                print('\n\nthe definitions are:')
                for i in range(len(all_defs)):
                    print('\n     {} -- {}'.format(i, all_defs[i]))
                answer = input('Guess please: ').strip().lower()
                if all_defs[int(answer)] == correct:
                    print('Correct!\n')
                    print('{} -- {}\n\n\n'.format(w, correct))
                    self.score += 0.5
                else:
                    print('Incorrect :(\n')
                    print('the correct definition for {} is: {}\n\n\n'.format(w, correct))
        print('Final score: {} out of 10'.format(self.score))

# def session_words(master_dictionary):
#  """this function selects the 10 words for each session"""
#  master_dictionary = self.master_dict
#  session_words = {}
#  # example of how to add to dict...
#  # session_words['veneration'] = 'condition or status of one who is venerated'

#  """then prints those 10 words and their definitions"""
#   for word in session_words:
#     print(word, ':',  session_words[word])

#def play_game(self):
#  """plays both rounds of the game"""
#  for word in word_list:
#    def give_question(self):
#      """prints question and four answers for player"""
#
#
#    def select_answer(self);
#      """allows the player to select answer, determins if correct"""
#
#
#    def question_response(self):
#      """prints question and answer, identify users choice"""


#    def assign_points(self):
#      """assigns new point value to each word"""
#

#    def second_chance(self):
#      """re-shows the questions answered wrong"""
