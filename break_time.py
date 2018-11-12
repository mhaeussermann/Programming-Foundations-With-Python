import webbrowser as wb
import time as t

iteration = 0
end_total = 3

print("Started on " + t.ctime())

while iteration < end_total:
    t.sleep(10)
    wb.open('https://www.google.de')
    iteration += 1
