def main():
    time=input("Please enter the time for a meal    ")
    time_Int=convert(time)
    match time_Int:
        case n if 7<=n<=8:
            print("breakfast time")
        case n if 12<=n<=13:
            print("lunch time")
        case n if 18<=n<=19:
            print("dinner time")



def convert(time):
    time_Int= float(time[0:time.find(":")])+ float(time[time.find(":")+1:])/60
    return time_Int


if __name__ == "__main__":
    main()
