def logics(a, b):
    result = []
    a = set(a)
    b = set(b)
    result.append(a.intersection(b))
    result.append(a.union(b))
    result.append(a.difference(b))
    result.append(b.difference(a))
    return result


def freq(str):
    result = {}
    for i in str:
        if i in result:
            result[i] += 1
        else:
            result[i] = 1
    return result


def compare_dicts(dict1, dict2):
    if dict1.keys() != dict2.keys():
        return False

    for key in dict1:
        val1 = dict1[key]
        val2 = dict2[key]

        if isinstance(val1, dict) and isinstance(val2, dict):
            if not compare_dicts(val1, val2):
                return False
        elif isinstance(val1, list) and isinstance(val2, list):
            if len(val1) != len(val2) or any(not compare_dicts(v1, v2) if isinstance(v1, dict) and isinstance(v2, dict) else v1 != v2 for v1, v2 in zip(val1, val2)):
                return False
        elif isinstance(val1, set) and isinstance(val2, set):
            if val1 != val2:
                return False
        else:
            if val1 != val2:
                return False

    return True


def build_xml_element(tag, content, **attributes):
    attrs = ' '.join(f'{key}="{value}"' for key, value in attributes.items())
    return f'<{tag} {attrs}>{content}</{tag}>'


def validate_dict(rules, d):
    for key, prefix, middle, suffix in rules:
        if key not in d:
            return False
        value = d[key]
        if not value.startswith(prefix):
            return False
        if not value.endswith(suffix):
            return False
        if middle not in value[len(prefix):-len(suffix) or None]:
            return False
    return True


def count_unique_and_duplicates(lst):
    unique_elements = set()
    duplicates = set()

    for item in lst:
        if item in unique_elements:
            duplicates.add(item)
        else:
            unique_elements.add(item)

    num_unique = len(unique_elements)
    num_duplicates = len(duplicates)

    return (num_unique, num_duplicates)


def set_operations(*sets):
    result = {}
    sets = list(sets)

    for i in range(len(sets)):
        for j in range(i + 1, len(sets)):
            a = sets[i]
            b = sets[j]
            result[f"{a} | {b}"] = a | b
            result[f"{a} & {b}"] = a & b
            result[f"{a} - {b}"] = a - b
            result[f"{b} - {a}"] = b - a

    return result


def find_loop(mapping):
    visited = set()
    result = []
    current_key = "start"

    while current_key not in visited:
        visited.add(current_key)
        current_value = mapping[current_key]
        result.append(current_value)
        current_key = current_value

    return result


def count_positional_in_keyword(*args, **kwargs):
    count = 0
    keyword_values = set(kwargs.values())

    for arg in args:
        if arg in keyword_values:
            count += 1

    return count


if __name__ == "__main__":
    print(logics([1, 2, 3, 4, 5], [3, 4, 5, 6, 7]))
    print(freq("ana are mere"))
    print(build_xml_element("a", "Hello there",
          href="http://python.org", _class="my-link", id="someid"))
    print(set_operations({1, 2}, {2, 3}))
    print(find_loop({'start': 'a', 'b': 'a', 'a': '6', '6': 'z',
                     'x': '2', 'z': '2', '2': '2', 'y': 'start'}))
    print(count_positional_in_keyword(1, 2, 3, 4, x=1, y=2, z=3, w=5))
