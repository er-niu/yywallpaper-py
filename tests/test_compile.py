# -*- coding:utf-8 -*-
import re
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

# pat_link_son = re.compile('<b><a href="(.*?)" target="_blank">.*?</a></b><p>更新时间：2018-06-29</p></li><li>', re.S)
date = '2018-06-29'
pat_link_son = re.compile('<li><a href="(.*?)" title=".*?" target="_blank"><img.*?' + date + '</p>', re.S)

res_code_son = '<li><a href="/desk/20801.htm" title="小羽 粉色睡衣美女2k壁纸" target="_blank"><img src="http://img.netbian.com/file/2018/0629/9fe9d214db1b7f3ef994c750892369a2.jpg" alt="小羽 粉色睡衣美女2k壁纸" /></a><b><a href="/desk/20801.htm">小羽 粉色睡衣美女2k壁纸</a></b><p>更新时间：2018-06-29</p></li><li><a href="/desk/20800.htm" title="小羽 齐肩短发美女 黑色内衣美女2k壁纸" target="_blank"><img src="http://img.netbian.com/file/2018/0629/e047af96c58be0129eb1ff5e2bdd10bd.jpg" alt="小羽 齐肩短发美女 黑色内衣美女2k壁纸" /></a><b><a href="/desk/20800.htm">小羽 齐肩短发美女 黑色内衣美女2k壁纸</a></b><p>更新时间：2018-06-29</p></li><li><div class="pic_box"><a href="http://pic.netbian.com/" target="_blank"><img src="http://img.netbian.com/file/2017/0607/065f5dfcbff6dfe9671775ce8e7807af.jpg" alt="4K/5K/8K超清壁纸" /></a></div><p><a href="http://pic.netbian.com/" target="_blank" style="color:#FF0000;">【4K/5K/8K超清壁纸】</a></p></li><li><a href="/desk/20799.htm" title="小羽 黑色衣服内衣 高跟鞋 美女壁纸" target="_blank"><img src="http://img.netbian.com/file/2018/0629/d912f0a4a1f7a7efa8025e6a5d184fc4.jpg" alt="小羽 黑色衣服内衣 高跟鞋 美女壁纸" /></a><b><a href="/desk/20799.htm">小羽 黑色衣服内衣 高跟鞋 美女壁纸</a></b><p>更新时间：2018-06-29</p></li><li><a href="/desk/20787.htm" title="江琴 白色睡衣长发美女壁纸" target="_blank"><img src="http://img.netbian.com/file/2018/0627/9d2a8bc0cfb3d69ddfa8489af79cc01e.jpg" alt="江琴 白色睡衣长发美女壁纸" /></a><b><a href="/desk/20787.htm">江琴 白色睡衣长发美女壁纸</a></b><p>更新时间：2018-06-27</p></li><li><a href="/desk/20786.htm" title="江琴 白色内衣性感身材美女壁纸" target="_blank"><img src="http://img.netbian.com/file/2018/0627/75f8c6a43155b0278648aaf896c57555.jpg" alt="江琴 白色内衣性感身材美女壁纸" /></a><b><a href="/desk/20786.htm">江琴 白色内衣性感身材美女壁纸</a></b><p>更新时间：2018-06-27</p></li><li><a href="/desk/20781.htm" title="戴帽子的清纯美女2k壁纸" target="_blank"><img src="http://img.netbian.com/file/2018/0625/a25483176b2abd2b677e4822cb3e4433.jpg" alt="戴帽子的清纯美女2k壁纸" /></a><b><a href="/desk/20781.htm">戴帽子的清纯美女2k壁纸</a></b><p>更新时间：2018-06-25</p></li><li><a href="/desk/20778.htm" title="Huhu 时尚美女壁纸" target="_blank"><img src="http://img.netbian.com/file/2018/0625/8057b62ef627e76470b5de6141d696e5.jpg" alt="Huhu 时尚美女壁纸" /></a><b><a href="/desk/20778.htm">Huhu 时尚美女壁纸</a></b><p>更新时间：2018-06-25</p></li><li><a href="/desk/20770.htm" title="江琴 毛衣 美腿 靓丽美女壁纸" target="_blank"><img src="http://img.netbian.com/file/2018/0622/68f0e22f0d14ba5629b9fedc3b3a2460.jpg" alt="江琴 毛衣 美腿 靓丽美女壁纸" /></a><b><a href="/desk/20770.htm">江琴 毛衣 美腿 靓丽美女壁纸</a></b><p>更新时间：2018-06-22</p></li><li><a href="/desk/20767.htm" title="江琴 白裙子美女壁纸" target="_blank"><img src="http://img.netbian.com/file/2018/0622/01edb40315d914280a4c844dc7e263a3.jpg" alt="江琴 白裙子美女壁纸" /></a><b><a href="/desk/20767.htm">江琴 白裙子美女壁纸</a></b><p>更新时间：2018-06-22</p></li><li><a href="/desk/20752.htm" title="美女芸斐高清壁纸" target="_blank"><img src="http://img.netbian.com/file/2018/0619/c60eae0479f3fe47256c76d3cea94a9e.jpg" alt="美女芸斐高清壁纸" /></a><b><a href="/desk/20752.htm">美女芸斐高清壁纸</a></b><p>更新时间：2018-06-19</p></li><li><a href="/desk/20751.htm" title="芸斐 美女模特芸斐壁纸" target="_blank"><img src="http://img.netbian.com/file/2018/0619/d6e6bfe572cc64fbc70af53d100fbf0c.jpg" alt="芸斐 美女模特芸斐壁纸" /></a><b><a href="/desk/20751.htm">芸斐 美女模特芸斐壁纸</a></b><p>更新时间：2018-06-19</p></li><li><a href="/desk/20744.htm" title="江琴 沙发 养眼美腿美女江琴壁纸" target="_blank"><img src="http://img.netbian.com/file/2018/0615/bdba0129c73ae2c4093bae65169111d3.jpg" alt="江琴 沙发 养眼美腿美女江琴壁纸" /></a><b><a href="/desk/20744.htm">江琴 沙发 养眼美腿美女江琴壁纸</a></b><p>更新时间：2018-06-15</p></li><li><a href="/desk/20743.htm" title="江琴 美腿美女壁纸" target="_blank"><img src="http://img.netbian.com/file/2018/0615/cbd81a01ba3c8be314631ed3413f121c.jpg" alt="江琴 美腿美女壁纸" /></a><b><a href="/desk/20743.htm">江琴 美腿美女壁纸</a></b><p>更新时间：2018-06-15</p></li><li><a href="/desk/20728.htm" title="漂亮空姐凌雪桌面壁纸" target="_blank"><img src="http://img.netbian.com/file/2018/0611/e74bf03761701d05328bca3b9abf30e9.jpg" alt="漂亮空姐凌雪桌面壁纸" /></a><b><a href="/desk/20728.htm">漂亮空姐凌雪桌面壁纸</a></b><p>更新时间：2018-06-11</p></li><li><a href="/desk/20726.htm" title="凌雪 气质空姐美女壁纸" target="_blank"><img src="http://img.netbian.com/file/2018/0611/dbbb6c439f71d6406bca18a9788631c7.jpg" alt="凌雪 气质空姐美女壁纸" /></a><b><a href="/desk/20726.htm">凌雪 气质空姐美女壁纸</a></b><p>更新时间：2018-06-11</p></li><li><a href="/desk/20719.htm" title="凌雪 空姐制服美女壁纸" target="_blank"><img src="http://img.netbian.com/file/2018/0608/6a1742b8e3f1aaa79467d27f73e962a6.jpg" alt="凌雪 空姐制服美女壁纸" /></a><b><a href="/desk/20719.htm">凌雪 空姐制服美女壁纸</a></b><p>更新时间：2018-06-08</p></li><li><a href="/desk/20718.htm" title="江琴 长发养眼美女壁纸" target="_blank"><img src="http://img.netbian.com/file/2018/0608/d764b654b2e7aaa97ecc070f7cb6d890.jpg" alt="江琴 长发养眼美女壁纸" /></a><b><a href="/desk/20718.htm">江琴 长发养眼美女壁纸</a></b><p>更新时间：2018-06-08</p></li>'
res_link = re.findall(pat_link_son, res_code_son.encode('utf-8'))

for link in res_link:
    print(link)