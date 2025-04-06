def get_num_words(string):
    return len(string.split())

def get_num_chars(string):
    chars = {}
    for char in string.lower():
        if char in chars:
            chars[char] += 1
        else: 
            chars[char] = 1
    return chars

def sort_counts(d):
    items = []
    for k, v in d.items():
        items.append({"char": k, "count": v})
    items.sort(key=lambda x: x["count"], reverse=True)

    return items

