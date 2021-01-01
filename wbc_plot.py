import csv
from PIL import Image, ImageDraw

reader = csv.reader(open('periods.csv'))

lo = 10000000
hi = -10000000
for row in reader:
    begin = int(row[0])
    end = int(row[1])
    lo = min(lo, begin, end)
    hi = max(hi, begin, end)

hi = hi - lo
begins = []
ends = []

reader = csv.reader(open('periods.csv'))
for row in reader:
    begin = int(row[0]) - lo
    begins.append(begin)
    end = int(row[1]) - lo
    ends.append(end)

img = Image.new('RGB', (hi, 1), color = 'white')
draw = ImageDraw.Draw(img)

for i in range(len(begins)):
    draw.line([(begins[i], 0), (ends[i], 0)], 'black', 1)
img = img.resize((hi, int(hi/2)), Image.NONE)
img.save('wbc.png')
