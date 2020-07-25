
import pyglet
import os

#path = os.path.join(os.path.expanduser('~'), 'hadoop', 'hadoop_working', 'Project', 'Sound','sa.wav')
#print (path)


#music = pyglet.resource.media("/home/hduser/hadoop/hadoop_working/Project/Sound/sa.wav")
sa = pyglet.resource.media('sa.wav')
re = pyglet.resource.media('re.wav')
sa.play()
re.play()




