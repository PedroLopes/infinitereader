import subprocess

#txt2speech = ['espeak',"-ven+f3", "-k5" ,"-s 120", " ".join()] #linux on my pi
txt2speech = 'say' #macOS

#infinite_material = "/home/pi/infinitejests/infinite.txt" #linux on my pi
infinite_material = "infinite.txt" #local

def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in xrange(0, len(l), n):
        yield l[i:i + n]

def read(line):
    subprocess.call([txt2speech, " ".join(line)])

with open(infinite_material) as f:
    content = f.readlines()

for line in content:
    if len(line) < 100:
        read(line)
    else:
        new_line = []
        counter = 1
        for word in line.split(" "):
            new_line.append(word)
            counter+=1
            if counter > 20:
                read(new_line)
                new_line = []
                counter=0
        read(new_line)
