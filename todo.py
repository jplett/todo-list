def add(item):
    """Adds an item to the list."""
    if len(item) > 0:
        todos.append(item)
        print "Added."
    else:
        print "Item too short."

def item_convert(item):
    """Converts item into the index # for deleting / finishing"""
    item = int(item)-1
    return item
        
def finish(item):
	"""Removes an item from the list. Accepts an int. """ ## might be useful to also allow removing a full item, eg try that first and if it excepts, try INT. this is handy for big items.
	try: 
   		item = item_convert(item)
		done.append(todos[item])
		del_item(item+1)
		return "Item finished! Congratulations!"
	except Exception:
		return "Fail."

def modify(item):
    """Modifies an item specified from user."""
    try:
        item = int(item)-1
        print "Changing item: " + todos[item]
        todos.pop(item)
        todos.insert(item,(raw_input("Change item to: ")))
        print "Item changed."
    except Exception:
        print "Fail."

def del_item(item):
    try:
        item = item_convert(item)
        todos.pop(item)
        return "Item deleted."
    except Exception:
        return "Fail."
               
def print_todo():
    """Prints to-do items only (eg not finished items)"""
    print "Todo:" ## just prints the to-dos. would be preferable when you have a lot of finished items.
    for i in range(0,(len(todos))):
        print "%s. %s"%(i+1,todos[i])

def print_done():
    """Prints finished items only (eg not todos)"""
    print "Finished:" ## just prints finished items.
    for i in range(0,(len(done))):
        print "%s. %s"%(i+1,done[i])
		
def print_all(): 
    """Prints lists."""
    print_todo() ##prints all the items
    print "\n"
    print_done()
    
    
def write_to_file(filename):
    """Writes to a user-specified file."""
    target = open(filename, 'w')
    target.truncate()
    target.write("Todo\n")
    for i in range(0,len(todos)):
        target.write(todos[i])
        target.write("\n")
    target.write("Done\n")
    for i in range(0,len(done)):
        target.write(done[i])
        target.write("\n")
    return "Finished."


def read_from_file(filename):
	"""Reads from a designated file and populates a "todo" and "done" list. It *adds* to these lists, so if there are existing items they won't be removed. Allows one to merge lists."""
##  filename = "todo.txt"
	#print "Reading from %s."%filename
	try:
		txt = open(filename)
		list = txt.readlines()
		try:
			for i in range(1,list.index('Done\n')):
				todos.append(list[i].rstrip('\n'))
			for i in range(list.index('Done\n')+1,len(list)):
				done.append(list[i].rstrip('\n'))
			return "Items added."
		except ValueError:
			return "List is invalid, possibly corrupt."
	except EnvironmentError:
		return "No such file!"

def dict_creator(list,action):
    """Creates dictionaries for this"""
    for i in range(0,len(list)):
        cmnd[list[i]] = action
	
def ret_dict_list(command):
    """Returns dict list"""
    x = []
##  print "To %s, try:"%command  ##this is probably stupid. descriptions should maybe be a separate list or something.
    for i in range(0,len(cmnd)):
        if cmnd.values()[i] == command:
            x.append(cmnd.keys()[i])
    print ', '.join(x)

def help():
    """Prints possible commands."""
    print "To 'add' items, try typing:"
    ret_dict_list('add')
    print "\nTo mark an item as 'finished,' try typing:"
    ret_dict_list('finish')
    print "\nTo change a todo item, try:"
    ret_dict_list('modify')
    print "\nTo delete a todo item, try:"
    ret_dict_list('delete')
    print "\nTo print your list, try:"
    ret_dict_list('print')
    print "\nTo save your list, try:"
    ret_dict_list('save')
    print "\nTo load and merge a list, try:"
    ret_dict_list('load')
    print "\nTo wipe your current list, try:"
    ret_dict_list('new')
    print "\nTo quit, try:"
    ret_dict_list('quit')
    a = "\nFinally, please note this program will save your list"
    b = "automatically after every action. The file is autosave.txt."
    print a, b
                     
def quitter():
    filename = "autosave.txt"
    print "Quitting will truncate %s."%filename
    quit = raw_input("Save before quitting? Y/N: ")
    if quit[0].lower() == "y":
        write_to_file(raw_input("Please give filename: "))
    else:
        pass
    target = open(filename, 'w')
    target.truncate()
    print "Quitting. Goodbye!"
    return 0

def new_list():
    print "Wiping lists."
    x = raw_input("Save first Y/N? ")
    if x.lower()=="y":
        filename = raw_input("Enter a filename (.txt preferred): ")
        print write_to_file(filename)
    else:
        pass
    

def todolist():
    print ""
    q = raw_input(prompt).split()
    print ""
    try:
        action = cmnd[q[0]]
        if action == "add":
            add(raw_input("Item to add: "))
        if action == "finish":
            print finish(raw_input("Item to finish: "))
        if action == "delete":
            print del_item(raw_input("Item to delete: "))
        if action == "save":
            filename = raw_input("Enter a filename (.txt preferred): ")   ##save and write raw_inputs should be a function.
            print "This will overwrite the file if it already exists."
            print "Write to %s? (Y/N)"%filename 
            go = raw_input(prompt)
            if go[0].lower() == "y": ##JUST CHECKING!
                print write_to_file(filename)
            else:
                pass
        if action == "load":
            print "Loading will combine your existing list with the specified list."
            print read_from_file(raw_input("Enter a filename (.txt preferred): "))
        if action == "print":
            print_all()
        if action == "modify":
            modify(raw_input("Item to modify: "))
        if action == "new": ##this doesnt work.
            new_list()
            todos = ['']
            done = ['']
        if action == "quit":
            return quitter() ##quitter returns 0; this returns 0 to the loop, which ends it.   
    except KeyError:
        help()
    write_to_file("autosave.txt")
    return 1 ## this returns a 1 to the loop, which means the variable is still true and the loop doesn't end.

def dict_initialize(cmnd):
    """Intitializes dictionary."""
    dict_creator(add_cmd,'add')
    dict_creator(print_cmd,'print')
    dict_creator(fin_cmd,'finish')
    dict_creator(mod_cmd,'modify')
    dict_creator(del_cmd,'delete')
    dict_creator(save_cmd,'save')
    dict_creator(load_cmd,'load')
    dict_creator(quit_cmd,'quit')
    dict_creator(new_cmd,'new')
    
todos = []
done = []
prompt = "> "
run = 1

cmnd = {}
add_cmd = ['add', 'do', 'create', 'task']
print_cmd = ['print', 'print-all']
fin_cmd = ['finish', 'done', 'complete']
del_cmd = ['delete', 'remove']
save_cmd = ['save', 'write']
load_cmd = ['load', 'read']
mod_cmd = ['modify', 'change', 'edit', 'fix', 'correct']
quit_cmd = ['quit', 'exit', 'close']    
new_cmd = ['new list', 'new', 'wipe']
dict_initialize(cmnd)

print "Type 'help' for a list of commands."
filename = "todo.txt"
print "Loading from %s"%filename
print read_from_file(filename)
while run == 1: 
    run = todolist()



