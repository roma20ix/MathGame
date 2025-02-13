"""
"""


from random import randint


def create_level(level: str) -> list[tuple[int, str]]:
	"""
	# level - строка, содержащая арифметическое выражение
	"""
	return [(i, randint(1, 3)) for i in level]
