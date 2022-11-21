def check():
    try:
        a = input('Введите числа через пробел: ')
        global array
        array = [int(x) for x in a.split()]
        error = None
        for i in array:
            if i % 1 == 0:
                continue
            else:
                error = True
    except ValueError:
        print("Не корректные данные. Программа завершена!")
    while error != True:
        try:
            global element
            element = int(input("Введите целое число: "))
            if element % 1 == 0:
                array.append(element)
                break
        except ValueError:
            print("Не корректные данные. Программа завершена!")
def sorting():
    for i in range(1, len(array)):
        x = array[i]
        idx = i
        while idx > 0 and array[idx - 1] > x:
            array[idx] = array[idx - 1]
            idx -= 1
        array[idx] = x
    return array
check()
print("Список до сортировки: ", array)
print("Список после сортировки: ", sorting())

def binary_search(array, element, left, right):
    if left > right:
        return False

    middle = (right + left) // 2
    if array[middle] == element:
        return middle
    elif element < array[middle]:
        return binary_search(array, element, left, middle - 1)
    else:
        return binary_search(array, element, middle + 1, right)

print("Индекс введенного числа в списке: ", binary_search(array, element, 0, len(array) - 1))