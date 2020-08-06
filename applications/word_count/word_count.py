
cache = {}

def word_count(s):
    # Your code here
    #
    # def lower_split(s):
    #     a = []
    #     b = s.lower().split()
    #     a.append(b)
    #
    #     return a
    s = s.lower().split()


    for i in s:

        i = i.replace('.', '')
        i = i.replace(',', '')
        i = i.replace('"', '')
        i = i.replace(';', '')
        i = i.replace("\'", '')



        if i not in cache:
            cache[i] = 0
        cache[i] += 1
    return cache


    # for i in s:
    #
    #     if s not in cache:
    #         cache[s] = 0
    #     return cache


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))
