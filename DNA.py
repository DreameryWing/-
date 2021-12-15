from random import *

def nucl_seq(n, m):
	for _ in range(n):
		nucl = []
		for _ in range(m):
			nucl.append(choice(["A", "T", "G", "C"]))
		print(nucl)
		print("A -", round((nucl.count("A")/m)*100, 2), '%')
		print("T -", round((nucl.count("T")/m)*100, 2), '%')
		print("G -", round((nucl.count("G")/m)*100, 2), '%')
		print("C -", round((nucl.count("C")/m)*100, 2), '%')
		print("GC -", round(((nucl.count("C") + nucl.count("G"))/m)*100, 2), '%')


n = int(input("Введите число последовательностей:"))
m = int(input("Введите длину:"))
x = nucl_seq(n, m)