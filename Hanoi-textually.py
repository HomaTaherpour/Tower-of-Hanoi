disks = int(input("PLEASE ENTER THE NUMBERS OF DISKS..."))
start_rod = 1
end_rod = 3
holder_rod = 2
counter = 0
def move(disks, start_rod, end_rod, holder_rod ) :
    global counter
    if disks == 0 :
        return
    elif disks >= 1:
        #take disks from start rod to holder rod and use end rod if you need
        #calling the function inside the same function
        #the first point that proves it's a recursive function
        move(disks-1, start_rod, holder_rod, end_rod)
        print("MOVE A DISK FROM", start_rod, "TO", end_rod)
        #in this point we need to print the start rod and holder rod or end one
        move(disks - 1, holder_rod, end_rod, start_rod)
        #the second point that proves it's a recursive function
        counter += 1
    else:
        print("IT'S NOT A VALID NUMBER!")
def main ():
    move(disks, start_rod, end_rod, holder_rod)
    print("NUMBERS OF MOVE =", counter)
    print("ALL DISKS ARE MOVED!")
main()