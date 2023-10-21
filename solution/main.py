def read_csv_and_calc_mean_solution(lines):

    first_line = lines[0].replace("\n", "").split(",")
    csv_list = [[0] * len(first_line)] * len(lines)
    csv_list[0] = first_line

    for i in range(1, len(lines)):
        csv_list[i] = lines[i].replace("\n", "").split(",")


    return csv_list

list1 = open("hackathon_sirius_data.csv", "r")
list2 = list1.readlines()
list1.close()

csv_list = read_csv_and_calc_mean_solution(list2)
list3 = [0] * len(csv_list)
list_start = [0] * len(csv_list)
list_end = [0] * len(csv_list)


for i in range(1, len(csv_list)):
    list3[i-1] = int(csv_list[i][2])
    list_start[i-1] = int(csv_list[i][2])
    list_end[i - 1] = int(csv_list[i][3])


def find_all_indices(arr, value):
    indices = []
    for i in range(len(arr)):
        if arr[i] == value:
            indices.append(i)
    return indices


# Пример использования:
indices = find_all_indices(list_start, 63)

import pandas as pd

# Загрузка набора данных
data = pd.read_csv('hackathon_sirius_data.csv')
common_point = set(data['start']).intersection(set(data['end']))

matrixIn = []
matrixEX = []
for i in range(0, len(common_point)):
    list_index = find_all_indices(list_start, i)
    newarr = []
    for j in range(len(list_index)):
        newarr.append(list_end[list_index[j]])
    matrixEX.append(newarr)

#matrixEX = [row for row in matrixEX if row]
print(matrixEX)




#ВЫХОДНЫЕ
arrTn = []

for k in range(0, len(matrixEX)):
    sum = 0
    for j in range(0, len(matrixEX[k])):

        for i in range(1, len(csv_list)):
            try:
                if matrixEX[k][j] == int(csv_list[i][3]) and k == int(csv_list[i][2]):
                    sum += int(csv_list[i][6])
                    #arrTn.append(int(csv_list[i][6]))
            except:
                a = 0
    arrTn.append(sum)

arrTn = [item for item in arrTn if item != 0]

#ВХОДНЫЕ
arrTNIN = []

for k in range(0, len(matrixEX)):
    sum = 0
    for j in range(0, len(matrixEX[k])):

        for i in range(1, len(csv_list)):
            try:
                if matrixEX[k][j] == int(csv_list[i][2]) and k == int(csv_list[i][3]):
                    sum += int(csv_list[i][6])
            except:
                a = 0
    arrTNIN.append(sum)

arrTNIN = [item for item in arrTNIN if item != 0]

arrRAZNOST = []
for i in range(0, len(arrTNIN)):
    arrRAZNOST.append(arrTn[i] - arrTNIN[i])

arrRAZNOST = list(map(abs, arrRAZNOST))
arrRAZNOST = [item for item in arrRAZNOST if item != 0]

maxLeng = 0.0
arrLeng = []
arrZAMENA = []
arrMAXTN = []
for k in range(0, len(matrixEX)):
    arrmedimLeng = []
    for j in range(0, len(matrixEX[1])):

        for i in range(1, len(csv_list)):
            try:
                if matrixEX[k][j] == int(csv_list[i][3]) and k == int(csv_list[i][2]):
                    m = float(csv_list[i][4])
                    arrmedimLeng.append(m)
                    if m > maxLeng:
                        maxLeng = m
            except:
                a = 0
    arrLeng.append(maxLeng)
    try:
        maxValue = max(arrmedimLeng)
        maxIndex = arrmedimLeng.index(maxValue)
    except:
        maxIndex = 0
    try:
        for i in range(1, len(csv_list)):
            if matrixEX[k][maxIndex] == int(csv_list[i][2]) and k == int(csv_list[i][3]):
                arrZAMENA.append(int(csv_list[i][6]))
                arrMAXTN.append(float(csv_list[i][7]))
    except:
        pass
    maxLeng = 0

arrLeng = [item for item in arrLeng if item != 0]


arrPochtiItog = []
for i in range(len(arrZAMENA)):
    arrPochtiItog.append(arrZAMENA[i] - arrRAZNOST[i])
arrPochtiItog = list(map(abs, arrPochtiItog))

arrItog = []
for i in range(len(arrMAXTN)):
    arrItog.append(int(arrPochtiItog[i] / arrMAXTN[i]))

print(arrTn)
print(arrTNIN)
print(arrRAZNOST)
print(arrLeng)
print(arrZAMENA)
print(arrMAXTN)
print(arrPochtiItog)
print(arrItog)
print(len(arrItog), len(arrPochtiItog), len(arrMAXTN), len(arrZAMENA), len(arrLeng), len(arrRAZNOST),
      len(arrTNIN), len(arrTn), len(matrixEX))

total = 0
for element in arrItog:
    total += element
print(total)

import tkinter as tk
from tkinter import filedialog
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import networkx as nx
import matplotlib.pyplot as plt



