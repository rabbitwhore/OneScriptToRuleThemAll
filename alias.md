## Alias

This is for creating a Alias for the python script

### For windows

Follow the instructions below to create a alias for **Danztool**
1. Open PowerShell.
2. Test if you have an profile **`Test-Path $PROFILE`**
3. This will create a new profile if you don't have one: **`New-Item -Type File -Path $PROFILE -Force`**
4. Open your profile with **`notepad $PROFILE`**
5. Add this **`function myscript { & python C:\Scripts\myscript.py $args }`** inside notepad
6. Restart your profile by running **`. $PROFILE`**

    if  **`. $PROFILE`**  runs to an error:
    - **`Get-ExecutionPolicy`**
    - **`Set-ExecutionPolicy RemoteSigned`**
    - **`. $PROFILE`**

7. to test your script run **`myscript`**

### For Mac OS

1. Navigate to your home directory
2. Type nano .bash_profile or .zprofile and press Enter to open the .bash_profile/.zprofile file in the nano text editor.
3. Type alias your_alias_name='python /path/to/your/python/script.py' where your_alias_name is the name you want to give your alias and /path/to/your/python/script.py is the full path to your Python script.
4. Save exit nano by press Ctrl + X, when it ask to save press y
5. Type source ~/.bash_profile or .zprofile and press Enter to apply the changes you made to the .bash_profile/.zprofile file.


#### Danzpunkten
[README](README.md)