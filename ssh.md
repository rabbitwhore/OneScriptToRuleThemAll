## SSH

In order to this script to work properly you need to have enabled SSH key authentication

### Enable SSH key authentication

#### Local configuration 

1. On your local machine, run the following command: **`ssh-keygen -t rsa -f /path/to/your/key`**
2. Inside your **.ssh** folder you will find your key. 
3. on windows you might need to create a config file inside your **.ssh** folder, it should look like this:

        config file --
        Host example.se
            Hostname example.se
            User username
            IdentityFile C:\Users\ssh\example_se

#### Server configuration

1. Copy your Local **rsa.pub** file to **/home/user/.ssh/authorized_keys** 
2. Disable **`PermitRootLogin`** inside your /etc/ssh/sshd_config file.
3. If you only have one root user you need to create a new user with root privileges, <br> follow the instructions under the following otherwise you can skip this step.

    - **`adduser newuser`**
    - **`usermod -aG sudo newuser`**
    - **`su - newuser`**
    - Once you are logged in as the new user. You can test if the user has <br>sudo privileges by typing the command **`sudo ls -la /root`**

4. Restart the SSH server using the command **`sudo systemctl restart sshd`**
5. Enable **`PubKeyAuthentication`** inside **/etc/ssh/sshd_config**
6. Enable **`Authorizedkeysfile`** inside **/etc/ssh/sshd_config**
7. Restart the SSH server using the command **`sudo systemctl restart sshd`**

#### Finish Local and Server configuration

To try everything, follow the instructions below:
- **`ssh username@example.se`**, if this works your fine
- if the above command fails you can try this **`ssh -i path/to/local/rsa/file username@example.se`**


#### OneScriptToRuleThemAll
[README](README.md)