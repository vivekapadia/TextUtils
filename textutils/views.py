# I have created this file -Vivek
from django.http import HttpResponse
from django.shortcuts import render

def index(req):

    params = {'name':'Vivek','age': 19}
    # arguments value access by index.html
    return render(req,'index.html',params)

    # nav = '''
    #         <div>
    #             <h1> HomePage </h1>
    #             <div>
    #                 <a href="/about">About</a>
    #                 <a href="/removepunc">Removepunc</a>
    #                 <a href="/capitalizefirst">Capfirst</a>
    #                 <a href="/spaceremover">SpaceRomover</a>
    #                 <a href="/newlineremove">Newlineremover</a>
    #                     <a href="/charcount">CharCount</a>
    #
    #             </div>
    #         </div>
    #       '''
    # return HttpResponse(nav)

def analyze(req):
    # Get the text
    # djtext = req.GET.get('usertext','default')
    djtext = req.POST.get('usertext','default')
    print(djtext)
    params = {}
    purpose = ''

    # check checkbox values
    # removepunc = req.GET.get('removepunc','off')
    removepunc = req.POST.get('removepunc','off')
    print(removepunc)

    # fullcaps = req.GET.get('fullcaps', 'off')
    fullcaps = req.POST.get('fullcaps', 'off')
    print(fullcaps)

    # newlineremover = req.GET.get('newlineremover', 'off')
    newlineremover = req.POST.get('newlineremover', 'off')
    print(newlineremover)

    # extraspaceremover = req.GET.get('extraspaceremover', 'off')
    extraspaceremover = req.POST.get('extraspaceremover', 'off')
    print(extraspaceremover)

    # Analyze - Check which checkbox is ON
    if removepunc == 'on':
        allpunc = '''!()-[]{};:'"\, <>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in allpunc:
                analyzed = analyzed + char

        # params = {'purpose': 'Remove Punctuations','analyzed_text': analyzed}

        if purpose == '':
            purpose += 'Remove Punctuations'
        else:
            purpose += ' | Remove Punctuations'

        djtext = analyzed
        # return render(req,'analyze.html',params)

    # elif fullcaps == 'on':
    if fullcaps == 'on':
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()

        # params = {'purpose':'CHANGE TO UPPERCASE','analyzed_text': analyzed}

        if purpose == '':
            purpose += 'CHANGE TO UPPERCASE'
        else:
            purpose += ' | CHANGE TO UPPERCASE'

        djtext = analyzed
        # return render(req,'analyze.html',params)

    # elif newlineremover == 'on':
    if newlineremover == 'on':
        analyzed = ""
        for char in djtext:
            if char != '\n' and char != '\r':
                analyzed = analyzed + char

        # params = {'purpose':'Removed NewLines','analyzed_text': analyzed}

        if purpose == '':
            purpose += 'Removed NewLines'
        else:
            purpose += ' | Removed NewLines'

        djtext = analyzed
        # return render(req,'analyze.html',params)

    # elif extraspaceremover == 'on':
    if extraspaceremover == 'on':
        analyzed = ""
        # for char in djtext:
        #     if char != "  ":
        for index , char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index+1] == " "):
                analyzed = analyzed + char

        # params = {'purpose':'Removed Spaces','analyzed_text': analyzed}

        if purpose == '':
            purpose += 'Removed Spaces'
        else:
            purpose += ' | Removed Spaces'

        djtext = analyzed
        # return render(req,'analyze.html',params)


    if(removepunc != 'on' and fullcaps != 'on' and newlineremover != 'on' and extraspaceremover != 'on'):
        return HttpResponse("Please Select any operation and try again </br> <b>Original Input :</b> </br> <pre>{}</pre>".format(djtext))

    params = {'purpose': purpose, 'analyzed_text': djtext}
    return render(req,'analyze.html',params)

    # return HttpResponse('RemovePunctuations')


# -------------------------------------------------------------------------------------------------------------------
# # TASK
# def about(req):
#     # nav = '''
#     #         <div>
#     #             <h1> AboutPage </h1>
#     #             <div>
#     #                 <a href="/">Home</a>
#     #                 <a href="/removepunc">Removepunc</a>
#     #                 <a href="/capitalizefirst">Capfirst</a>
#     #                 <a href="/spaceremover">SpaceRomover</a>
#     #                 <a href="/newlineremove">Newlineremover</a>
#     #                 <a href="/charcount">CharCount</a>
#     #
#     #             </div>
#     #         </div>
#     #       '''
#     # return HttpResponse(nav)
#
#     return HttpResponse('<a href="/">Home</a>')
#
# def removepunc(req):
#     # Get the text
#     djtext = req.GET.get('usertext','default')
#     print(djtext)
#
#     # Analyse the text
#     return HttpResponse('<a href="/">Home</a>')
#
#     # nav = '''
#     #             <div>
#     #                 <h1> removepunc </h1>
#     #                 <div>
#     #                     <a href="/">Home</a>
#     #                     <a href="/about">About</a>
#     #                     <a href="/capitalizefirst">Capfirst</a>
#     #                     <a href="/spaceremover">SpaceRomover</a>
#     #                     <a href="/newlineremove">Newlineremover</a>
#     #                     <a href="/charcount">CharCount</a>
#     #
#     #                 </div>
#     #             </div>
#     #           '''
#     # return HttpResponse(nav)
#
# def capitalizefirst(req):
#     # nav = '''
#     #             <div>
#     #                 <h1> CapitalizeFirst </h1>
#     #                 <div>
#     #                     <a href="/">Home</a>
#     #                     <a href="/about">About</a>
#     #                     <a href="/removepunc">Removepunc</a>
#     #                     <a href="/spaceremover">SpaceRomover</a>
#     #                     <a href="/newlineremove">Newlineremover</a>
#     #                     <a href="/charcount">CharCount</a>
#     #
#     #                 </div>
#     #             </div>
#     #           '''
#     # return HttpResponse(nav)
#
#     return HttpResponse('<a href="/">Home</a>')
#
#
# def newlineremove(req):
#     # nav = '''
#     #             <div>
#     #                 <h1> NewLineRemove </h1>
#     #                 <div>
#     #                     <a href="/about">About</a>
#     #                     <a href="/removepunc">Removepunc</a>
#     #                     <a href="/capitalizefirst">Capfirst</a>
#     #                     <a href="/spaceremover">SpaceRemover</a>
#     #                     <a href="/charcount">CharCount</a>
#     #                 </div>
#     #             </div>
#     #           '''
#     # return HttpResponse(nav)
#
#     return HttpResponse('<a href="/">Home</a>')
#
# def charcount(req):
#     # nav = '''
#     #             <div>
#     #                 <h1> CharCount </h1>
#     #                 <div>
#     #                     <a href="/about">About</a>
#     #                     <a href="/removepunc">Removepunc</a>
#     #                     <a href="/capitalizefirst">Capfirst</a>
#     #                     <a href="/spaceremover">SpaceRomover</a>
#     #                     <a href="/newlineremove">Newlineremover</a>
#     #                     <a href="/charcount">CharCount</a>
#     #
#     #                 </div>
#     #             </div>
#     #           '''
#     # return HttpResponse(nav)
#
#     return HttpResponse('<a href="/">Home</a>')
#
# def spaceremover(req):
#     # nav = '''
#     #             <div>
#     #                 <h1> spaceremover </h1>
#     #                 <div>
#     #                     <a href="/">Home</a>
#     #                     <a href="/about">About</a>
#     #                     <a href="/removepunc">Removepunc</a>
#     #                     <a href="/capitalizefirst">Capfirst</a>
#     #                     <a href="/newlineremove">Newlineremover</a>
#     #
#     #                 </div>
#     #             </div>
#     #           '''
#     # return HttpResponse(nav)
#
#     return HttpResponse('<a href="/">Home</a>')
#
# # Content from a file
# def task1(req):
#     fp = open("Display.txt", "r")
#     content = fp.read()
#     fp.close()
#     return HttpResponse(content)
#
# # Navigator
# def task2(req):
#     nav = '''
#             <h2>Navigator Bar</h2>
#             <a href = "https://www.youtube.com/playlist?list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9">Django with harry bhai</a>
#             <a href = "https://www.instagram.com/vivekapadia/">Instagram Vivekji</a>
#             <a href = "https://www.facebook.com/vivekapadia/">Facebook Vivekji</a>
#             '''
#     return HttpResponse(nav)

























































