

def main(inputV):
    out=inputV.replace(':(','🙁')
    out=out.replace(':)','🙂')

    return out

inputV=input("Enter a string")
outputV=main(inputV)
print(outputV)


