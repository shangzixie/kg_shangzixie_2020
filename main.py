import  sys

def answer(s1, s2):
    if len(s1) > len(s2):
        return False

    s1Tos2 = {}
    for i in range(len(s1)):
        if s1[i] not in s1Tos2:
            s1Tos2[s1[i]] = s2[i]
        if s1Tos2[s1[i]] != s2[i]:
            return False

    return True

if __name__ == '__main__':

    print(answer(sys.argv[1], sys.argv[2]))