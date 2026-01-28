# Linux Commands 🔧🐧


---

> ## How this cheat-sheet is organised
> - Commands grouped by purpose (navigation, files, viewing, search, permissions, processes, networking, compression).

---

# Navigation
> ### 1. `cd` — change directory  

**Extra:**  
- `cd` alone → goes to your home directory.  
- `cd -` → go to previous directory.  
- `cd ..` → go up one level.  
- Example:  
```bash
cd /var/log
```

>### 2. `pwd` — present working directory    
**Extra:**  
- Use `pwd` to confirm current absolute path.  
- Example:  
```bash
pwd
# /home/suyashk13/projects
```

---

# Files & Directories (create / copy / move / delete)
>### 3. `rm` : remove a file(delete):  

**Extra:**  
- `rm filename` deletes without moving to trash — be careful.  
- `rm -i filename` prompts before removing.

>### 4. `rm -r` : to delete a folder (as there are file inside a folder so -r means recursively delete the files)  
 
**Extra:**  
- Add `-f` to force: `rm -rf foldername` (dangerous).  
- Safer: list contents before removing: `ls foldername`.

>### 6. `mkdir -p` : -p gives no error if folder already exits and can create folder inside folder eg website/static/{css, js}  
**Extra:**  
- Example:  
```bash
mkdir -p website/static/{css,js,images}
```

>### 7. `touch` : creates files eg touch views.py forms.py    
**Extra:**  
- `touch` also updates the file timestamp if it exists.  
- Example: `touch README.md`

>### 8. `cp` : copy files cp filename new_filename for folders *cp -r foldername new_folder*  

**Extra:**  
- `cp -v` shows verbose output.  
- To copy and preserve attributes: `cp -a src/ dest/`

>### 9. linux does not have rename option so **mv** done it the same folder itself renames a file or folder *mv foldername new_folder* **mv filename new_file**   
**Extra:**  
- `mv` also moves files between directories: `mv file /path/to/destination/`  
- `mv -i` prompts before overwrite.

---

# Viewing file contents
>### 10. `cat` : shows content inside of a file  

**Extra:**  
- Good for small files. For long files prefer `less`.  
- Example: `cat /etc/hostname`

### 11. To see contents of a file there are many linux commands such as  
  
>     less filename -- file may be of many pages less gives first page  

>     head -n 10 filename : shows first 10 lines of the file (number can change)  

>     tail -n 10 filename : shows last 10 lines**  
**Extra:**  
- `less` allows scrolling (`j`, `k`, `/search`, `q` to quit).  
- `tail -f logfile` follows new appended lines (great for watching logs live).  
- Examples:  
```bash
head -n 20 /var/log/syslog
tail -n 50 /var/log/nginx/access.log
less /usr/share/distro/release_notes.txt
```

---

# Searching
>### 12. `grep` : to search a word eg: grep "hello" notes.txt  
**Extra:**  
- `grep -i` → case-insensitive.  
- `grep -R "pattern" .` → recursive search in current dir.  
- Combine with `--color=auto` to highlight matches: `grep --color=auto -n "TODO" -R .`

>### 13. `find` :  to find a file in a directory: **find . -name "forms.py"**  

**Extra:**  
- Search by type: `find . -type f -name "*.py"` (files) or `-type d` (directories).  
- Run a command on found files: `find . -name '*.log' -exec rm {} \;` (use carefully).

---

# Permissions
>### 14. To change the read, write, execute permission use **chmod** eg: chmod +x script.sh to give excute permission for the file   

**Extra:**  
- Symbolic: `chmod u+x script.sh` adds execute for owner.  
- Numeric mode: `chmod 755 file` (owner rwx, group rx, others rx).  
- Check with `ls -l filename`.

---

# Processes
### 15. To view processes : ps  
>     ps aux -- shows all the processes  
>     with ps aux we use pipe( | ) and grep to search for specific process eg: ps aux | grep "zsh" or "code"**  
**Extra:**  
- `top` or `htop` (if installed) show interactive process viewer.  
- `ps -ef` is another common format.  
- Example: `ps aux | grep nginx`

### 16. to kill a process : kill process_id  

**Extra:**  
- `kill PID` sends SIGTERM (15) by default.  
- `kill -9 PID` sends SIGKILL (force). Use only when necessary.  
- To find PID: `pgrep -l process_name` or `ps aux | grep name`.

---

# Networking & HTTP
>### 17. `curl -I https://api.freeapi.app/api/v1/public/quotes/quote/random` (-I is to get headers of the API)  
 
**Extra:**  
- `curl -v` for verbose.  
- `curl -s` for silent (useful in scripts).  
- `curl -I` shows response headers only.  

>### 18. `curl -o filename` -- to save the response in a file eg. curl -o https://api.freeapi.app/api/v1/public/quotes/quote/random  

**Important correction (extra):** the original example mixes up arguments — the correct form is `curl -o <filename> <URL>`  
**Extra example:**  
```bash
curl -o quote.json "https://api.freeapi.app/api/v1/public/quotes/quote/random"
# or save with remote name:
curl -O https://example.com/file.tar.gz
```

>### 19. `wget`: gets a file from using a link eg wget https://github.com/suyash-sketch/learn-git/archive/refs/heads/main.zip  
**Extra:**  
- `wget -c` to continue an interrupted download.  
- `wget -q` for quiet.  
- `wget -O saved-name.zip <url>` to set output filename.

---

# Compression / Archiving
>### 20. `unzip` - unzips a zip folder  

**Extra:**  
- `unzip file.zip -d destination_dir` to extract to specific directory.  
- For tar archives: `tar -xf file.tar.gz` (extract), `tar -czf archive.tar.gz folder/` (create).

---

# Handy Quick Reference (copyable)

```text
# Navigation
cd /path/to/dir
pwd

# Files & dirs
ls -la
mkdir -p a/b/c
touch file.txt
cp -r src/ dest/
mv oldname newname
rm file
rm -rf dir

# Viewing
cat file
less file
head -n 10 file
tail -n 10 file
tail -f logfile

# Search
grep -R "pattern" .
find . -name "*.py"

# Permissions
chmod +x script.sh
ls -l script.sh

# Processes
ps aux | grep process
top
kill PID

# Networking
curl -I https://example.com
curl -o out.json https://api...
wget -c https://example.com/file.zip

# Compression
unzip file.zip -d outdir
tar -czf out.tar.gz folder/
tar -xzf out.tar.gz
```

---

