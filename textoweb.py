x = input("Enter your text you would like to convert>")
with open("convert.html", "a") as f:
    y = print("<p>" + x + "</p>", file=f)
    f.close()
