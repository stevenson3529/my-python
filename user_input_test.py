'''
Testing for the 'user_input' module
'''
import user_input
height = user_input.ask("What is your height?","n")
print("your height is",height)
name = user_input.ask("What is your name?","s")
print("Hello",name)
likeBeef = user_input.ask("Do you like beef?","b")
print("Likes beef =",likeBeef)
