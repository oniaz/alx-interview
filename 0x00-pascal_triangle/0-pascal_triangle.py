def pascal_triangle(n):
    arr = []
    for row in range(n):
        arr.append([1])
        for col in range(row + 1):
            if (row > 0):
                if (col == 0):
                    pass
                elif (col < (row / 2) or col == (row / 2)):
                    arr[row].append(arr[row - 1][col - 1] + arr[row - 1][col])
                else:
                    arr[row].append(arr[row][row-col])
    return arr
