*** SikuliX-IDE-1.0Win32BetaNNN ***
*** SikuliX-IDE-1.0Win64BetaNNN ***
-----------------------------------

Be aware: 
- still work in progress - might contain bugs
- not everything is tested
- not everything is implemented / documented

*** Installation
unzip to any location you like

*** Currently ONLY usage from command line is possible (no SikuliX.exe yet)
But you might use any Windows approach or tool, to put something on the desktop, that can be double clicked to start the IDE

*** Using the contained command scripts
- use either sikuli-ide.cmd (starts the IDE) or sikli-script.cmd (interactive or run scripts) this way:
sikuli-ide.cmd  (cannot be used to run scripts from commandline): -h (help for more options)
sikuli-script.cmd (supported options: -h (help for more options), -i (interactive), -r (run a script))

*** Java-Version:
- the stuff is compiled with Java 6 latest version
- it runs on Java 7 too
- Java 7 is used if present
- having Java 6 and 7 on your machine, use option 
  -j6 to force running with your Java 6 
with the above mentioned command scripts
- only works, if Java is installed in the standard places in %ProgramFiles% or %ProgramFiles(x86)%

*** Using sikuli-script.jar in Java programming with IDE's like Netbeans, Eclipse, ...
    or Java based scripting (like Jython, JRuby, Scala, Groovy, Clojure, ...)

look: https://github.com/RaiMan/SikuliX-API/wiki/Usage-in-Java-programming  
