#--------------- G L O B A L S ---------------#
error = "none"
userfound = 0
passfound = 0

#--------------- U S E R N A M E   C H E C K ---------------#
def checker(user, passw):
    global userfound 
    lineno = 0
    file = open("data\\accounts.sql", "r")
    # loop over lines in a file
    for line in file:
        lineno = lineno + 1
        if user not in line:
            continue
        else:
            userfound = lineno
            file.close()
            return userfound
        break
    else:
        file.close()
        return 0

#--------------- P A S S W O R D   C H E C K ---------------#               
def passchek(passw):
    global passfound 
    lineno = 0
    file = open("data\\accounts.sql", "r")
    # loop over lines in a file
    for line in file:
        lineno = lineno + 1
        if passw not in line:
            continue
        else:
            passfound = lineno
            file.close()
            return passfound
        break
    else:
        file.close()
        return 0

#--------------- F I N A L   C H E C K ---------------#
def finalcheck():
    global passfound, userfound
    passfoundm1 = passfound - 1
    if passfoundm1 == userfound:
        return 1
    else:
        return 0