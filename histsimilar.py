# Filename: histsimilar.py
# -*- coding: utf-8 -*-

import Image

def make_regalur_image(img, size = (256, 256)):
    return img.resize(size).convert('RGB')
#����ת�䣬ȫ��ת��Ϊ256*256���ش�С

def split_image(img, part_size = (64, 64)):
    w, h = img.size
    pw, ph = part_size
    
    assert w % pw == h % ph == 0
    
    return [img.crop((i, j, i+pw, j+ph)).copy() \
                for i in xrange(0, w, pw) \
                for j in xrange(0, h, ph)]
#region = img.crop(box)
#��img��ʾ��ͼƬ���󿽱���region�У����region�������������Ĳ�����region��ʵ����һ��
#image����box�Ǹ���Ԫ�飨�������ң���

def hist_similar(lh, rh):
    assert len(lh) == len(rh)
    return sum(1 - (0 if l == r else float(abs(l - r))/max(l, r)) for l, r in zip(lh, rh))/len(lh)
#�����Ǹ���ͼƬ�����Ҽ��������ĳ�����ȣ�zip�ǿ��Խ��ܶ��x,y,z����ֵͳһ�����������
def calc_similar(li, ri):
#   return hist_similar(li.histogram(), ri.histogram())
    return sum(hist_similar(l.histogram(), r.histogram()) for l, r in zip(split_image(li), split_image(ri))) / 16.0 #256>64
    #����histogram()������x�����������ȡ���õ��ģ�����ֱ��ͼͳ�ƣ���������x��ȡֵ��Χ��Ϊ100�����䣬
        #��ͳ��x�е�ÿ��ֵ������������еĴ�����histogram()������������p��t2��
        #����p��ʾ���������ȡ��ֵ���ֵ�Ƶ����t2��ʾ���䡣
        #����Ǽ���һ�����ص��ж�����ɫ�ֲ���
        #��split_image����Ķ���zipһ�£�����histogram,Ȼ��õ����ֵ

def calc_similar_by_path(lf, rf):
    li, ri = make_regalur_image(Image.open(lf)), make_regalur_image(Image.open(rf))
    return calc_similar(li, ri)

def make_doc_data(lf, rf):
    li, ri = make_regalur_image(Image.open(lf)), make_regalur_image(Image.open(rf))
    li.save(lf + '_regalur.png')#ת��ͼƬ��ʽ:img.save('file.jpg'),������ʱ��
    ri.save(rf + '_regalur.png')#img����Ӳ��
    fd = open('stat.csv', 'w')#statģ�������������ͳ�Ƶģ�stat���������������������ֵ�ͷ���
        #����ǹؼ�������histogram�Ľ������map����
    fd.write('\n'.join(l + ',' + r for l, r in zip(map(str, li.histogram()), map(str, ri.histogram()))))
#   print >>fd, '\n'
#   fd.write(','.join(map(str, ri.histogram())))
    fd.close()
    import ImageDraw
    li = li.convert('RGB') #��save��������ת����ʽ
    draw = ImageDraw.Draw(li)
    for i in xrange(0, 256, 64):
        draw.line((0, i, 256, i), fill = '#ff0000')
        draw.line((i, 0, i, 256), fill = '#ff0000')
        #��ʼ���ջ���!!!!!!!!!!!!!!!ͨ����ÿһ��ˢ�ɺ�ɫ����������ɫ������ֲ�����
        #�÷���pygame.draw.line(Surface, color, start_pos, end_pos, width=1)
    li.save(lf + '_lines.png')
    

if __name__ == '__main__':
    path = r'testpic/TEST%d/%d.JPG'
    for i in xrange(1, 7):
        print 'test_case_%d: %.3f%%'%(i, \
            calc_similar_by_path('testpic/TEST%d/%d.JPG'%(i, 1), 'testpic/TEST%d/%d.JPG'%(i, 2))*100)
    
#   make_doc_data('test/TEST4/1.JPG', 'test/TEST4/2.JPG')  