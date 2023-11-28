import unittest
import object_game

class TestObjectGame(unittest.TestCase) :

  # Testing rooms
  room_1 = object_game.Room(111, [
      object_game.GameObject(
          "Sweater",
          "It's a blue sweater that had the number 12 stitched on it.",
          "Someone has unstitched the second number, leaving only the 1.",
          "The sweater smells of laundry detergent."),
        object_game.GameObject(
          "Chair", 
          "It's a wooden chair with only 3 legs.",
          "Someone had deliberately snapped off one of the legs.",
          "It smells like old wood.")
    ])

  room_2 = object_game.Room(123, [])

  # Checks to see if the correct code returns true
  def test_check_code_true(self) :

    self.assertEqual(self.room_1.check_code(111), True)

  # Checks to see if a wrong code returns false
  def test_check_code_false(self) :

    self.assertEqual(self.room_1.check_code(123), False)

  # Checks to make sure the list is returned correctly
  def test_get_game_object_names(self) :

    all_names = self.room_1.get_game_object_names()
    names_list_length = len(self.room_1.get_game_object_names())

    self.assertEqual(names_list_length, 2)
    self.assertEqual(all_names, ["Sweater", "Chair"])

  # Checks to make sure the list is returned correctly
  def test_get_game_object_names_none(self) :

    no_names = self.room_2.get_game_object_names()
    no_names_length = len(no_names)

    self.assertEqual(no_names_length, 0)
    self.assertEqual(no_names, [])