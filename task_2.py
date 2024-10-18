disket_size_Mbytes = 1.44
symbol_size_bytes = 4
pages_in_book = 100
lines_in_book = 50
simbol_in_book = 25
size_book = simbol_in_book * lines_in_book * pages_in_book * symbol_size_bytes
disket_size_bytes = disket_size_Mbytes * (2**20)
numbers_book = int(disket_size_bytes // size_book)
print("Количество книг, помещающихся на дискету:", numbers_book)
