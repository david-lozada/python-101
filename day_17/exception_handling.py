try:
	names = ['Finland', 'Sweden', 'Norway','Denmark','Iceland', 'Estonia','Russia']
	*rest, es, ru = names
	print(rest, es, ru)
except Exception as e:
	raise e