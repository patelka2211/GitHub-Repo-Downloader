'''
## GitHub Repo Downloader
- Program to download public GitHub repo and store that repo to the local storage.
'''

import os
import requests
import shutil

class GitReD:
    def __init__(self, owner, repo, dest='.', keep_zip_saved=False) -> None:
        self.__owner = owner
        self.__repo = repo
        self.__dest = dest
        self.__keep_zip_saved = keep_zip_saved
        # self.__dest = os.getcwd()
        self.__branch = None

    def identify_branch(self):
        try:
            branch_request = requests.get(f'https://api.github.com/repos/{self.__owner}/{self.__repo}/branch/main')
            if branch_request!=200:
                self.__branch = 'master'
            else:
                self.__branch = 'main'
        except Exception as e:
            print(e)
    
    def download_zip(self):
        if self.__branch==None:
            self.identify_branch()
        try:
            zip_file = requests.get(f'https://github.com/{self.__owner}/{self.__repo}/archive/refs/heads/{self.__branch}.zip')
            if not os.path.exists(self.__dest):
                os.mkdir(self.__dest)
            try:
                with open(f'{self.__dest}/{self.__repo}.zip','wb') as file:
                    file.write(zip_file.content)
            except Exception as e:
                print(e)
        except Exception as e:
            print(e)

    def extract_zip(self):
        try:
            source = f'{self.__dest}/{self.__repo}.zip'
            if not os.path.exists(source):
                return {"status":False,"message":'source not exists'}
            shutil.unpack_archive(source, self.__dest)
        except Exception as e:
            print(e)

        if self.__keep_zip_saved==False:
            # Delete zip file
            os.remove(source)

    def move_to_parent(self):
        if self.__branch==None:
            self.identify_branch()
        try:
            source = f"{self.__dest}/{self.__repo}-{self.__branch}"
            if not os.path.exists(source):
                return {"status":False,"message":'source not exists'}

            # code to move the files from sub-folder to main folder.
            files = os.listdir(source)
            for file in files:
                file_name = os.path.join(source, file)
                shutil.move(file_name, self.__dest)
            os.rmdir(source)
        except Exception as e:
            print(e)
    
    def download(self, dest='.', keep_zip_saved=False):
        self.__dest = dest
        self.__keep_zip_saved = keep_zip_saved
        self.download_zip()
        self.extract_zip()
        self.move_to_parent()


if __name__=="__main__":
    
    # owner/repo
    # github/linguist

    repo_downloader = GitReD('github', 'linguist')

    repo_downloader.download(dest='github_linguist', keep_zip_saved=True)