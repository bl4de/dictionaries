### Dictionaries

This repository contains custom made dictionariy used to directories/files enumeration when attacking web applications.

### starter.txt

`starter.txt` contains most common entries one can found on any web server. Configuration files, IDE files, dot files, default CMS, CRM, eCommerce engines, backups, "hidden" panels, admin interfaces, SQLs - name it. I add new entries every time I come across something new (by reading blog posts, Bug Bounty or CTF writeups etc., learning new stuff etc.)

This is the one I use as the first dictionary to enumerate resources when I come across working, responsive web server. Based on the results returned by this dictionary I plan next step(s) of enumeration, which in case of discovering working web applications, are:

### lowercase.txt (~100k words) and wordlist.txt (~400k words)

Those two are the best way to enumerate **files** when you identify technology behind web server (PHP, ASP, JSP, JS etc.) by using suffix with extension. They give very good results especially if there are already discovered subfolders in web application (like *include/*, *config/*, *templates/*, *api/*, *controllers/* etc. - you get the drill).



