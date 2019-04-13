import os

midi_files = os.listdir("results")

for x in range(len(midi_files)):
    midi_file = str(midi_files[x])
    name = str(midi_file.replace('.mid', '.mp3'))
    command = 'timidity.exe results/'+midi_file+' -Ow -o mp3/'+name
    print(command)
    result = os.system(command)


#midi_file = '0.mid'
#name = str(midi_file.replace('.mid', '.mp3'))
#command = 'timidity.exe results/'+midi_file+' -Ow -o mp3/'+name
#print(command)
#result = os.system(command)
