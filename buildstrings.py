import time

amount = 1_000_000

print("Compare time needed to build a string using concatenation and\nusing a list (append en join).")
print(f"Number of iterations: {amount}.\n")


start_time = time.time()
final_string = ''
for i in range(amount):
    final_string += 'spam '
#print(final_string)
print()
end_time = time.time()
duration = str(round(end_time - start_time, 3))
print(f"Time needed using concatenation: {duration} seconds\n")

start_time = time.time()
final_string = []
for i in range(amount):
    final_string.append('spam ')
final_string = ''.join(final_string)
#print(final_string)
print()
end_time = time.time()
duration = str(round(end_time - start_time, 3))
print(f"Time needed using a list (append and join): {duration} seconds\n")

