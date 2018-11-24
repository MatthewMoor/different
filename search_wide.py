from collections import deque

def search(name):
	graph = {}
	search_queue = deque()
	search_queue += graph['name']
	searched = []
	while search_queue:
		person = search_queue.popleft()
		if not person in searched:
			if person is 'trader':
				print(person + 'is a mango seller!')
				return True
			else:
				search_queue += graph[person]
				searched.append(person)
	return False
	
print(search('you'))
