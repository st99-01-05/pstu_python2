import sys

class DNASequence:
    def __init__(self, sequence):
        self.sequence = sequence
        self.compressed_sequence = self._compress()

    def _compress(self):
        nucleotide_dict = {'A': 0b00, 'T': 0b01, 'C': 0b10, 'G': 0b11}
        compressed_sequence = 0b00
        for nucleotide in self.sequence:
            compressed_sequence <<= 2
            compressed_sequence |= nucleotide_dict[nucleotide]
        return compressed_sequence

    def unpack(self):
        nucleotide_dict = {0b00: 'A', 0b01: 'T', 0b10: 'C', 0b11: 'G'}
        uncompressed_sequence = ''
        compressed_sequence = self.compressed_sequence
        while compressed_sequence > 0:
            nucleotide = compressed_sequence & 0b11
            uncompressed_sequence += nucleotide_dict[nucleotide]
            compressed_sequence >>= 2
        return uncompressed_sequence[::-1]

    def __str__(self):
        return self.unpack()

# Генерация случайной последовательности ДНК из 1000 нуклеотидов
random_sequence = "ACTG" * 250

# Создание экземпляра класса DNASequence
dna = DNASequence(random_sequence)

# Вывод оригинального и сжатого размера последовательности в памяти
print("Оригинальный размер:", sys.getsizeof(random_sequence))
print("Сжатый размер:", sys.getsizeof(dna.compressed_sequence))

# Распаковка сжатой последовательности и вывод
uncompressed_sequence = dna.unpack()
print("Распакованная последовательность:", uncompressed_sequence)
