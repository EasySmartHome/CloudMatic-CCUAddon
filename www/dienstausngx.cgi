#!/bin/tclsh

package require HomeMatic

global env
set private 0

foreach key [array names env] {
  if {$key == "REMOTE_ADDR"} {
  	set octets [split $env($key) "."]
    if {($private == 0 && [lindex $octets 0] == "172") && ([lindex $octets 1] == "16" || [lindex $octets 1] == "17" || [lindex $octets 1] == "18" || [lindex $octets 1] == "19" || [lindex $octets 1] == "20" || [lindex $octets 1] == "21" || [lindex $octets 1] == "22" || [lindex $octets 1] == "23" || [lindex $octets 1] == "24" || [lindex $octets 1] == "25" || [lindex $octets 1] == "26" || [lindex $octets 1] == "27" || [lindex $octets 1] == "28" || [lindex $octets 1] == "29" || [lindex $octets 1] == "30" || [lindex $octets 1] == "31")} { set private 1 }
    if {$private == 0 && [lindex $octets 0] == "192" && [lindex $octets 1] == "168"} { set private 1 }
    if {$private == 0 && [lindex $octets 0] == "10"} { set private 1 } 
    if {$private == 0 && [lindex $octets 0] == "127"} { set private 1 }
  }
}

if {$private == 0} { exit }

set dienstngx unknown
set content [::HomeMatic::Util::LoadFile "/etc/config/addons/mh/dienstngx"]
catch { [regexp -line {(.*)} $content dummy dienstngx] }

if {$dienstngx == 1} {
	if {[catch {exec /bin/sh /etc/config/addons/mh/dienstausngx.sh } result]} {
		# non-zero exit status, get it:
		set status [lindex $errorCode 2]
	} else {
		# exit status was 0
		# result contains the result of your command
		set status 0
	}
	if {[catch {exec /bin/sh /etc/config/addons/mh/loophammer.sh } result]} {
		# non-zero exit status, get it:
		set status [lindex $errorCode 2]
	} else {
		# exit status was 0
		# result contains the result of your command
		set status 0
	}
	puts "Der Reverse Proxy Dienst wurde beendet."
}
if {$dienstngx == 0} {
  puts "Der Reverse Proxy Dienst ist bereits deaktiviert."
}