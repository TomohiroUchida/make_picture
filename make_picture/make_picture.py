# coding: Shift-JIS 
#OSX�̏ꍇ��UTF-8
from PIL import Image, ImageDraw, ImageFont

#�f�B�X�v���C�̃T�C�Y�ɂ��ݒ�
HEIGHT_PIC = 16

#�\�����镶���̐ݒ�
TEXT = u"�p���b���邱�Ƃ�����ȂɈ̂���ł����B"
BK_COLOR = "blue"
FONT_COLOR = "white"
WIDTH_PIC = len(TEXT)*HEIGHT_PIC
FONT = ImageFont.truetype(r"C:\Windows\Fonts\msmincho.ttc", HEIGHT_PIC,encoding="unic")

IMAGE = Image.new('RGB', (WIDTH_PIC, HEIGHT_PIC), color=BK_COLOR)
DRAW = ImageDraw.Draw(IMAGE)
DRAW.text((0, 0), TEXT, font=FONT, fill=FONT_COLOR)
IMAGE.show()
IMAGE.save(r"C:\Users\tomohiro\Desktop\text imag.jpg", "JPEG", quality=100, optimize=True)
