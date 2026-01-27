1. cd = change directory  
2. pwd = present working directory  
3. rm : remove a file(delete):  
4. rm -r : to delete a folder (as there are file inside a folder so -r means recursively delete the files)  
5. man = manual (to read more info about a command) eg. man ls
6. mkdir -p : -p gives no error if folder already exits and can create folder inside folder eg website/static/{css, js}
7. touch : creates files eg touch views.py forms.py
8. cp: copy files cp filename new_filename for folders *cp -r foldername new_folder*
9. linux does not have rename option so **mv** done it the same folder itself renames a file or folder *mv foldername new_folder* **mv filename new_file**
10. cat : shows content inside of a file
11. To see contents of a file there are many linux commands such as  
    less filename -- file may be of many pages less gives first page  
    head -n 10 filename : shows first 10 lines of the file (number can change)  
    tail -n 10 filename : shows last 10 lines
12. grep : to search a word eg grep "hello" notes.txt
13. find :  to find a file in a directory: **find . -name "forms.py"**
14. To change the read, write, execute permission use **chmod** eg: chmod +x script.sh to give excute permission for the file   
15. To view processes : ps  
    ps aux -- shows all the processes  
    with ps aux we use pipe( | ) and grep to search for specific process eg ps aux | grep "zsh" or "code"
16. to kill a process : kill process_id
17. curl -I https://api.freeapi.app/api/v1/public/quotes/quote/random (-I is to get headers of the API) 
18. curl -o filename -- to save the response in a file eg. curl -o https://api.freeapi.app/api/v1/public/quotes/quote/random
19. wget: gets a file from using a link eg wget https://github.com/suyash-sketch/learn-git/archive/refs/heads/main.zip
20. unzip - unzips a zip folder