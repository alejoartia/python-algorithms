"""Here you can see an example of files handle( w,r,a)"""



def read():
    numbers = []
    #in open you put the route
    with open("./files/files_number.txt", "r", encoding="utf-8") as f:
        for line in f:
            numbers.append(int(line))
    print(numbers)

def write():
    names = ["paqui", "alejandro", "julieth", "daniel", "mia"]
    # with "a" instead "w" you can write intead of overwrite
    with open("./files/names.txt", "w", encoding ="utf-8") as f:
        for name in names:
            f.write(name)
            f.write("\n")

def run():
    #write()
    read()

if __name__=='__main__':
    run()