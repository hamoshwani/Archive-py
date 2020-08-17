import os
def save(body,name):
    saving=[]
    if name.startswith("http://") or name.startswith("https://"):
        name1 = name.split("://")
        filename=f"{name1[1]}"
    else:
     filename=f"output/{name}.txt"
    if os.path.exists(f"output/{name}.txt"):
        os.remove(f"output/{name}.txt")
    for i in body:
        saving.append(i+"\n")
    file=open(filename,"a")
    file.writelines(saving)
    file.close()
    print(f"\nFile saved to:\"output/{name}.txt\"")