def plot_graph():
    # Создаем пустой граф
    G = nx.Graph()

    # Массивы начальных и конечных станций
    start_stations = [54, 22, 32, 48, 28, 34, 62, 10, 83, 2, 50, 77, 58, 63, 73, 72, 46, 46, 77, 82, 81, 31, 79, 63, 56,
                      31, 4, 55, 4, 53, 5, 57, 47, 20, 35, 15, 59, 38, 49, 52, 13, 29, 18, 65, 85, 85, 25, 21, 78, 6,
                      78, 71, 40, 31, 70, 70, 89, 60, 88, 88, 89, 39, 39, 19, 42, 23, 12, 41, 43, 84, 37, 51, 44, 44,
                      80, 68, 61, 1, 69, 64, 87, 14, 15, 14, 27, 11, 51, 74, 30, 22, 28, 22, 54, 27, 32, 34, 34, 62, 10,
                      10, 10, 10, 50, 83, 73, 72, 73, 71, 46, 70, 79, 40, 0, 31, 75, 56, 4, 5, 55, 44, 75, 53, 47, 47,
                      20, 20, 59, 59, 38, 38, 49, 13, 13, 29, 16, 85, 25, 40, 78, 60, 78, 88, 40, 26, 71, 60, 42, 23,
                      42, 3, 89, 76, 39, 24, 41, 41, 80, 63, 43, 43, 84, 12, 86, 68, 1, 1, 17, 57, 57, 64, 64, 45, 45,
                      11, 19, 19,
                      ]
    end_stations = [22, 28, 22, 54, 27, 32, 34, 34, 62, 10, 10, 10, 10, 50, 83, 73, 72, 73, 71, 46, 70, 79, 40, 0, 31,
                    75, 56, 4, 5, 55, 44, 75, 53, 47, 47, 20, 20, 59, 59, 38, 38, 49, 13, 13, 29, 16, 85, 25, 40, 78,
                    60, 78, 88, 40, 26, 71, 60, 42, 23, 42, 3, 89, 76, 39, 24, 41, 41, 80, 63, 43, 43, 84, 12, 86, 68,
                    1, 1, 17, 57, 57, 64, 64, 14, 15, 45, 45, 11, 19, 19, 54, 22, 32, 48, 28, 34, 62, 10, 83, 2, 50, 77,
                    58, 63, 73, 72, 46, 46, 77, 82, 81, 31, 79, 63, 56, 31, 4, 55, 4, 53, 5, 57, 47, 20, 35, 15, 59, 38,
                    49, 52, 13, 29, 18, 65, 85, 85, 25, 21, 78, 6, 78, 71, 40, 31, 70, 70, 89, 60, 88, 88, 89, 39, 39,
                    19, 42, 23, 12, 41, 43, 84, 37, 51, 44, 44, 80, 68, 61, 1, 69, 64, 87, 14, 27, 11, 51, 74, 30,
                    ]

    # Массив с длинами в километрах
    distances = [45, 9, 10, 14, 36, 23, 26, 447, 113, 55, 47, 266, 374, 4, 17, 37, 24, 52, 20, 56, 48, 24, 17, 13, 26,
                 48, 48, 5, 35, 101, 96, 70, 29, 27, 11, 14, 14, 11, 43, 33, 63, 50, 169, 2, 0, 63, 156, 27, 148, 8, 38,
                 37, 55, 7, 10, 57, 22, 46, 72, 30, 14, 176, 23, 33, 62, 4, 87, 3, 52, 4, 0, 87, 140, 92, 5, 47]
    # Здесь 10 км соответствует пути между 54 и 22, а 15 км - между 37 и 18

    # Добавляем ребра между начальными и конечными станциями и устанавливаем атрибут "distance"
    for start, end, distance in zip(start_stations, end_stations, distances):
        G.add_edge(start, end, distance=distance)

    # Рисуем граф, используя длины в километрах
    edge_labels = {(start, end): str(distance) for (start, end, distance) in
                   zip(start_stations, end_stations, distances)}
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_size=500, node_color='lightblue', font_size=10, font_color='black')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')
    plt.title("Граф станций с длинами маршрутов")
    plt.show()


def open_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        # Делайте что-то с выбранным файлом, например, выводите его путь
        print("Выбранный файл:", file_path)

# Создаем главное окно
window = tk.Tk()
window.title("Графики и файлы")
window.geometry("800x600+350+50")

from tkinter import PhotoImage
# bg_image = PhotoImage(file="parovozik.jpg")

# canvas = tk.Canvas(window, width=bg_image.width(), height=bg_image.height())
# canvas.pack()

# canvas.create_image(150, 150, image=bg_image, anchor=tk.NW)


# Кнопка для вывода графика
plot_button = tk.Button(window, text="Построить график", command=plot_graph)
plot_button.pack()

# Кнопка для открытия файлов
open_file_button = tk.Button(window, text="Открыть файлы", command=open_file)
open_file_button.pack()

# Запуск главного цикла Tkinter
window.mainloop()