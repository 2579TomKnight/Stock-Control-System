#Python Refresher

#Revolutionary Grocery store express lane checker
#V1.000000000298134
#Made by Tom Knight

#Input Function
def items_On_List():
    print ("Welcome to express lane")
    print ("Please add the name of your scrumptious food item to the list")
    itemList = []
    item = (input("Add 1 item to the list (-1 to quit)"))
    itemList.append(item)
    while item != '-1':
        item = (input("Add 1 item to the list (-1 to quit)"))
        itemList.append(item)   
    itemList.pop(-1)
    return itemList

#Processing Function
def process(itemList):
    length = len(itemList)
    return length

#Output Function
def output(length):
    if length > 12:
        print("You shall not pass!")
        print("Please transfer to the standard lane, thanks!")
    else:
        print("Your fine mate")

#Main Function
def main():
    f1 = items_On_List()
    f2 = process(f1)
    f3 = output(f2)

main()    
#End source code


    
