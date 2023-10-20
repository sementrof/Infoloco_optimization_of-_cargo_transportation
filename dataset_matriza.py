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