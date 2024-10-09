
Embedding File Using Steghide

Let's create a text file containing our secret message that we will conceal within a photo.

    Run touch secret.txt, then run ls to view the output.

    touch-secret.png

    Run nano secret.txt to edit our secret file.

    nano-secret.png

    nanosecret.png

    In our secret file we will add our secret below:
        The password is: Pa$$w0rd
        CTRL+O to write out the file, then press ENTER.
        Type y and press ENTER.
        ENTER again to save file name and exit nano.

    write-secret.png

    Now we will embed secret.txt into our image using the following command
        steghide embed -cf ~/Pictures/Square.jpeg -ef secret.txt
        Enter passphrase: Pass

    steghide-embed.png

        To see the list of options for steghide just type steghide into the terminal and press ENTER to list out the options.

        Steghide options

    Navigate to the directory where our picture is located.
        Type cd Pictures/ and press Enter to exit nano.

    cd-Pictures.png

    This is just a normal image from what we can see. We can view the image using Ristretto Image Viewer. Enter the command: ristretto square.jpeg

    ristretto square.jpeg

    view-image.png

    ristretto-square.png

    Exit ristretto after viewing the image.

    Using the --info option we can see that there is an embedded file in this image.
        Run steghide --info Square.jpeg
        Select y when prompted to enter the password for Square.jpeg
        Type in the password Pass

    steg-info.png

        This tells us that this image has our embedded file secret.txt, encrypted using rijndael-128 (AES) block cipher (cbc), and the embedded file is compressed.

    We can now extract our embed secret from our image with the following command.
        steghide extract -sf Square.jpeg
        Enter passphrase: Pass
        Type ls to see our secret has been extracted from our file.

    Example

    Type ls to list out the files in the Pictures directory.

    steghide-ls.png

    Read out the secret.txt file using 'cat'

    cat secret.txt

    cat-secrettext.png

