# Convert Image files to ascii text

```sh
git clone https://github.com/EvoltPratom/img2ascii.git
```

<code>wget -o i2a.zip https://github.com/EvoltPratom/img2ascii/archive/master.zip</code>


Extract the files

<code>Expand-Archive i2a.zip -DestinationPath i2a</code>


<code>
python i2a.py file1.jpg file2.png file3.jpeg
</code>

As a library

```sh
>>> from i2a import img2ascii
>>> img2ascii('t2.jpg')
Saving t2.jpg to t2.txt
>>>

```
