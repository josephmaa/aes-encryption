https://github.com/josephmaa/aes-encryption

Installation:

After creating a conda env with `conda env create -n demo`, run `conda install pip`, then `pip3 install -r requirements.txt` to setup your virtual environment.

To run the server, start the terminal with the following command:

python3 server.py <PORT> <KEY>
python3 python3 client.py <SERVER_IP> <PORT> <KEY>

> > > (demo) ~/demo/secure_server % python3 server.py 1234 abcdefghnbfghasd 1:33:35
> > > Waiting for clients to connect...

Then in another terminal run

> > > (demo) ~/demo/secure_server % python3 client.py 127.0.0.1 1234 abcdefghnbfghasz 1:33:22
> > > Please enter a message to send to the server: testing

Since the keys match, we see on the server update side:

> > > (demo) ~/demo/secure_server % python3 server.py 1234 abcdefghnbfghasd 1:35:13
> > > Waiting for clients to connect...
> > > Client connected from: ('127.0.0.1', 63981)
> > > Client sent testing
> > > Waiting for clients to connect...

If you were to use a key mismatch, you should see a mismatch in padding:

> > > (demo) ~/demo/secure_server % python3 server.py 1234 abcdefghnbfghasd 1:35:52
> > > Waiting for clients to connect...

> > > (demo) ~/demo/secure_server % python3 client.py 127.0.0.1 1234 abcdefghnbfghasz 1:35:25
> > > Please enter a message to send to the server: testing

> > > (demo) ~/demo/secure_server % python3 server.py 1234 abcdefghnbfghasd 1:35:52
> > > Waiting for clients to connect...
> > > Client connected from: ('127.0.0.1', 64030)
> > > Traceback (most recent call last):
> > > File "/Users/josephgmaa/demo/secure_server/server.py", line 48, in <module>

    plaintext = unpad(plaintext, AES.block_size).decode("utf-8")

File "/Users/josephgmaa/miniconda3/envs/demo/lib/python3.10/site-packages/Cryptodome/Util/Padding.py", line 92, in unpad
raise ValueError("Padding is incorrect.")
ValueError: Padding is incorrect.
