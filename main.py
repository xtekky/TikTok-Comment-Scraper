import os
import json
try:
  import requests
  import shutil
except:
  os.system('pip install -q requests')
  os.system('pip install -q shutil')

ExportResponse_toJson = False
Iteration       = 0
CursorIteration = 0
ComIteration    = 0
Count           = '999999'
HostUrl         = 'https://www.tiktok.com/api/comment/list/?aid=1988&aweme_id='


def TerminalInput():
    print("TikTok Comment Scraper".center(shutil.get_terminal_size().columns))
    print("By Tekky [.gg/onlp]".center(shutil.get_terminal_size().columns))
    print('\n')
    VideoID     = input('          [?] TikTok link > ')
    Iteration   = input('          [?] How Many Iteration > ')
    Export      = input('          [?] Export? (y/n) ')  
    if "vm.tiktok.com" in VideoID or "vt.tiktok.com" in VideoID:
        VideoID = requests.head(VideoID, stream=True, allow_redirects=True, timeout=5).url.split("/")[5].split("?", 1)[0]
    else:
        VideoID = VideoID.split("/")[5].split("?", 1)[0]
    if Export != 'y':    
        PrintComments(VideoID, Count, CursorIteration, ComIteration, Iteration, Export)
    else:
        Export = True
        PrintComments(VideoID, Count, CursorIteration, ComIteration, Iteration, Export)


def ExportResponse_toJson(VideoID, Count, CursorIteration, response):    
    with open (VideoID + '.json', 'w') as f:
        json.dump(response, f, indent=4)    
        
def PrintComments(VideoID, Count, CursorIteration, ComIteration, Iteration, Export):
    Headers         = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
        'referer': f'https://www.tiktok.com/@x/video/{VideoID}',
    }
    i = 0
    while i <= int(Iteration):
        response = requests.get(f"{HostUrl}{VideoID}&count={Count}&cursor={CursorIteration}", headers=Headers).json()    
        for x in range(len(response["comments"])):
            print(response["comments"][x]["text"])
            ComIteration += 1
        CursorIteration += 50
        i += 1
        print(ComIteration)
        if Export == True:
            ExportResponse_toJson(VideoID, Count, CursorIteration, response)

if __name__ == '__main__':
    TerminalInput()