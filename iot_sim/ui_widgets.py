"""Metin sarma ve kimlikli butonlar; çizimle tıklama alanı aynı kayıttadır."""
import pygame

BG=(12,19,28)
PANEL=(23,33,46)
TEXT=(224,234,244)
MUTED=(147,166,184)
ACCENT=(91,211,194)
BORDER=(47,64,81)


def wrap_text(text, font, width):
    """Uzun sözcük dahil metni piksel genişliğine göre satırla."""
    lines=[]
    for paragraph in str(text).split("\n"):
        line=""
        for word in paragraph.split():
            candidate=f"{line} {word}".strip()
            if font.size(candidate)[0]<=width:
                line=candidate
                continue
            if line:
                lines.append(line)
                line=""
            for char in word:
                if font.size(line+char)[0]>width and line:
                    lines.append(line)
                    line=""
                line+=char
        lines.append(line)
    return lines


def text_block(surface, text, x, y, width, font, color=TEXT, gap=4):
    """Satırları çiz ve sonraki boş y koordinatını döndür."""
    for line in wrap_text(text,font,max(10,width)):
        surface.blit(font.render(line,True,color),(x,y))
        y+=font.get_height()+gap
    return y


def button(surface, rect, label, font, active=False, enabled=True):
    """Etkin/seçili durumu çiz; etiket dar alanda küçültülür."""
    pygame.draw.rect(surface,(35,75,77) if active else PANEL,rect,border_radius=8)
    pygame.draw.rect(surface,ACCENT if active else BORDER,rect,1,border_radius=8)
    color=TEXT if enabled else MUTED
    chosen=font
    while chosen.size(label)[0]>rect.width-12 and chosen.get_height()>13:
        chosen=pygame.font.SysFont("DejaVu Sans",chosen.get_height()-3)
    image=chosen.render(label,True,color)
    surface.blit(image,(rect.centerx-image.get_width()/2,rect.centery-image.get_height()/2))
