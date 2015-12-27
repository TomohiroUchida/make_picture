# coding: Shift-JIS 
#OSXの場合はUTF-8
from PIL import Image, ImageDraw, ImageFont

#ディスプレイのサイズによる設定
HEIGHT_PIC = 16

#表示する文字の設定
TEXT = u"英語を話せることがそんなに偉いんですか。"
BK_COLOR = "blue"
FONT_COLOR = "white"
WIDTH_PIC = len(TEXT)*HEIGHT_PIC
FONT = ImageFont.truetype(r"C:\Windows\Fonts\msmincho.ttc", HEIGHT_PIC,encoding="unic")

IMAGE = Image.new('RGB', (WIDTH_PIC, HEIGHT_PIC), color=BK_COLOR)
DRAW = ImageDraw.Draw(IMAGE)
DRAW.text((0, 0), TEXT, font=FONT, fill=FONT_COLOR)
IMAGE.show()
IMAGE.save(r"C:\Users\tomohiro\Desktop\text imag.jpg", "JPEG", quality=100, optimize=True)
