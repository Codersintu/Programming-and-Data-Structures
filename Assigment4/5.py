def group_anagrams(words):
    hashmap = {}

    for word in words:

        key = "".join(sorted(word))

    
        if key not in hashmap:
            hashmap[key] = []

        
        hashmap[key].append(word)

    
    return list(hashmap.values())
