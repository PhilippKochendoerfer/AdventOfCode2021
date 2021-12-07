paths = ["day7_test.txt","day7.txt"]



def main():
    for path in paths:
        with open(path) as file:
            lines = [l.rstrip() for l in file.readlines()]


        inp = processInput(lines)

        dist = [0]*max(inp)

        for i in range(0,len(dist)):
            #print(i)
            dist[i] = sum([abs(i-j)*(abs(i-j)+1)/2 for j in inp])


        inp.sort()

        if(len(inp)%2==0):
            y = (inp[int(len(inp)/2)]+inp[int(len(inp)/2)+1])/2
        else:
            y = inp[len(inp)/2]

        x = sum(inp)/len(inp)

        print(dist)
        print(min(dist))
        #print(x)
        #print(y)
        #print(f"Part1: {path}: {sum(simulateEfficient(processInput(lines), 80))}")



def processInput(lines):
    return [int(x) for x in lines[0].split(",")]

if __name__ == "__main__":
    main()
