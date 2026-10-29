#!/usr/bin/env python3
"""Generate original limited-palette pixel-art PNG assets for Cantinho da Mio.
Uses only Python's standard library; each pixel is written to a raster buffer.
"""
from pathlib import Path
import struct, zlib

OUT = Path("assets")
OUT.mkdir(exist_ok=True)
PAL = {
 "ink":(7,10,20,255),"outline":(16,20,36,255),"wall":(25,37,65,255),
 "wall2":(34,48,79,255),"wall3":(43,54,87,255),"floor":(39,42,63,255),
 "floor2":(49,53,77,255),"floor3":(59,61,86,255),"wood":(83,69,91,255),
 "wood2":(111,91,118,255),"woodlight":(153,126,153,255),"silver":(185,207,231,255),
 "blue":(98,151,201,255),"blue2":(55,95,151,255),"purple":(111,91,155,255),
 "lavender":(163,143,198,255),"cream":(224,220,209,255),"paper":(239,230,210,255),
 "red":(151,78,93,255),"green":(83,131,125,255),"gold":(196,166,102,255),
 "skin":(225,190,170,255),"hair":(29,26,39,255),"white":(245,246,250,255)
}
class Img:
 def __init__(self,w,h,fill="ink"):
  self.w,self.h=w,h; self.p=bytearray(PAL[fill]*(w*h))
 def px(self,x,y,c):
  if 0<=x<self.w and 0<=y<self.h:
   i=(y*self.w+x)*4; self.p[i:i+4]=bytes(PAL[c] if isinstance(c,str) else c)
 def rect(self,x,y,w,h,c):
  for yy in range(max(0,y),min(self.h,y+h)):
   for xx in range(max(0,x),min(self.w,x+w)): self.px(xx,yy,c)
 def line(self,x1,y1,x2,y2,c):
  dx=abs(x2-x1); sx=1 if x1<x2 else -1; dy=-abs(y2-y1); sy=1 if y1<y2 else -1; err=dx+dy
  while True:
   self.px(x1,y1,c)
   if x1==x2 and y1==y2: break
   e=2*err
   if e>=dy: err+=dy; x1+=sx
   if e<=dx: err+=dx; y1+=sy
 def box(self,x,y,w,h,c,edge="outline"):
  self.rect(x,y,w,h,edge); self.rect(x+1,y+1,w-2,h-2,c)
 def save(self,name):
  raw=b"".join(b"\x00"+bytes(self.p[y*self.w*4:(y+1)*self.w*4]) for y in range(self.h))
  def chunk(t,d): return struct.pack(">I",len(d))+t+d+struct.pack(">I",zlib.crc32(t+d)&0xffffffff)
  png=b"\x89PNG\r\n\x1a\n"+chunk(b"IHDR",struct.pack(">IIBBBBB",self.w,self.h,8,6,0,0,0))+chunk(b"IDAT",zlib.compress(raw,9))+chunk(b"IEND",b"")
  (OUT/name).write_bytes(png)

# Complete 320x240 room background: all visual geometry is raster art, not CSS.
r=Img(320,240,"ink")
r.rect(0,0,320,240,"wall")
# patterned upper wall with little moon-stone blocks
for y in range(4,72,16):
 for x in range(4,320,16):
  r.box(x,y,15,15,"wall2")
  r.line(x+3,y+4,x+6,y+2,"wall3"); r.px(x+11,y+10,"purple")
