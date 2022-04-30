owner="patelka2211"
repo="GitHub-Repo-Downloader"
save_in_folder="True" # If True then repo will be saved in new folder in cwd, else repo will directly saved in cwd.
save_zip="True" # If True then .zip file of repo will be saved in cwd, else .zip file of repo will be deleted.

curl "https://raw.githubusercontent.com/patelka2211/GitHub-Repo-Downloader/main/GitReD.py" > "GitReD_temp_installer.py"

py "GitReD_temp_installer.py" $owner $repo $save_in_folder $save_zip &

wait $!

rm "GitReD_temp_installer.py"