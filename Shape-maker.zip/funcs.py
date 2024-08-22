# By neverfriendme
from turtle import *
import math

def Form_cric():
    if 1 == 1:
        while True:
            forward(3.14)
            right(3.14)
def Form_octa():
    if 1 == 1:
        while True:
            forward(90)
            left(45)
            right(90)
def Form_nona():
    if 1 == 1:
        while True:
            right(90)
            left(50)
            forward(90)
def listfunc_form():
    print(".nona\n.circ\n.octa\n.hexa\n.dode\n.tria\n.squa\nMore updates coming soon!")

def help():
    print("listfunc.[Function] not listfunc.Function\n-v will display the version\nhelp or ?h to get Help")

def Form_hexa():
    area = 3/3 * 10 * 20
    if 1 == 1:
        while True:
            forward(area)
            left(20)
            right(area * 1.6)

def Form_dode():
    area = 1/4 * 10 * 15
    if 1 == 1:
        while True:
            forward(area)
            left(30)
            right(area * 1.6)

def Form_tria():
    area = 1/2 * 600   
    if 1 == 1:
        while True:
            forward(area)
            left(60)
            right(area)

def Form_squa():
    area = 10/20 * 300   
    if 1 == 1:
        while True:
            forward(area * 2)
            left(60)
            right(area)
# --special--
def listfunc_spec():
    print(".special1\nMore updates coming soon!")
    
def Form_spec1():
    side1 = 5/math.pi
    side2 = 100/math.pi
    if 1 == 1:
        while True:
            forward(side2 * 3)
            left(side1 * 4)
            right(side2 * 4)
            forward(side1 * 3)


            
