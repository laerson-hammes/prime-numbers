def prime_numbers(data: list) -> list[int]:
   numbers = []
   for number in data:
      aux = 0
      for i in range(1, len(data)):
         if number % i == 0:
            aux += 1
      if aux == 2:
         numbers.append(number)
   return numbers


print(prime_numbers(list(range(1, 1000))))