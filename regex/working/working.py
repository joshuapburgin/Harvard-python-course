import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(input_time):
    try:
        pattern = r'(?P<start_hour>\d{1,2})(?::(?P<start_minute>\d{2}))?\s+(?P<start_ampm>AM|PM)\s*to\s*(?P<end_hour>\d{1,2})(?::(?P<end_minute>\d{2}))?\s+(?P<end_ampm>AM|PM)'

        match = re.search(pattern, input_time)
        if match:
            # Extracting each component from the match object
            start_hour = int(match.group('start_hour'))
            start_minute = int(match.group('start_minute')) if match.group('start_minute') else 0
            start_ampm = match.group('start_ampm')

            end_hour = int(match.group('end_hour'))
            end_minute = int(match.group('end_minute')) if match.group('end_minute') else 0
            end_ampm = match.group('end_ampm')

            #a dictionary with all the parsed components
            time_dictionary ={
                "start_hour": start_hour,
                "start_minute": start_minute,
                "start_ampm": start_ampm,
                "end_hour": end_hour,
                "end_minute": end_minute,
                "end_ampm": end_ampm

            }
        else:
            raise ValueError


        if start_hour>12 or end_hour>12 or start_minute>59 or end_minute>59:
            raise ValueError

    except ValueError:
        sys.exit("ValueError")
    else:
        output=""
        if start_ampm=="AM":
            AM_time = [f"{0 if start_hour==12 else start_hour:02}",f"{start_minute:02}"]
            PM_time = [f"{end_hour+12 if end_hour!=12 else end_hour}",f"{end_minute:02}"]
            return f"{AM_time[0]}:{AM_time[1]} to {PM_time[0]}:{PM_time[1]}"
        else:
            AM_time = [f"{0 if end_hour==12 else end_hour:02}",f"{end_minute:02}"]
            PM_time = [f"{start_hour+12 if start_hour!=12 else start_hour}",f"{start_minute:02}"]
            return f"{PM_time[0]}:{PM_time[1]} to {AM_time[0]}:{AM_time[1]}"


if __name__ == "__main__":
    main()
