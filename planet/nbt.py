"""

This file is uniquely licensed under the MIT license because it may be useful in other applications an utilites.

MIT License

Copyright (c) 2022 Alexey Pavlov

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


"""

import nbtlib
import subprocess

def remove_header(filename: str):
    #with open(filename,  "rb") as file:
    #   data = file.read()
    #with open(filename,  "wb") as write_file:
    #    write_file.write(data[8:])
    # This is WIP code! Do not use!
    
    return subprocess.Popen(["/usr/bin/pi-nbt",  "remove-header",  filename])

def add_header(filename: str):
    return subprocess.Popen(["/usr/bin/pi-nbt",  "add-header",  filename])


def load_nbt(filename: str,  header_type = None):
    if  header_type == "level.dat":
        remove_header(filename)
    elif header_type not in ["level.dat",  None]:
        raise Exception("Invalid file! Please use header_type=None to open a file without a header")
    
    return nbtlib.load(filename,  gzipped=False,  byteorder="little")
    
    
