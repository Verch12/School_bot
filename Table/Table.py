from PIL import Image, ImageDraw, ImageFont
from database.database import database

def imeg(id, all,x,y):
    url = 'Table/'+str(id)+'.jpg'
    print(all)

    f = open('database/database.info', 'r', encoding="utf-8")
    l = f.readline()
    info = l.strip("\n").split(",")
    f.close()

    if all[0] == True:
        im = Image.new('RGB', (155*(len(info)-1), 262), color=('#FFFFFF'))
        for q in range(len(info)-1):
            mass = database(x, q)
            draw = ImageDraw.Draw(im)

            draw.line(xy=((5+155*q, 5), (5+155*q, 257), (150+155*q, 257), (150+155*q, 5), (5+155*q, 5)), fill='#1C0606', width=2)

            font = ImageFont.truetype('Table/ofont.ru_Calibri.ttf', size=24)

            draw.text((66+155*q, 10),info[q],font=font,fill='#1C0606')
            for i in range(8):
                draw.line(xy=((5+155*q, (5+i*28)+28), (150+155*q, (5+i*28)+28)), fill='#1C0606', width=2)
                draw.text((10+155*q, (10+i*28)+28),mass[i],font=font,fill='#1C0606')
            im.save(url)

    if all[1] == True:
        im = Image.new('RGB', (155, 262*5), color=('#FFFFFF'))
        for q in range(5):
            mass = database(q, y)
            draw = ImageDraw.Draw(im)

            draw.line(xy=((5, 5+262*q), (5, 257+262*q), (150, 257+262*q), (150, 5+262*q), (5, 5+262*q)), fill='#1C0606', width=2)

            font = ImageFont.truetype('Table/ofont.ru_Calibri.ttf', size=24)

            draw.text((66, 10+262*q), info[y], font=font, fill='#1C0606')
            for i in range(8):
                # draw.line(xy=((30, 200),(130, 100),(80, 50)), fill='#1C0606', width=2)
                draw.line(xy=((5, ((5 + i * 28) + 28)+262*q), (150, q*262+((5 + i * 28) + 28))), fill='#1C0606', width=2)
                draw.text((10, ((10 + i * 28) + 28)+262*q), mass[i], font=font, fill='#1C0606')
            im.save(url)

    if all[0] == True and all[1] == True:
        im = Image.new('RGB', (155*(len(info)-1), 262 * 5), color=('#FFFFFF'))
        for z in range(len(info) - 1):
            for q in range(5):
                mass = database(q, z)
                draw = ImageDraw.Draw(im)

                draw.line(
                    xy=((5+155*z, 5 + 262 * q), (5+155*z, 257 + 262 * q), (150+155*z, 257 + 262 * q), (150+155*z, 5 + 262 * q), (5+155*z, 5 + 262 * q)),
                    fill='#1C0606', width=2)

                font = ImageFont.truetype('Table/ofont.ru_Calibri.ttf', size=24)

                draw.text((66+155*z, 10 + 262 * q), info[z], font=font, fill='#1C0606')
                for i in range(8):
                    draw.line(xy=((5+155*z, ((5 + i * 28) + 28) + 262 * q), (150+155*z, q * 262 + ((5 + i * 28) + 28))), fill='#1C0606',
                              width=2)
                    draw.text((10+155*z, ((10 + i * 28) + 28) + 262 * q), mass[i], font=font, fill='#1C0606')
                im.save(url)

    if all[0] == False and all[1] == False:
        mass = database(x, y)
        im = Image.new('RGB', (155, 262), color=('#FFFFFF'))
        draw = ImageDraw.Draw(im)

        draw.line(xy=((5, 5), (5, 257), (150, 257), (150, 5), (5, 5)), fill='#1C0606', width=2)

        font = ImageFont.truetype('Table/ofont.ru_Calibri.ttf', size=24)

        draw.text((66, 10), info[y], font=font, fill='#1C0606')
        for i in range(8):
            draw.line(xy=((5, (5 + i * 28) + 28), (150, (5 + i * 28) + 28)), fill='#1C0606', width=2)
            draw.text((10, (10 + i * 28) + 28), mass[i], font=font, fill='#1C0606')
        im.save(url)
    return url