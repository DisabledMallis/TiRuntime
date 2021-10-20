#!/usr/bin/python
#coding=utf-8
import wget;
import os;

def downloadFile(url, filename=None):
	wget.download(url, filename);


print("TiRuntime setup");
option = input("1. Setup & Run TiRuntime\n2. Clean TiRuntime\n:");
if option == 1:
	downloadFile("https://www.antlr.org/download/antlr-4.9.2-complete.jar", "antlr4.jar");
	os.system("./run.sh");
if option == 2:
	filelist = [ 
		f for f in os.listdir("src/antlr/") if not f.endswith(".g4") 
	]
	for f in filelist:
		os.remove(os.path.join("src/antlr/", f));
		print("Deleted "+f);