'''
## GitHub Repo Downloader
- Program to download public GitHub repo and store that repo to the local storage.
'''

try:
    import sys
    import os
    import requests
    import shutil
    import json

    class GitReD_downloader:
        def __init__(self, owner, repo, save_in_folder=True, keep_zip_saved=False) -> None:
            self.__owner = owner
            self.__repo = repo
            self.__save_in_folder=save_in_folder
            self.__keep_zip_saved=keep_zip_saved
            self.__branch = None
            self.__lock=False

        def __need_to_return(self):
            if self.__branch==None:
                self.__identify_branch()
            if self.__lock==True:
                return True
            return False

        def __identify_branch(self):
            try:
                branch_request = requests.get(f'https://api.github.com/repos/{self.__owner}/{self.__repo}/branches/main')
                if branch_request.status_code==200:
                    self.__branch = json.loads(branch_request.text)['name']
                else:
                    self.__lock=True
            except Exception as e:
                print(e)
        
        def __download_zip(self):
            if self.__need_to_return():
                return
            try:
                zip_file = requests.get(f'https://github.com/{self.__owner}/{self.__repo}/archive/refs/heads/{self.__branch}.zip')
                try:
                    with open(f'{self.__repo}.zip','wb') as file:
                        file.write(zip_file.content)
                except Exception as e:
                    print(e)
            except Exception as e:
                print(e)

        def __extract_zip(self):
            if self.__need_to_return():
                return
            try:
                source = f'{self.__repo}.zip'
                if not os.path.exists(source):
                    return {"status":False,"message":'source not exists'}
                shutil.unpack_archive(source)
            except Exception as e:
                print(e)
            if self.__keep_zip_saved==False:
                # Delete zip file
                os.remove(source)

        def __move_to_parent(self):
            if self.__need_to_return():
                return

            if self.__save_in_folder==False:
                try:
                    source = f"{self.__repo}-{self.__branch}"
                    
                    if os.path.exists(source):
                        # Code to move the files from sub-folder to main folder.
                        files = [os.path.join(source, file) for file in os.listdir(source)]
                        cwd = os.getcwd()
                        for file in files:
                            shutil.move(file,f'{cwd}/')
                        os.rmdir(source)
                        return True
                    return {"status":False,"message":'Source not exists'}
                except Exception as e:
                    print(e)
        
        def download(self):
            self.__download_zip()
            self.__extract_zip()
            self.__move_to_parent()

    if __name__=="__main__":
        repo_downloader = GitReD_downloader(f'{sys.argv[1]}', f'{sys.argv[2]}', json.loads(sys.argv[3].lower()), json.loads(sys.argv[4].lower()))
        repo_downloader.download()
except Exception as e:
    print(e)