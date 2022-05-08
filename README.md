# GitHub-Repo-Downloader
<div style="width: 100%;text-align: center;">
    <div title="patelka2211/GitHub-Repo-Downloader on GitHub" style="display: flex;flex-direction: column;align-items: center;justify-content: space-around; max-width: 100vw; margin: auto; padding: 0.6vh;border: 1px solid #b9bbbe99; border-radius: 1.6vh;">
        <img src="https://opengraph.githubassets.com/126f5rfsv12/patelka2211/GitHub-Repo-Downloader" alt="" style="width: 100%;height: 100%;border-radius: 1vh;">
        <div style="margin: 5px auto;color: #58a6ff;">
            github.com /
            <code>
            <a href="https://github.com/patelka2211/GitHub-Repo-Downloader" title="patelka2211/GitHub-Repo-Downloader on GitHub" target="blank_" style="cursor: pointer;">
                <a href="https://github.com/patelka2211" title="patelka2211 on GitHub" style="text-decoration: none;color: #58a6ff;" target="blank_">patelka2211</a> / <a href="https://github.com/patelka2211/GitHub-Repo-Downloader" title="patelka2211/GitHub-Repo-Downloader on GitHub" style="text-decoration: none;color: #58a6ff;" target="blank_">GitHub-Repo-Downloader</a>
            </a>
        </code>
        </div>
    </div>
</div>

# Input
Run [DOWNLOAD_REQUIRED_MODULES.py](./DOWNLOAD_REQUIRED_MODULES.py "DOWNLOAD_REQUIRED_MODULES.py") file to download required modules.

```shell
py DOWNLOAD_REQUIRED_MODULES.py
```

# Output

![](./output/1.jpg "Output 1")
### Running [GitRep.py](./GitRep.py)

![](./output/2.jpg "Output 2")
### You can see github_linguist folder has been created and [github/linguist](https://github.com/github/linguist "GitHub/Linguist") repository has been downloaded to local storage. And linguist.zip file is there because as specified not to delete inside [GitRep.py](./GitRep.py "GitRep.py") file.


```shell
py GitRep.py
```



```python
# Example
# Owner/repo
# github/linguist

repo_downloader = GitReD('github', 'linguist')

repo_downloader.download(dest='github_linguist', keep_zip_saved=True)
```

- NOTE: You may not be able to find the `github_linguist/` folder on this repository. Because I've included that folder into [.gitignore](.gitignore ".gitignore") file.

### Folder structure
```
root (If specified to make directory.)
| - specified_directory
    | - repo.zip (If specified to keep the zip file saved.)
    | - repository_file1.ext
    | - repository_file2.ext
    | - repository_file3.ext
    •
    •
    •
    | - repository_fileN.ext
```
---
```
root (If not specified to make directory.)
| - repo.zip (If specified to keep the zip file saved.)
| - repository_file1.ext
| - repository_file2.ext
| - repository_file3.ext
•
•
•
| - repository_fileN.ext
```


# Download using shell script

```sh
# For example
owner="patelka2211" # The owner name of repo which you want to download.
repo="GitHub-Repo-Downloader" # The repo name.
save_in_folder="True" # If True then repo will be saved in a new folder in cwd, else repo will directly saved in cwd.
save_zip="True" # If True then .zip file of the repo will be saved in cwd, else .zip file of repo will not be saved.

curl "https://raw.githubusercontent.com/patelka2211/GitHub-Repo-Downloader/main/GitReD.py" > "GitReD_temp_installer.py"

py "GitReD_temp_installer.py" $owner $repo $save_in_folder $save_zip &

wait $!

rm "GitReD_temp_installer.py"
```

# About languages

|Total used languages|Top language|
|:--:|:--:|
|![GitHub language count](https://img.shields.io/github/languages/count/patelka2211/GitHub-Repo-Downloader)|![GitHub top language](https://img.shields.io/github/languages/top/patelka2211/GitHub-Repo-Downloader)|


# License

[![GitHub](https://img.shields.io/github/license/patelka2211/GitHub-Repo-Downloader?color=%2359c7fa)](./LICENSE)

<div style="display: flex; flex-direction: column; align-items: center;">
<div style="display: flex; align-items: center;">
&copy; 2022
<a href="https://github.com/patelka2211" title="Kartavya Patel" style="margin-left: 5px;">Kartavya Patel</a>
</div>
<a href="https://github.com/patelka2211" title="Kartavya Patel"><img src="https://avatars.githubusercontent.com/u/82671701?v=4" width="60px"/></a>
</div>