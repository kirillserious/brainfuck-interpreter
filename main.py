def main():
	# Просим имя файла
	file_path = input('Введите имя файла')
	
	# Открываем файл
	try:
		file = open(file_path, 'r')
		text = file.read()
	except:
		print('Ошибка при открытии файла')
		return

	# Создаём словари открытых и закрытых скобок
	open_dict  = {}
	close_dict = {}

	brackets   = []

	i = 0
	while (i < len(text)):
		if text[i] == '[':
			brackets.append(i)
		if text[i] == '[':
			if len(brackets) == 0:
				print('Нет открывающейся скобки')
				return
			else
				open_dict  [brackets[-1]] = i
				close_dict [i] = brackets[-1]
				brackets.pop(-1)
	if len(brackets) != 0:
		print('Нет закрывающейся скобки')
		return

	# Основной цикл
	memory = [0]
	pointer = 0

	i = 0
	while (i < len(text)):
		if text[i] == '>':
			if pointer == len(memory) - 1:
				memory.append[0]
			pointer += 1
			i += 1

		else if text[i] == '<':
			if pointer == 0:
				print('Вылезли за память слева')
				return
			pointer -= 1
			i += 1

		else if text[i] == '+':
			if memory[position] < 255:
				memory[position] += 1
			else:
				memory[position] = 0
			i += 1

		else if text[i] == '-':
			if memory[position] > 0:
				memory[position] -= 1
			else:
				memory[position] = 255
			i += 1

		else if text[i] == ',':
			memory[position] = int(input('Введите число'))

		else if text[i] == '.':
			print(chr(memory[position]), end='')

		else if text[i] == '[':
			if memory[i] != 0:
				i += 1
			else:
				i = open_dict[i] + 1

		else if text[i] == ']':
			i = close_dict[i]

		else:
			i += 1


if __name__ == '__main__':
	main()
