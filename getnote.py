import requests
from bs4 import BeautifulSoup
import os


def gettitle(url):
  s = requests.Session()
  res = s.get(url)
  soup = BeautifulSoup(res.text, 'html.parser')
  title = soup.find('h2', class_='info__title').text.replace(' ', '')
  tag = soup.find_all('a', class_='info__cat__desc__btn')
  path = '%s\\%s\\%s'%(tag[0].text, tag[1].text, title)
  return path, title
  

def getimg(url):
  res = requests.get(url)
  if '404' in res.text:
    return None
  else:
    soup = BeautifulSoup(res.text, 'html.parser')
    return soup.find('img')

def writehtml(imgs):
  f = open('pics.html', 'w')
  for img in imgs:
    f.write('%s\n'%str(img))
  f.close()
  
def downpic(url):
  s = requests.Session()
  pic = s.get(url)
  return pic.content
  
  
  
  
  
'''
def getnoteid():
  print('(1)mathematics (2)english (3)chinese (4)chemistry (6)physics (7)biology (8)earth-science')
  n = int(input('subjects : '))
  subs = ['mathematics','english','chinese','chemistry','physics','biology','earth-science']
  url = 'https://www.clearnotebooks.com/zh-TW/notebooks/grade/senior-high/subject/%s?order=like_counts_desc'%subs[n]
  s = requests.Session()
  res = s.get(url)
  soup = BeautifulSoup(res.text, 'html.parser')
  li = soup.find_all('a', class_='noteinfo-title__btn')
  for i in li:
    print(li.text, 'note_id :', li['href'].split('/')[-1])
  note_id = input('note_id')
  return note_id
'''  
  
  
#note_id = url.split('/')[-1]
#note_id = getnoteid()
note_id = input('note_id:')
url = 'https://www.clearnotebooks.com/zh-TW/notebooks/%s'%note_id
u = 'https://www.clearnotebooks.com/zh-TW/public_page?note_id=%s&page='%note_id

path, title = gettitle(url)

imgs = []
n = 0
while True:
  url = '%s%s'%(u, n)
  img = getimg(url)
  if img == None:
    break
  imgs.append(img['src'])
  print(img)
  n += 1

path = path.replace(':','').replace('?', '').replace('*', '').replace('>', '').replace('<', '').replace('|', '')
os.system('mkdir "%s"'%path)
print(path)
for i in range(len(imgs)):
  fname = '%s\\%s-%s.jpg'%(path, title, i)
  fname = fname.replace(':','').replace('?', '').replace('*', '').replace('>', '').replace('<', '').replace('|', '')
  f = open(fname, 'wb')
  f.write(downpic(imgs[i]))
  f.close()
  print('saved %s'%fname)
  
  
  
  
  
  
  
  
  