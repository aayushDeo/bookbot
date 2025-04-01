def word_count(str):
    words = str.split()
    return len(words)

def char_stat(str):
    str = str.lower()
    char_cnt = dict()
    for c in str:
        if c in char_cnt:
            char_cnt[c] += 1
        else:
            char_cnt[c] = 1
    return char_cnt