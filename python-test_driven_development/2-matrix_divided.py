def matrix_divided(matrix, div):
    """
    Matrisin bütün elementlərini div-ə bölür və yeni matris qaytarır.
    """
    
    # 1. div-in rəqəm olub-olmadığını yoxlayaq
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    
    # 2. div-in sıfır olub-olmadığını yoxlayaq
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # 3. Matrisin ümumi strukturunu yoxlayaq
    error_msg = "matrix must be a matrix (list of lists) of integers/floats"
    
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(error_msg)

    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(error_msg)
        
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError(error_msg)

    # 4. Sətirlərin ölçüsünün eyni olduğunu yoxlayaq
    row_size = len(matrix[0])
    for row in matrix:
        if len(row) != row_size:
            raise TypeError("Each row of the matrix must have the same size")

    # 5. Bölmə əməliyyatı (yuvarlaqlaşdırma ilə)
    return [[round(x / div, 2) for x in row] for row in matrix]
