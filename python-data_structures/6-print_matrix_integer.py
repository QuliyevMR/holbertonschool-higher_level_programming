#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for i in range(len(row)):
            # Əgər element sətirdə sonuncu deyilsə, boşluqla çap et
            if i != len(row) - 1:
                print("{:d}".format(row[i]), end=" ")
            else:
                # Sonuncu elementdən sonra boşluq qoyma
                print("{:d}".format(row[i]), end="")
        # Hər sətirdən sonra yeni sətirə keç
        print()
