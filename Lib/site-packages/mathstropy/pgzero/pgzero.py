#remove objec from list with status not 0
def listCleanup(objects):
    newList = []
    for i in range(len(objects)):
        if objects[i].status == 0:
            newList.append(objects[i])
    return newList
