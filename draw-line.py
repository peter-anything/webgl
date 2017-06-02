#!/usr/bin/env python
#coding: utf-8

from PIL import Image, ImageDraw

def jiaoxian_save_preview():
    '''渲染角线的preview.png'''
    no = 'b16ee7fcb62511e1ac95782bcb748630'
    record = {"materialNo":"b16ee7fcb62511e1ac95782bcb748630","width":1.8768,"length":40,"points":[{"y":-1.3099,"x":-0.3711},{"y":-1.0017,"x":-0.3711},{"y":-1.0017,"x":0.0908},{"y":0.6629,"x":0.0908},{"y":1.464,"x":0.9384},{"y":1.9264,"x":0.9384},{"y":5.0085,"x":0.7631},{"y":5.0085,"x":-0.9384},{"y":-5.0085,"x":-0.9384},{"y":-5.0085,"x":-0.4213},{"y":-2.2346,"x":-0.4213},{"y":-2.2346,"x":0.0675},{"y":-1.7707,"x":0.5645},{"y":-1.3099,"x":0.0646}],"height":10.017}
    points = [(50 * each['x'], 50 * each['y']) for each in record['points']]

    pic_width = 512 #图片尺寸
    padding_precent = 0.9 #填充百分比
    # zippoints = zip(*points)

    # zippoints = [zippoint for zippoint in zippoints]

    # min_x = min(zippoints[0])
    # min_y = min(zippoints[1])

    # range_x = max(zippoints[0]) - min_x
    # range_y = max(zippoints[1]) - min_y

    # maxxy = max(range_x, range_y)

    # print(maxxy)

    # scale = pic_width * padding_precent / maxxy

    # print(scale)


    newIm = Image.new("RGBA",(pic_width, pic_width), (255, 255, 255, 0))
    drawIm = ImageDraw.Draw(newIm)
    # print(points)
    # newp = lambda p:(int(p[0] * scale + pic_width / 2), int(pic_width / 2 - p[1] * scale))
    # new_points = map(newp, points)

    # new_points = [new_point for new_point in new_points]

    # print(new_points)

    # new_points.append(new_points[0])
    drawIm.line(points, (0, 0, 0), width=4) #线条的粗细

    file_path = 'jiaoxian_%s_preview.png' % no
    newIm.save(file_path)
    photo_file = open(file_path, 'rb')
    item = IfuwoItem.objects.get(no=no)
    item.save_photo(photo_file, 'preview')
    photo_file.close()
    os.remove(file_path)

jiaoxian_save_preview()

