checklist = []

checklist = list()
checklist.append('Blue')
print(checklist)

checklist.append('Orange')
print(checklist)

##CREATE
def create(item):
    checklist.append(item)

##READ
def read(index):
    item = checklist[index]
    return item

##UPDATE
def update(index, item):
    checklist[index] = item

##DESTROY
def destroy(index):
    checklist.pop(index)

##LIST ALL ITEMS 
def list_all_items():
    index = 0
    for list_item in checklist:
        print("{} {}".format(index, list_item))
        index += 1

##MARK COMPLETED 
def mark_completed(index):
    if 0 <= index < len(checklist):
        checklist[index] = "√" + checklist[index]

##USER INPUT DEFINE
def user_input(prompt):
    user_input = input(prompt)
    return user_input

##SELECTION
def select(function_code):
    if function_code == "A":
        input_item = user_input("Input item:")
        create(input_item)

    elif function_code == "C":
        item_index = int(user_input("Completed item index:"))
        mark_completed(item_index)

    elif function_code == "R":
        item_index = user_input("Index Number?")
        item = read(int(item_index))
        print(item)

    elif function_code == "P":
        list_all_items()

    elif function_code == "Q":
        return False
    
    else:
        print("Unknown Option")
    return True


##TESTING
def test():
    test()
create("purple sox")
create("red cloak")

print(read(0))
print(read(1))

update(0, "purple socks")

destroy(1)
print(read(0))

select("A")
list_all_items()

select("R")
list_all_items()

##LOOP
running = True
while running:
    selection = user_input("Press A to add to list, R to read from list, C to complete an item, P to display, or Q to quit:")
    select(selection)