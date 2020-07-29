def onlyVocals(str):
    vocals = "aeiou"
    for c in str:
        if not(c in vocals):
            return False
    return True

def onlyCons(str):
    vocals = "aeiou"
    for c in str:
        if c in vocals:
            return False
    return True

def stringsExclusivos(strA, strB):
    casoUno = onlyVocals(strA) and onlyCons(strB)
    casoDos = onlyVocals(strB) and onlyCons(strA)
    return casoUno or casoDos

print(stringsExclusivos("aeu", "trtrtrtrtr"))