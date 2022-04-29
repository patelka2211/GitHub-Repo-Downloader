# First argv is owner name
# For exmaple github

# Second argv is repo name
# For exmaple linguist

# Third argv is to save inside folder or not
# If yes then True otherwise False

# Fourth argv is to keep .zip file of repo or not
# If yes then True otherwise False

curl "https://raw.githubusercontent.com/patelka2211/GitHub-Repo-Downloader/main/GitReD.py" >> "GitReD_temp_installer.py"

py "GitReD_temp_installer.py" "github" "linguist" "False" "False"

rm "GitReD_temp_installer.py"
