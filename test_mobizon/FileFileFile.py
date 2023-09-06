test_file = open('/home/aleksey/Desktop/Testsss/krutoydoc.txt', 'a')
test_file.write('Salat.'"\n")
test_file.close()
test_file = open('/home/aleksey/Desktop/Testsss/krutoydoc.txt')
print(test_file.read()) # Прочесть весь файл
#for line in test_file:  # Прочесть файл по строкам
#    print(line)
#for line in test_file:
#    print(line.rstrip("\n") + "!!!") # добавление символа в конец каждой строки









