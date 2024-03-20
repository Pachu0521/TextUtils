from django.shortcuts import render, HttpResponse

def index(request):
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")

def contact(request):
    return render(request,"contact.html")


def analyze(request):
    djtext = request.POST.get("text", "defualt")
    removepunc = request.POST.get("removepunc", "off")
    uppercase = request.POST.get("uppercase", "off")
    extraspaceremover = request.POST.get("extraspaceremover", "off")
    newliner = request.POST.get("newliner", "off")
    charcount = request.POST.get("charcount", "off")

    if removepunc == "on":
        punctuations = "!@#$%^&*(\")_+=-\|]}[{';:/?.>,<"
        analyzes = ""
        for char in djtext:
            if removepunc:
                if char not in punctuations:
                        analyzes = analyzes + char
            elif uppercase:
                analyzes = analyzes + char.upper()

        param = {"purpose": "Remove Punctuations", "analyzes": analyzes}
        djtext = analyzes
        # return render(request, "analyze.html", param)

    if uppercase == "on":
        analyzes = ""
        for char in djtext:
            analyzes = analyzes + char.upper()
        param = {"purpose": "Upper Case", "analyzes": analyzes}
        djtext = analyzes
        # return render(request, "analyze.html", param)

    if extraspaceremover == "on":
        analyzes = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index+1] == " "):
                analyzes = analyzes + char
        param = {"purpose": "Extra Space Remover", "analyzes": analyzes}
        djtext = analyzes
        # return render(request, "analyze.html", param)

    if newliner == "on":
        analyzes = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzes = analyzes + char
        param = {"purpose": "New Line Remover", "analyzes": analyzes}
        djtext = analyzes
        # return render(request, "analyze.html", param)

    if (charcount == 'on'):
        analyzes = ""
        count = 0
        for char in djtext:
            print(char)
            if char != " ":
                analyzes = analyzes + char
                count += 1
        param = {"purpose": "Character Counter", "analyzes": analyzes, "count": count}
        djtext = analyzes
        # return render(request, 'analyze.html', param)

    # else:
    #     return HttpResponse("Error")
    return render(request, 'analyze.html', param)




