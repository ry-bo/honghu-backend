import os
import shutil
import requests

def get_pics():
    start_url = 'https://pixabay.com/api/?key=17342877-cb061dfd6503a5f3b5927cfb1&q=yellow+flowers&image_type=photo&pretty=true&lang=zh&per_page=60&orientation=vertical'
    res = requests.get(start_url)
    print(res.status_code)
    res_json = res.json()
    return res_json['hits']

def upload_to_honghu(pic):
    upload_url = 'http://127.0.0.1:8000/api/feeds/create'
    files = {'image': (pic['image'].split('/')[-1], open(pic['image'], 'rb'))}
    del pic['image']
    requests.post(upload_url, data=pic, files=files)

def down_pic(url):
    down_path = 'media/photologue/photos'
    file_name = url.split('/')[-1]
    if os.path.exists(os.path.join(down_path, file_name)):
        return
    r = requests.get(url=url, stream=True)
    if r.status_code == 200:
        with open(os.path.join(down_path, file_name), 'wb') as f:
            r.raw.decode_content = True
            shutil.copyfileobj(r.raw, f)      

if __name__ == "__main__":
    pic = {}
    down_path = 'media/photologue/photos'
    for p in get_pics():
        down_pic(p['previewURL'])
        file_name = p['previewURL'].split('/')[-1]
        pic = {
        "image": os.path.join(down_path, file_name),
        "title": ' '.join(p['pageURL'].split('/')[-2].split('-')[:-1]),
        "slug": p['pageURL'].split('/')[-2],
        "caption": p['tags'],
        'crop_from': "center",
        "is_public": True,
        }
        print(pic)
        upload_to_honghu(pic)
