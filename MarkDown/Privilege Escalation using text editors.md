## Privilege Escalation in a Linux System.

[link to guide](https://medium.com/schkn/linux-privilege-escalation-using-text-editors-and-files-part-1-a8373396708d)

Scenario — 1: Using .sh file for privilege escalation

There was this box which I was trying to hack and get the root access. So basically, I was able to execute the following commands and files as root in the user’s shell.
Privilege escalation using .sh

From the above, you can tell that the user haris is able to execute the file test.sh as root. Which means that if he executes the file using sudo it will be equivalent to the root executing the file. Also, the NOPASSWD specifies that no password will be asked while executing the file.

This is a very insecure way of allowing a user to access a file.

Using above permissions, the user can easily get into root, just by doing some simple modifications in the test.sh and then executing it with sudo. Let’s first see the contents of the file and let’s try executing it.

As you can see it is just printing a welcome message and nothing else.

So how can we use this file in our favour?

Well, the answer is very simple!

Since it is a bash file so commands inside it will get executed, and if we execute the file as root, then all the commands inside it will also get executed as root. So, let’s take advantage of that and append /bin/bash -i to the file. This will execute bash as root, which in turn will open the root shell.

And we got the root!

This is a pretty much simple scenario and is very easy to exploit. These type of mistakes are often done by administrators and are used by other system users and testers to get into the root.
Scenario — 2: Using nano for privilege escalation.

    Note: Root Access to any text editor other than nano can also be used to exploit such situations.

Now let’s take a look at a little more complicated situation.

In this case, the user has access to nano text editor as root but only in a specific directory.
Privilege escalation using nano

The user can only use sudo in /var/opt directory, if the user will try to use it some other place, he will be restricted.

Now if the /var/opt/* part was not mentioned in the /etc/sudoers file, then it would be a pretty much easy deal to exploit it, as you would be able to edit any system file as root. But that’s not the case over here. it will take a little more creative approach to exploit it.

Let me give you a hint: how do you traverse backwards in a directory? For example, if suppose you are in /home/user/xyz/ , then how would you traverse one step backwards to /home/user ?

The answer is simple!

You can simply do cd .. or cd /home/user/xyz/../ .

That is the trick which can be used to exploit it.

So, let’s try to edit the sudoers file and try to add more privileges to the user account. But if you will try to execute the following command:

sudo nano /etc/sudoers

Then it will get restricted and you will get a permission denied message. But as we know, we can execute nano as root in /var/opt . So you can use it to traverse backwards and reach onto the sudoers file as shown below:

sudo nano /var/opt/../../etc/sudoers

Yes, that’s the trick ;)

Now the moment you execute it, it will open the sudoers file inside the nano text editor as root. Now modify the file and give the user haris the root privileges by modifying the file as mentioned below:

Replace the marked line with haris ALL=(ALL) NOPASSWD:ALL , save the file and run sudo -i . This will give you the root shell.
Scenario — 3: Using Vim for privilege escalation.

We are going to create a similar scenario as the previous one. But in this case, we have access to the Vim editor instead of nano and no directory restrictions are specified.
Privilege escalation using Vim editor

Now you must be thinking, we can repeat the same steps we did in scenario 2 to get into the root and in this case, there is no directory restriction too so it will be a straightforward approach, which is correct but there exists a simpler and easy way to do it when you have access to Vim.

Vim is a very versatile text editor which have many awesome functionalities including the ability to open a shell inside it. Yes, you read it right this is what we just needed. So, to open vim as root we can use the following command.

sudo vi test.sh

As soon as you will execute it, vi window will open, now you need to switch into the command mode you can do that by pressing ESC key. In command mode, use :!bash command this will open a root shell.

There is one more shortcut which you can use when you have access to vim, you can use the following command to trigger the root shell using vim.

sudo vi -c '!bash'

There are many Linux executable other than text editors which you can use for privilege escalation. I will try to include them and many more other techniques in the next part.

If you guys have any other ideas which I should mention then please comment them down below.