def add(item):
	"""Adds an item to the list."""
	todos.append(item)  ##it might be possible to add len=0 items (eg blanks).
	print "Added."

def remove(item):
	"""Removes an item from the list. Accepts an int. """ ## might be useful to also allow removing a full item, eg try that first and if it excepts, try INT. this is handy for big items.
	try: 
		item = int(item)-1
		done.append(todos[item])
		todos.pop(item)
		print "Deleted."
	except Exception:
		print "Fail"
	
def print_todo():
	print "Todo:" ## just prints the to-dos. would be preferable when you have a lot of finished items.
	for i in range(0,(len(todos))):
		print "%s. %s"%(i+1,todos[i])

def print_done():
	print "Finished:" ## just prints finished items.
	for i in range(0,(len(done))):
		print "%s. %s"%(i+1,done[i])
		
def print_all(): 
	"""Prints lists."""
	print_todo() ##prints all the items
	print ""
	print_done()

def write_to_file(filename):
	"""Writes to a user-specified file."""
#	filename = "todo.txt"
#	print "Name the list. Default is %s"%filename
#	filename = raw_input(prompt)
	print "Are you sure you want to write to %s?"%filename
	print "This will overwrite the file."
	go = raw_input("Y/N? ")
	if go.lower() == "y": ##JUST CHECKING!
		target = open(filename, 'w')
		print "Truncating."
		target.truncate()
		target.write("Todo\n")
		for i in range(0,len(todos)):
			target.write(todos[i])
			target.write("\n")
		target.write("Done\n")
		for i in range(0,len(done)):
			target.write(done[i])
			target.write("\n")
		print "Finished."
	else:
		pass

def read_from_file(todo,done):
	"""Reads from a designated file and populates a "todo" and "done" list. It *adds* to these lists, so if there are existing items they won't be removed. Allows one to merge lists."""
	filename = "todo.txt"
	print "Name the list. Default is %s"%filename
	filename = raw_input(prompt)
	try:
		txt = open(filename)
		list = txt.readlines()
		try:
			for i in range(1,list.index('Done\n')):
				todos.append(list[i].rstrip('\n'))
			for i in range(list.index('Done\n')+1,len(list)):
				done.append(list[i].rstrip('\n'))
			print "Items added."
		except ValueError:
			print "List is invalid. Required 'Done' to be in the list."
	except EnvironmentError:
		print "No such file!"
	
	
	
todos = []
done = []
prompt = "> "

run = 1
while run == 1: ## this should be turned into a function or something?
	action = raw_input(prompt)
	action = action.split()
	to_add = ""
	if action[0] == "add" or action[0] == "do": ## maybe adding should be the default? like, "pop 1" or "delete 1" should delete 1, but "go to the dentist" should add "go to the dentist".
		action.pop(0)
		for i in range(0,len(action)):
			to_add = to_add + " " + action[i]  ##this is hideous and there has to be a better way to do this.
		add(to_add.strip())
	if action[0] == "print" or action[0] == "print-all":
		print_all()
	if action[0] == "pop" or action[0] == "remove" or action[0] == "finished" or action[0] == "finish":
		remove((action[1]))
	if action[0] == "write":
		write_to_file(action[1])
	if action[0] == "read":
		read_from_file(todos,done)
	if action[0] == "wipe":
		print "Wiping list."
		print "Saving backup, just in case!"
		write_to_file("backup.txt")
		todos = []
		done = []
	if action[0] == "quit":
		quit = raw_input("Save before quitting? Y/N :")
		if quit.lower() == "y":
			write_to_file(raw_input("Please give filename: "))
		else:
			pass
		run = 0
		
		
	print ""
	
