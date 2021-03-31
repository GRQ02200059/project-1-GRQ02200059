import markdown2 as markdown2
from django.shortcuts import render

from . import util

def search(request):
    q=request.GET.get('q')
    err=""
    if not q:
        err="  ERROR   \n请输入关键词"
        return render(request,"encyclopedia/detail.html",{'html':err})
    result=util.get_entry(q)
    the_result=[].append(result)
    # if result!=None:
    #     return render(request, "encyclopedia/search.html", {
    #         "entry": result
    #     })
    # else :
    the_result=[]
    for entry in util.list_entries():
        if q in entry:
            the_result.append(entry)
    return render(request, "encyclopedia/index.html", {
                "entries": the_result
        })

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })
def create_np(request):
    print("000000000")
    return  render(request,"encyclopedia/create_np.html",{})
def detail(request,entry):
    print('detail'+ entry)
    if entry=='favicon.ico':
        entry="HTML"
    string = "E:\project-1-GRQ02200059\entries\\" + entry + ".md"
    input_file = open(string, mode="r", encoding="gbk")
    text = input_file.read()
    html = markdown2.markdown(text, extras=['fenced-code-blocks'])

    with open("hhh.html", "w+")as f:
        f.write(html)
    return render(request, "encyclopedia/detail.html", {"html": html,"title":entry})
def random(request):
    list=util.list_entries()

    from random import choice
    item=choice(list)
    string = "E:\project-1-GRQ02200059\entries\\" + item + ".md"
    input_file = open(string, mode="r", encoding="gbk")
    text = input_file.read()
    html = markdown2.markdown(text, extras=['fenced-code-blocks'])
    print(item)
    with open("hhh.html", "w+")as f:
        f.write(html)
    return render(request, "encyclopedia/detail.html", {"html": html,"title":item})
def edited(request,entry):
    print('='*30)
    print(entry)
    print("="*30)
    print(edit)
    print("="*30)
    if request.method=='POST':
        html=request.POST.get('edited')
        print(html)

    util.save_entry(entry,html)
    string = "E:\project-1-GRQ02200059\entries\\" + entry + ".md"
    input_file = open(string, mode="r", encoding="gbk")
    text = input_file.read()
    html = markdown2.markdown(text, extras=['fenced-code-blocks'])
    print(html)
    with open("hhh.html", "w+")as f:
        f.write(html)
    return render(request, "encyclopedia/detail.html", {"html": html, "title": entry})
def get_np(request):
    if request.method=='POST':
        entry=request.POST.get('entry')
        context=request.POST.get('context')
        print(entry,context)
        if entry in util.list_entries():
            return render(request, "encyclopedia/detail.html", {"html":"词条已存在，请重新输入","title":entry})
        util.save_entry(entry,context)
    # return render(request,"encyclopedia/create_np.html",{})

    string = "E:\project-1-GRQ02200059\entries\\" + entry + ".md"
    input_file = open(string, mode="r", encoding="gbk")
    text = input_file.read()
    html = markdown2.markdown(text, extras=['fenced-code-blocks'])
    print(entry)
    with open("hhh.html", "w+")as f:
        f.write(html)
    return render(request, "encyclopedia/detail.html", {"html": html,"title":entry})
def edit(request,title):
    print("in edit")
    string = "E:\project-1-GRQ02200059\entries\\" + title + ".md"
    input_file = open(string, mode="r", encoding="gbk")
    text = input_file.read()
    html = markdown2.markdown(text, extras=['fenced-code-blocks'])
    print(title)
    with open("hhh.html", "w+")as f:
        f.write(html)
    return render(request,"encyclopedia/edit.html",{"html": html,"entry":title})
