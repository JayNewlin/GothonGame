from nose.tools import *
from gothonweb.map import *

def test_room():
	gold = Room("GoldRoom",
				"""This room has gold in it you can grab. There's a
				door to the north.""")
	assert_equal(gold.name, "GoldRoom")
	assert_equal(gold.paths, {})

def test_room_paths():
	center = Room("Center", "Test room in the center.")
	north = Room("North", "Test room in the north.")
	south = Room("South", "Test room in the south.")

	center.add_paths({'north': north, 'south': south})
	assert_equal(center.go('north'), north)
	assert_equal(center.go('south'), south)

def test_map():
	start = Room("Start", "You can go west and down a hole.")
	west = Room("Trees", "There are trees here, you can go east.")
	down = Room("Dungeon", "It's dark down here, you can go up.")

	start.add_paths({'west': west, 'down': down})
	west.add_paths({'east': start})
	down.add_paths({'up': start})

	assert_equal(start.go('west'), west)
	assert_equal(start.go('west').go('east'), start)
	assert_equal(start.go('down').go('up'), start)

# Rewritten after START became a function
def test_gothon_game_start():
  	assert_equal(central_corridor.go('shoot!'), central_corridor_shoot)
  	assert_equal(central_corridor.go('dodge!'), central_corridor_dodge)
  	assert_equal(central_corridor.go('tell a joke'), laser_weapon_armory)

def test_laser_weapon_armory():
 	assert_equal(laser_weapon_armory.go('*'), armory_death)
 	# We can't get the keypad_code from the function, so it prints to the terminal, so that we can test 
 	# the_bridge path successfully on the web.
 	# assert_equal(laser_weapon_armory.go(keypad_code), the_bridge)
	

def test_the_bridge():
	assert_equal(the_bridge.go('throw the bomb'), bridge_throw_bomb)
	assert_equal(the_bridge.go('slowly place the bomb'), escape_pod)

# We can't test the escape_pod() when it's in the START() function
# def test_escape_pod():
# 	assert_equal(escape_pod.go('2'), the_end_winner)
# 	assert_equal(escape_pod.go('*'), the_end_loser)



