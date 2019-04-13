import os

i = len(os.listdir("results/"))-1000

for filename in os.listdir("results/"):
    if filename.startswith("output"):
        os.rename('results/'+str(filename), 'results/'+str(i)+'.mid')
        i += 1
