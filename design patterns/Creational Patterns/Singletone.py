class Borg:
	#makes class attributes global
	_shared_state = {}

	def __init__(self):
		self.__dict__ = self._shared_state

class Singleton(Borg):
	"""docstring for ClassName"""
	def __init__(self, **kwargs):
		Borg.__init__(self)
		self._shared_state.update(kwargs)

	def __str__(self):
		return str(self._shared_state)

x = Singleton(adminpwd='admin1234')
print(x)

y = Singleton(userpwd = 'user1234')
print(y)