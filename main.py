def main():
	# Просим имя файла
	file_path = input('Введите имя файла: ')
	
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

	for i in range(len(text)):
		if text[i] == '[':
			brackets.append(i)
		elif text[i] == ']':
			if len(brackets) == 0:
				print('Нет открывающейся скобки')
				return
			else:
				open_dict  [brackets[-1]] = i
				close_dict [i] = brackets[-1]
				brackets.pop()

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
				memory.append(0)
			pointer += 1
			i += 1

		elif text[i] == '<':
			if pointer == 0:
				print('Вылезли за память слева')
				return
			pointer -= 1
			i += 1

		elif text[i] == '+':
			if memory[pointer] < 255:
				memory[pointer] += 1
			else:
				memory[pointer] = 0
			i += 1

		elif text[i] == '-':
			if memory[pointer] > 0:
				memory[pointer] -= 1
			else:
				memory[pointer] = 255
			i += 1

		elif text[i] == ',':
			memory[pointer] = int(input('Введите число'))
			i += 1

		elif text[i] == '.':
			print(chr(memory[pointer]), end='')
			i += 1

		elif text[i] == '[':
			if memory[pointer] != 0:
				i += 1
			else:
				i = open_dict[i] + 1

		elif text[i] == ']':
			i = close_dict[i]

		else:
			i += 1


if __name__ == '__main__':
	main()
