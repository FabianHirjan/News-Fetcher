def combine_lists(*args):
    # Determină lungimea maximă a listelor
    max_length = max(len(lst) for lst in args)
    result = []

    # Iterează prin fiecare poziție
    for i in range(max_length):
        # Crează un tuplu pentru fiecare poziție
        current_tuple = []
        for lst in args:
            # Adaugă elementul dacă există, altfel adaugă None
            if i < len(lst):
                current_tuple.append(lst[i])
            else:
                # Poți schimba None cu altceva dacă dorești
                current_tuple.append(None)
        result.append(tuple(current_tuple))

    return result


# Exemplu de utilizare
lists = [[1, 2, 3], [5, 6, 7], ["a", "b", "c"]]
result = combine_lists(*lists)
print(result)
