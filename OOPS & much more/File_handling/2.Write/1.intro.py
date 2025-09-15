"""
Write Mode:
-We are writing that why we are using w
-It does'nt makes any sense if we are using write mode to open a file
-Bydefault if the file doesn't exist write mode creates it self.
-If we hover on write it wants a str
-What write mode does actually is if there is something written in the file it removes everything
 and does overwrite
-To add multiple lines use \n
"""

with open("hello1.txt", "w") as f:
    f.write("HeLLo Mootttooo\n")
    f.write("HeLLo Samsung\n")
    f.write("HeLLo iphone")
