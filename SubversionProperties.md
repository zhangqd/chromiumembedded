**This Wiki page is obsolete and no longer maintained. Visit the new CEF project page at https://bitbucket.org/chromiumembedded/cef/**

## Subversion properties ##

For CEF development, you should configure your Subversion config file to automatically set properties on new files as shown below. We do not use svn:eol-style=native because it makes it painful to move diff files across different platforms.

```
# CEF-specific config file to put at ~/.subversion/config or %USERPROFILE%\AppData\Roaming\Subversion\config
# Originally copied from http://src.chromium.org/viewvc/chrome/trunk/tools/buildbot/slave/config?revision=46073

[miscellany]
global-ignores = *.pyc *.user *.suo *.bak *~ #*# *.ncb *.o *.lo *.la .*~ .#* .DS_Store .*.swp *.scons *.mk *.Makefile *.sln *.vcproj *.rules SConstruct *.xcodeproj
enable-auto-props = yes

[auto-props]
*.c = svn:eol-style=LF
*.h = svn:eol-style=LF
*.cc = svn:eol-style=LF
*.cpp = svn:eol-style=LF
*.def = svn:eol-style=LF
*.obsolete = svn:eol-style=LF
*.m = svn:eol-style=LF
*.mm = svn:eol-style=LF
*.idl = svn:eol-style=LF
*.html = svn:eol-style=LF
*.htm = svn:eol-style=LF
*.xml = svn:eol-style=LF
*.js = svn:eol-style=LF
*.css = svn:eol-style=LF
*.mock-http-headers = svn:eol-style=LF
*.afm = svn:eol-style=LF
*.txt = svn:eol-style=LF
*.gyp = svn:eol-style=LF
*.gypi = svn:eol-style=LF
*.grd = svn:eol-style=LF
*.xtb = svn:eol-style=LF
*.py = svn:eol-style=LF
*.pl = svn:eol-style=LF
*.pm = svn:eol-style=LF
*.sh = svn:eol-style=LF;svn:executable
*.make = svn:eol-style=LF
Makefile = svn:eol-style=LF
*.bat = svn:eol-style=CRLF
*.rc = svn:eol-style=CRLF
*.txt = svn:eol-style=LF
*.patch = svn:eol-style=LF
*.png = svn:mime-type=image/png
*.jpg = svn:mime-type=image/jpeg
*.pdf = svn:mime-type=application/pdf
```