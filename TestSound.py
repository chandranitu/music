import pyglet
import os

# path = os.path.join(os.path.expanduser('~'), 'hadoop', 'hadoop_working', 'Project', 'Sound','sa.wav')
# print (path)


# music = pyglet.resource.media("/home/hduser/hadoop/hadoop_working/Project/Sound/sa.wav")
sa = pyglet.resource.media('sound/SA.mp3')
re = pyglet.resource.media('sound/RE.mp3')
sa.play()
re.play()

if __name__ == "__main__":
    print("")
