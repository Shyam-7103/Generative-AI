import pyttsx3
import os
engine = pyttsx3.init()

# print("""Twinkle, twinkle, little star,
# How I wonder what you are!
# Up above the world so high,
# Like a diamond in the sky.

# When the blazing sun is gone,
# When he nothing shines upon,
# Then you show your little light,
# Twinkle, twinkle, all the night.

# Then the trav'ller in the dark,
# Thanks you for your tiny spark,
# He could not see which way to go,
# If you did not twinkle so.

# In the dark blue sky you keep,
# And often thro' my curtains peep,
# For you never shut your eye,
# Till the sun is in the sky.

# 'Tis your bright and tiny spark,
# Lights the trav'ller in the dark:
# Tho' I know not what you are,
# Twinkle, twinkle, little star.""")

# Problem - 2 int cmd prompt

# Problem - 3 external module download


# engine.say("My name is Shyam Patel")
# engine.runAndWait()

# Problem - 4 Using Chatgpt

# specify the directory path
path = input("/")

# check if directory exists
if os.path.exists(path):
    print("Contents of the directory:")
    for item in os.listdir(path):
        print(item)
else:
    print("Directory does not exist")

# Give comments to Problem - 4