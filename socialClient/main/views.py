from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
 
def main(req): 
    return render(req,'main.html')
 


def myPage(req):
    return render(req,'myPage.html')