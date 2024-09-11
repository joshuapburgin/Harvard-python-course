file= input("File name:    ").lower().replace(" ","")
output=""
parts=file.split(".")
if len(parts)>2:
    file="."+parts[2]
else:
    file=file



if "gif" in file or "jpeg" in file or "png" in file:
    output="image/"+file[file.find(".")+1:]
elif "jpg" in file:
    output="image/jpeg"
elif "txt" in file:
    output="text/"+file[0:file.find(".")]
elif "pdf" in file or "zip" in file:
    output="application/"+file[file.find(".")+1:]
elif "." not in file:
    output="application/octet-stream"
else:
    output="application/octet-stream"

print(output)
