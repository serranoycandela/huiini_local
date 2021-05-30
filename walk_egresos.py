import os

path = "C:/Dropbox (LANCIS)/RENATO"
for root, dirs, files in os.walk(path, topdown=False):
   for name in files:
      print(root)
      print(os.path.join(root, name))
   for name in dirs:
      print(os.path.join(root, name))