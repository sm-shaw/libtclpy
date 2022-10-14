import tclpy
import builtins as __builtin__

def init_hammerdbpy():
    init_tcl = (r'''
set UserDefaultDir [ file join [ file dirname [ info script ] ] ]
::tcl::tm::path add "$UserDefaultDir/modules"

append modulelist { Thread msgcat xml comm task reformat_tcl }
for { set modcount 0 } { $modcount < [llength $modulelist] } { incr modcount } {
    set m [lindex $modulelist $modcount]
		set loadtext $m
	if [catch { package require $m }] {
                puts stderr "While loading module\
                        \"$m\"...\n$errorInfo"
                exit 1
        }
    }
    
append loadlist { genvu.tcl gentpcc.tcl gentpch.tcl gengen.tcl genxml.tcl genmodes.tcl gentccmn.tcl gentccli.tcl geninitcli.tcl gencli.tcl genhelp.tcl genstep.tcl }
for { set loadcount 0 } { $loadcount < [llength $loadlist] } { incr loadcount } {
    set f [lindex $loadlist $loadcount]
		set loadtext $f
	if [catch {source [ file join $UserDefaultDir src generic $f ]}] {
                puts stderr "While loading component file\
                        \"$f\"...\n$errorInfo"
                exit 1
        }
    }

for { set dbsrccount 0 } { $dbsrccount < [llength $dbsrclist] } { incr dbsrccount } {
    set f [lindex $dbsrclist $dbsrccount]
		set loadtext $f
	if [catch {source [ file join $UserDefaultDir src $f ]}] {
                puts stderr "Error loading database source files/$f"
        }
    }

rename putscli _putscli
proc putscli { output } {
puts "$output\r"
	}
''')

    tclpy.eval(init_tcl)

def eval_hammerdb_command(command_name,*args):
    to_hdb = command_name
    for arg in args:
            if type(arg) != str:
                to_hdb = ' '.join((to_hdb, str(arg)))
            else:
                to_hdb = ' '.join((to_hdb, arg))

    tclpy.eval(to_hdb)
    tclpy.eval('flush stdout')
    if runscript_printline == 0:
        __builtin__.print('\r')

def runscript(output):
    global runscript_printline
    runscript_printline = output

def tclversion():
    a = tclpy.eval('list [info patchlevel]')
    __builtin__.print('Python interface to Tcl version ' + a)

def buildschema(*args):
    eval_hammerdb_command('buildschema',*args)

def deleteschema(*args):
    eval_hammerdb_command('deleteschema',*args)

def clearscript(*args):
    eval_hammerdb_command('clearscript',*args)

def customscript(*args):
    eval_hammerdb_command('customscript',*args)

def datagenrun(*args):
    eval_hammerdb_command('datagenrun',*args)

def dbset(*args):
    eval_hammerdb_command('dbset',*args)

def dgset(*args):
    eval_hammerdb_command('dgset',*args)

def diset(*args):
    eval_hammerdb_command('diset',*args)

def distributescript(*args):
    eval_hammerdb_command('distributescript',*args)

def librarycheck(*args):
    eval_hammerdb_command('librarycheck',*args)

def loadscript(*args):
    eval_hammerdb_command('loadscript',*args)

def print(*args, **kwargs):
    command_list = ['db', 'bm', 'dict', 'script', 'vuconf', 'vucreated', 'vustatus', 'datagen', 'tcconf']
    flag = 0
    for j in command_list:
            if args[0]==j:
                flag=1
                break
    if flag==1:
        eval_hammerdb_command('print',*args)
    else:
        return __builtin__.print(*args, **kwargs)

def quit(*args):
    eval_hammerdb_command('quit',*args)

def runtimer(*args):
    eval_hammerdb_command('runtimer',*args)

def steprun(*args):
    eval_hammerdb_command('steprun',*args)

def switchmode(*args):
    eval_hammerdb_command('switchmode',*args)

def tcset(*args):
    eval_hammerdb_command('tcset',*args)

def tcstart(*args):
    eval_hammerdb_command('tcstart',*args)

def tcstatus(*args):
    eval_hammerdb_command('tcstatus',*args)

def tcstop(*args):
    eval_hammerdb_command('tcstop',*args)

def vucomplete(*args):
    eval_hammerdb_command('vucomplete',*args)

def vucreate(*args):
    eval_hammerdb_command('vucreate',*args)

def vudestroy(*args):
    eval_hammerdb_command('vudestroy',*args)

def vurun(*args):
    eval_hammerdb_command('vurun',*args)

def vuset(*args):
    eval_hammerdb_command('vuset',*args)

def vustatus(*args):
    eval_hammerdb_command('vustatus',*args)

def waittocomplete(*args):
    eval_hammerdb_command('waittocomplete',*args)

def source(filename):
    runscript(1)
    from pathlib import Path

    path = Path(filename)

    if path.is_file():
        exec(open(filename).read())
    else:
        print(f'The file {filename} does not exist')

    runscript(0)

def help(*args):
     eval_hammerdb_command('help',*args)

init_hammerdbpy()
