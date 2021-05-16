def isPlinedrome(inp):
    for i in range(0,len(inp)):
        if inp[i] != inp[len(inp)-i-1]:
            return False
    return True


