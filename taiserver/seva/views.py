from django.shortcuts import render
from django.http import HttpResponse
from subprocess import check_output

# Create your views here.

def index(request):
   # translation = "Recording recieved."
   translation = check_output(["deepspeech", "--model", "models/output_graph.pbmm", "--alphabet", "models/alphabet.txt",
                   "--lm", "models/lm.binary", "--trie", "models/trie", "--audio", "test1.wav"])

   return HttpResponse(translation)
