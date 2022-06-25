#Zenan Shang
#CSC3002F OS1 Assignment
#17 April 2022

import sys
import random

def generate(num):     #generating the reference string with numbers ranging from [0 to 9]
    page = []
    for i in range (num):
        page.append(random.randint(0,9))     #random number generator
    return page

def FIFO(size, page):     #generating the output using the FIFO algorithm
    output = []
    count = 0     #counting the faults
    tempsize = size     #The expected page index of the last frame
    for i in range(len(page)):     #iterating through all the numbers in the reference string
        if (i >= tempsize):     #checking if there are any unused frames, e.g. size = 4 but output only have 3 list values, therefore 1 frame is unused
            if output.count(page[i]) <= 0:     #if the page number is not in the frames, then Delete the last number and insert a new number in the front of the list 
                output.pop()
                output.insert(0, page[i])
                count = count + 1
        else:
            if output.count(page[i]) <= 0:     #Checking if the pages we are working with is in the frames or not. 
                output.insert(0,page[i])      #No: we insert the pages
                count = count + 1
            else:
                tempsize = tempsize + 1     #Yes: adding one to the expected page index of the last frame
    output.insert(0, count)
    return output
               
def LRU(size, page):     #generating the output using the LRU algorithm
    output = []
    tempsize = size     #The expected page index of the last frame
    count = 0     #counting the faults
    for i in range(len(page)):     #iterating through all the numbers in the reference string
        if (i >= tempsize):     #checking if there are any unused frames, e.g. size = 4 but output only have 3 list values, therefore 1 frame is unused
            if output.count(page[i]) <= 0:      #if the page number is not in the frames, then Delete the last number and insert a new number in the front of the list
                output.pop()
                output.insert(0, page[i])
                count = count + 1
            else:     #delete the page in the frame and insert it to the front because the first value in the list is the most recently used value
                output.remove(page[i])
                output.insert(0, page[i])
        else:
            if output.count(page[i]) <= 0:     #Checking if the pages we are working with is in the frames or not. 
                output.insert(0,page[i])     #No: we insert the pages
                count = count + 1
            else:
                tempsize = tempsize + 1     #Yes: adding one to the expected page index of the last frame
    output.insert(0, count)
    return output

def OPT(size, page):     #generating the output using the LRU algorithm
    output = []
    count = 0     #The fault
    tempsize = size     #The expected page index of the last frame
    for i in range(len(page)):     #iterating through all the numbers in the reference string
        if (i >= tempsize):     #checking if there are any unused frames, e.g. size = 4 but output only have 3 list values, therefore 1 frame is unused
            if output.count(page[i]) <= 0:      #checking if the page number is in the frames or not
                templist = []     #a list use to store the distance between the current page index and the next expected frame value in reference string
                for j in range (size):     #Collecting all the page distances
                    if output[j] in page[i+1:]:
                        templist.append(page[i+1:].index(output[j]))
                    else:
                        templist.append(-1)      #if page is not found, then it is -1
                count = count + 1
                if templist.count(-1) <= 0:     #find the largest distance, delete the page and insert the current page in iteration
                    maxnum = max(templist)
                    maxindex = templist.index(maxnum)
                    output.remove(output[maxindex])
                    output.insert(0, page[i])   
                else:     #delete the page that do not have an expected next page
                    minindex = templist.index(-1)
                    output.remove(output[minindex])
                    output.insert(0, page[i])
        else:
            if output.count(page[i]) <= 0:     #Checking if the pages we are working with is in the frames or not. 
                output.insert(0,page[i])     #No: we insert the pages
                count = count + 1
            else:
                tempsize = tempsize + 1     #Yes: adding one to the expected page index of the last frame
    output.insert(0, count)
    return output

def main():
    #...TODO...
    number_of_pages = int(sys.argv[1])
    number_of_frames = int(sys.argv[2])
    page = generate(number_of_pages)
    print("These are the randomly generated reference string")
    print(*page)
    output = FIFO(number_of_frames, page)
    print ('FIFO', output[0], "page faults.", "The pages in the frame are", output[1::], end=".\n")
    output = LRU(number_of_frames, page)
    print ('LRU', output[0], "page faults.", "The pages in the frame are", output[1::], end=".\n")
    output = OPT(number_of_frames, page)
    print ('OPT', output[0], "page faults.", "The pages in the frame are", output[1::], end=".\n")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print ( "Usage: python paging.py [number of pages] [number of frames]")
    else:
        main()
        
