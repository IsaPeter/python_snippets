# python_snippets
Various Python Based Little Scripts


## Tools

### dirlister

Try to find Directory listing in a given URL's. It probe all subdirectories located in the URL.

```bash
$ cat /tmp/input_urls.txt | ./dirlister --stdin

[+] Directory Listing! URL: https://docs.oasis-open.org/asap/0.9
[+] Directory Listing! URL: https://docs.oasis-open.org/asap
[+] Directory Listing! URL: https://docs.oasis-open.org
```

### groupper

Reading lines from stdin and grouping the output. Useful for payload generation and mass probe, when you want to include more than 1 payload in a request.

```bash
python3 -c "for i in range(100): print(i)" | ./groupper -c 50 -j ' '
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49

51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99
```


### uniqdomains

Read input from STDIN and print unique domains from the input URL list.

```bash
┌──(kali㉿kali)-[/tmp/python_snippets]
└─$ cat /tmp/a/urls.txt | wc -l        
258864
                                                                                                                                                                                                                                            
┌──(kali㉿kali)-[/tmp/python_snippets]
└─$ cat /tmp/a/urls.txt | elf/uniqdomains 
www.pcx.hu
3.pcx.hu
2.pcx.hu
pcx.hu
1.pcx.hu
static1.pcx.hu
admin.pcx.hu
www2.pcx.hu
static0.pcx.hu
new.pcx.hu
mail.pcx.hu
old.pcx.hu
weboldalonwww.pcx.hu
mattermost.pcx.hu
```
