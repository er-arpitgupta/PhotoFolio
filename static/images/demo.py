import os

files = os.listdir('photos/')
count = 1
for file in files:
    if file.startswith('data'):
        os.rename(file, f'editing{count}.jpg')
        count+=1