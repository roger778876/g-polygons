from display import *
from draw import *
from parser import *
from matrix import *
import math

screen = new_screen()
color = [ 0, 255, 0 ]
gold = [255, 215, 0]
edges = []
transform = new_matrix()

# print_matrix( make_bezier() )
# print
# print_matrix( make_hermite() )
# print

parse_file( 'script', edges, transform, screen, color )
# parse_file( 'script2', edges, transform, screen, gold )
# parse_file( 'script3', edges, transform, screen, gold )