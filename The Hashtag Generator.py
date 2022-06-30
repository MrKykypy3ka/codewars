def generate_hashtag(s):
    if s == '':
        return False
    elif len(s) > 140:
        return False
    else:
        return f'#{"".join(s.title().split())}'
