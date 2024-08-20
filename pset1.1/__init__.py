import check50


@check50.check()
def exists():
    """pset1.1.py exists"""
    check50.exists("pset1.1.py")


@check50.check(exists)
def azcbobobegghakl():
    """correctly identifies the number of vowels in azcbobobegghakl"""
    file = open("pset1.1.py")
    text = file.read()
    file.close()
    pset = open("pset.py", "w")
    pset.write("s = 'azcbobobegghakl'\n")
    pset.write(text)
    pset.close()
    check50.run("python3 pset.py").stdout("Number of vowels: 5").exit(0)


def bzcbcbcbdgghfkl():
    """correctly identifies the number of vowels in bzcbcbcbdgghfkl"""
    file = open("pset1.1.py")
    text = file.read()
    file.close()
    pset = open("pset.py", "w")
    pset.write("s = 'bzcbcbcbdgghfkl'\n")
    pset.write(text)
    pset.close()
    check50.run("python3 pset.py").stdout("Number of vowels: 0").exit(0)