# lower wall trim and wood plank floor
r.rect(0,72,320,8,"wood"); r.rect(0,73,320,2,"silver")
r.rect(0,80,320,160,"floor")
for y in range(82,240,10):
 r.line(0,y,319,y,"outline")
 start=(y//10%2)*17
 for x in range(start,320,34): r.line(x,y,x,y+9,"floor3")
# rug, stitch edge and geometric pattern
r.box(74,118,174,91,"red","outline"); r.rect(78,122,166,83,"woodlight")
r.rect(82,126,158,75,"red")
for x in range(86,238,12):
 r.px(x,130,"paper"); r.px(x,197,"paper")
for y in range(136,196,8):
 r.px(87,y,"paper"); r.px(235,y,"paper")
for x in range(96,230,9):
 r.line(x,139,x+2,143,"lavender"); r.line(x,187,x+2,191,"lavender")
# window with curtain / rain frame
r.box(24,16,66,47,"outline","outline"); r.rect(27,19,60,41,"blue2")
r.rect(30,22,54,35,"wall"); r.rect(32,24,50,31,"blue2")
r.line(57,23,57,55,"silver"); r.line(32,39,82,39,"silver")
r.rect(27,18,4,43,"lavender"); r.rect(82,18,4,43,"lavender")
for x in [34,43,51,66,77]: r.line(x,27,x-2,32,"silver")
# bookshelf
r.box(8,76,43,39,"wood"); r.rect(11,79,37,32,"wall2")
for i,c in enumerate(["purple","blue","green","red","silver"]):
 x=13+i*6; r.rect(x,81,4,12+(i%2)*3,c); r.line(x+1,82,x+1,88,"cream")
r.rect(11,96,37,3,"woodlight"); r.rect(11,106,37,3,"woodlight")
# wardrobe
r.box(94,12,49,61,"wood"); r.rect(97,15,43,55,"wood2")
r.box(100,19,17,35,"paper"); r.box(120,19,17,35,"paper")
r.line(109,22,109,50,"wood"); r.line(128,22,128,50,"wood")
r.px(113,37,"outline"); r.px(124,37,"outline"); r.rect(99,57,39,8,"blue2")
# bed on right, pillow, blanket, bed rail
r.box(210,78,99,72,"wood"); r.rect(214,82,91,64,"blue2")
r.box(218,84,34,20,"paper"); r.rect(221,87,28,14,"silver")
r.rect(253,95,49,47,"purple"); r.rect(257,99,41,39,"blue2")
for y in [104,113,122,131,140]: r.line(258,y,297,y,"lavender")
# bed posts and small plush silhouette
r.rect(212,78,5,72,"woodlight"); r.rect(302,78,5,72,"woodlight")
r.box(270,86,17,17,"paper"); r.px(274,91,"outline"); r.px(282,91,"outline"); r.line(275,97,281,97,"red")
# desk, chair and notebook
r.box(68,77,50,28,"wood"); r.rect(71,80,44,22,"wood2")
r.box(75,83,14,11,"paper"); r.line(78,86,86,86,"blue2"); r.line(78,89,84,89,"blue2")
r.box(93,82,18,15,"blue2"); r.rect(96,85,12,9,"lavender")
r.rect(73,105,4,12,"wood"); r.rect(109,105,4,12,"wood")
r.box(84,108,22,16,"wood"); r.rect(87,111,16,10,"blue2")
# retro radio on floor side
r.box(249,158,44,24,"wood"); r.rect(252,161,38,18,"wall2")
r.rect(255,164,19,11,"blue2"); r.rect(277,164,10,10,"woodlight")
for x in [279,283,287]: r.px(x,168,"outline")
r.line(256,163,268,163,"silver")
# small plant / candle / scattered floor objects
r.box(18,135,15,13,"wood"); r.rect(22,127,3,9,"green"); r.rect(18,131,4,4,"green"); r.rect(26,129,5,5,"green")
r.box(58,213,10,12,"paper"); r.rect(61,210,4,3,"gold")
r.box(275,207,13,10,"wood"); r.rect(279,201,4,7,"silver"); r.px(281,200,"gold")
r.box(154,218,14,7,"blue2"); r.px(158,216,"silver")
# details on wall: framed moon and snake-like original sigil
r.box(153,18,25,28,"wood"); r.rect(156,21,19,22,"wall2")
r.rect(164,25,6,6,"silver"); r.rect(162,25,2,2,"wall2"); r.px(169,28,"wall2")
for i in range(5): r.px(160+i,34+i%2,"green")
r.save("room.png")

# Sprite sheet: 3 frames x 4 directions, 16x24 each; simple original pixel character.
s=Img(48,96,(0,0,0,0))
def put(x,y,c): s.px(x,y,c)
for row in range(4):
 for col in range(3):
  ox=col*16; oy=row*24; shift=(-1 if col==1 else 1 if col==2 else 0)
  # hair/head and face
  for yy in range(3,10):
   for xx in range(4,12):
    if (xx in (4,11) and yy in (3,9)): continue
    put(ox+xx,oy+yy,"hair")
  if row==0:
   s.rect(ox+5,oy+6,6,4,"skin"); put(ox+6,oy+7,"ink"); put(ox+10,oy+7,"ink")
   s.rect(ox+4,oy+3,8,2,"hair")
  elif row in (1,2):
   s.rect(ox+(5 if row==1 else 4),oy+6,6,4,"skin"); put(ox+(6 if row==1 else 8),oy+7,"ink")
  else:
   s.rect(ox+4,oy+4,8,6,"hair")
  s.rect(ox+4,oy+10,8,7,"blue2"); s.rect(ox+4,oy+12,8,2,"lavender")
  s.rect(ox+5,oy+17,3,4,"silver"); s.rect(ox+9,oy+17,3,4,"silver")
  if col==1: s.rect(ox+3,oy+20,4,2,"silver"); s.rect(ox+10,oy+18,3,2,"silver")
  elif col==2: s.rect(ox+4,oy+18,3,2,"silver"); s.rect(ox+9,oy+20,4,2,"silver")
s.save("mio.png")

# 4-frame transparent rain overlay sheet, each frame 320x240.
rain=Img(320*4,240,(0,0,0,0))
for frame in range(4):
 for i in range(38):
  x=(i*47+frame*9)%320; y=(i*31+frame*7)%240
  rain.line(x,y,x-2,y+5,"silver")
rain.save("rain.png")

# Pixel inventory icons: 6 icons on a 16x16 grid, 3 columns x 2 rows.
icons=Img(48,32,(0,0,0,0))
for i,c in enumerate(["gold","silver","purple","blue","green","paper"]):
 ox=(i%3)*16; oy=(i//3)*16
 icons.box(ox+3,oy+3,10,10,c)
 icons.px(ox+7,oy+5,"cream"); icons.px(ox+6,oy+8,"outline")
icons.save("inventory.png")
print("Generated assets:", ", ".join(p.name for p in OUT.glob("*.png")))
