import numpy as np

def generate_array():
            #Генерує випадковий масив цілих чисел.
    return np.random.randint(5, 20, 10)
def analyze_list(arr):
            #Аналізує масив: знаходить частоту елементів.
    unique_elements, counts = np.unique(arr, return_counts=True)
    return unique_elements, counts

def print_result(unique_elements, counts):
            #Виводить результати аналізу.
    for element, count in zip(unique_elements, counts):
        print(f"Число {element} повторюється {count} разів")
    print("Масив без дублікатів:", unique_elements)

def main():
    arr = generate_array()  # Формуємо вхідні дані
    unique_elements, counts = analyze_list(arr)  # Обробляємо дані
    print("Згенерований масив:", arr)
    print_result(unique_elements, counts)  # Виводимо результат

if __name__ == "__main__":
    main()

