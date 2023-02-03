def permutation(array1, array2):
    if len(array1) != len(array2):
        return False

    array1_copy = array1[:]
    array2_copy = array2[:]
    array1_copy.sort()
    array2_copy.sort()

    if array1_copy == array2_copy:
        return True
    return False
