from PySide6.QtGui import QTextCharFormat, QColor, QPixmap, QIcon, QPainter, QPainterPath, QPen, QFont, QTransform, QFontDatabase, QFontMetrics
from PySide6.QtCore import Qt, QRect
from Settings import Settings, box_sizes, default_value, bg_images, box_color
import math


def hexRgba_to_hexArgb(color: str, alphaEnabled=True) -> str:
    color = color.replace("#", "")
    alpha = color[6:8] if alphaEnabled else "ff"
    return "#" + alpha + color[0:6]

def hexArgb_to_hexRgba(color: str, alphaEnabled=True) -> str:
    color = color.replace("#", "")
    alpha = color[0:2] if alphaEnabled else "ff"
    return "#" + color[2:8] + alpha


def set_color(window, key, uiElem, color):
    if type(color) == str:
        color = QColor(color)
    if color.isValid():
        qt_hex = hexArgb_to_hexRgba(color.name(QColor.NameFormat.HexArgb)).replace("#", "")
        if (window.ui.selected_expr.value() < len(window.deser.expressions)
            and window.ui.selected_expr.isEnabled()):
            setattr(window.deser.expressions[window.ui.selected_expr.value()], key, qt_hex)
        pixmap = QPixmap(32, 32)
        pixmap.fill(Qt.GlobalColor.transparent)
        painter = QPainter(pixmap)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing, False)

        # Outer border (dark, visible on light themes)
        painter.fillRect(0, 0, 32, 32, QColor(0, 0, 0, 180))
        # Inner border (light, visible on dark themes)
        painter.fillRect(2, 2, 28, 28, QColor(255, 255, 255, 120))

        # Checkerboard pattern (shows through transparent colors)
        checker_size = 4  # px per square
        for row in range(6):  # 24px / 4px = 6 rows
            for col in range(6):  # 6 cols
                if (row + col) % 2 == 0:
                    checker_color = QColor(200, 200, 200, 255)
                else:
                    checker_color = QColor(255, 255, 255, 255)
                painter.fillRect(
                    4 + col * checker_size,
                    4 + row * checker_size,
                    checker_size,
                    checker_size,
                    checker_color
                )

        # Color fill (drawn on top — transparent colors let checker show through)
        painter.fillRect(4, 4, 24, 24, color)

        painter.end()

        uiElem.setIcon(QIcon(pixmap))
        uiElem.setText(" #" + qt_hex)

def replace_placeholders(text):
    placeholders_indicators = [r"\[0\]", r"\[1\]", r"\[2\]", r"\[3\]", r"\[4\]", r"\[5\]"]
    placeholders = Settings.value("placeholders")
    for i, p in enumerate(placeholders_indicators):
        text = text.replace(p, placeholders[i])
    return text

def draw_text(window, mess):
    #base character width and heights, from the font
    base_width = 33
    base_height = 41

    #all message related data
    text = replace_placeholders(mess.text)
    exp_index = mess.exp_index
    expr = window.deser.expressions[exp_index]
    width = expr.width
    height = expr.height
    h_spacing = expr.horizontal_spacing
    v_spacing = expr.vertical_spacing
    color = QColor(hexRgba_to_hexArgb(expr.color, Settings.value("renderAlpha", type=bool)))
    outline_color = QColor(hexRgba_to_hexArgb(expr.outline)) if Settings.value("renderOutline", type=bool) else QColor("#00000000")

    #set up pixmap
    textbox_w, textbox_h = (box_sizes(Settings.value("boxSizeIndex", type=int))
        if not Settings.value("customDimensions", type=bool)
        else (Settings.value("boxWidth", type=int), Settings.value("boxHeight", type=int)))
    pixmap = QPixmap(textbox_w, textbox_h)
    pixmap.setDevicePixelRatio(1.0)
    alpha = 255 if not Settings.value("transluscentBox", type=bool) else Settings.value("boxAlpha", type=int)
    pixmap.fill(QColor(f"#{alpha:02x}{box_color(Settings.value('boxColorIndex', type=int))}"))
    painter = QPainter(pixmap)
    painter.setRenderHint(QPainter.Antialiasing)
    painter.setPen(QPen(outline_color, 2))
    painter.setBrush(color)

    side_margins = 25
    transform = QTransform()
    transform.scale(width / base_width, height / base_height)
    painter.setTransform(transform)
    boundaries = painter.transform().inverted()[0].mapRect(QRect(0, 0, pixmap.width() - side_margins, pixmap.height()))
    #the ruby divisor, makes ruby text smaller, arbirtary
    ruby_factor = 1.6

    #font related settings
    game_font = QFontDatabase.applicationFontFamilies(window.ui.gameView.font_id)
    font_id = 0
    for i, font in enumerate(game_font):
        if font.endswith("M"):
            font_id = i
    base_font = QFont(game_font[font_id], base_width)
    ruby_font = QFont(game_font[font_id], base_width // ruby_factor)
    painter.setFont(ruby_font)
    ruby_fm = QFontMetrics(painter.font())
    painter.setFont(base_font)
    fm = QFontMetrics(painter.font())


    start_x = side_margins
    x = start_x
    y = fm.ascent() + ruby_fm.ascent()
    cur_text = ""
    i = 0

    def flush(cur_text, x, y):
        painter.setFont(base_font)
        path = QPainterPath()
        skip = []
        for i, c in enumerate(cur_text):
            #icon found
            if i in skip:
                continue
            if cur_text[i:i+3] == r"\[b" and cur_text[i+4:i+6] == r"\]":
                x, y, = draw_icon(x, y, f":/icons/buttons/{cur_text[i+2:i+4]}.png", painter.brush().color(), painter.pen().color())
                skip.extend(list(range(i, i+6)))
                continue
            #per-letter wrapping, as is in Wii Party
            if x + fm.horizontalAdvance(c) + h_spacing >= boundaries.width():
                x, y = new_line(x, y)
            path.addText(x, y, painter.font(), c)
            x += fm.horizontalAdvance(c) + h_spacing
        painter.drawPath(path)
        return x, y

    def ruby_flush(ruby_text, text, beg_x, end_x):
        painter.setFont(ruby_font)
        ruby_y = (y - fm.lineSpacing() - v_spacing // 2) + ruby_fm.lineSpacing() // ruby_factor
        ruby_width = sum(ruby_fm.horizontalAdvance(c) + h_spacing // 2 for c in ruby_text)
        x = (end_x + beg_x) // 2
        x -= ruby_width // 2 #right aligned
        path = QPainterPath()
        for c in ruby_text:
            path.addText(x, ruby_y, painter.font(), c)
            x += ruby_fm.horizontalAdvance(c) + h_spacing // 2
        painter.drawPath(path)
        return x

    def new_line(x, y):
        y += fm.lineSpacing() + v_spacing
        x = start_x
        return x, y

    def draw_icon(x, y, icon, color, stroke_color):

        mask_pixmap = QPixmap(icon)
        bitmap_mask = mask_pixmap.createMaskFromColor(QColor(Qt.black), Qt.MaskInColor)
        mask_pixmap.setMask(bitmap_mask)

        # Scale up 1.2x
        scale = 1.3
        new_w = int(mask_pixmap.width() * scale)
        new_h = int(mask_pixmap.height() * scale)
        scaled_mask = mask_pixmap.scaled(new_w, new_h, Qt.KeepAspectRatio, Qt.SmoothTransformation)

        # Recolored icon
        recolored = QPixmap(scaled_mask.size())
        recolored.fill(Qt.transparent)
        if x + recolored.width() + h_spacing >= boundaries.width():
            x, y = new_line(x, y)
        p = QPainter(recolored)
        p.setRenderHint(QPainter.Antialiasing)
        p.setRenderHint(QPainter.SmoothPixmapTransform)
        p.fillRect(recolored.rect(), color)
        p.setCompositionMode(QPainter.CompositionMode_DestinationIn)
        p.drawPixmap(0, 0, scaled_mask)
        p.end()

        # Stroke pixmap
        stroke_width = 2
        stroke_pixmap = QPixmap(scaled_mask.size())
        stroke_pixmap.fill(Qt.transparent)
        p = QPainter(stroke_pixmap)
        p.setRenderHint(QPainter.Antialiasing)
        p.setRenderHint(QPainter.SmoothPixmapTransform)
        p.fillRect(stroke_pixmap.rect(), stroke_color)
        p.setCompositionMode(QPainter.CompositionMode_DestinationIn)
        p.drawPixmap(0, 0, scaled_mask)
        p.end()

        # Draw stroke with antialiasing via opacity falloff
        draw_y = y - fm.ascent() + new_h // 4
        for dx in range(-stroke_width, stroke_width + 1):
            for dy in range(-stroke_width, stroke_width + 1):
                dist = math.sqrt(dx*dx + dy*dy)
                if dist <= stroke_width:
                    # Fade opacity at the edges for smooth antialiased look
                    opacity = 1.0 - (dist / stroke_width) * 0.5
                    painter.setOpacity(opacity)
                    painter.drawPixmap(x + dx, draw_y + dy, stroke_pixmap)

        painter.setOpacity(1.0)
        painter.drawPixmap(x, draw_y, recolored)

        return x + recolored.width() + h_spacing, y


    while i < len(text):
        #color tag found, update brush color for future text
        if i + 12 < len(text) and text[i:i+4] == "[c:#" and text[i+12] == "]":
            x, y = flush(cur_text, x, y)
            painter.setBrush(QColor(hexRgba_to_hexArgb(text[i+4:i+12], Settings.value("renderAlpha", type=bool))))
            cur_text = ""
            i += 13 #skips past color tag
        #ruby tag found
        elif text[i:i+3] == "[r:" and not text.find("[/r]", i) == -1:
            x, y = flush(cur_text, x, y)
            pos = i + 3
            cur_text = ""
            ruby_text = ""
            #gather ruby text
            while pos < len(text) and not text[pos] == "]":
                ruby_text += text[pos]
                pos += 1
            pos += 1
            #gather text to put ruby text over
            while pos < len(text) and not text[pos:pos+4] == "[/r]":
                cur_text += text[pos]
                pos += 1
            end_x, _ = flush(cur_text, x, y)
            ruby_flush(ruby_text, cur_text, x, end_x)
            cur_text = ""
            x = end_x
            i = pos + 4 #places at end of ruby tag
        #new line found
        elif text[i] == "\n":
            x, y = flush(cur_text, x, y)
            cur_text = ""
            x, y = new_line(x, y)
            i += 1
        #nothing found, gather text
        else:
            cur_text += text[i]
            i += 1

    #print any remaining text
    x, y = flush(cur_text, x, y)


    painter.end()
    window.ui.gameView.setPixmap(pixmap)


def render_game_view(window):
    window.ui.gameView.clear()
    if not window.selected_message == None:
        draw_text(window, window.deser.messages[window.selected_message])