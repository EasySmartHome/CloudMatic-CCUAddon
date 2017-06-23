#!/bin/tclsh

package require HomeMatic

set ID          mh
set URL         /addons/mh/index.cgi
set NAME        CloudMatic

array set DESCRIPTION {
  de {<li>Sicherer VPN Fernzugriff</li><li>SMS Versand</li><li>Versand von PUSH Nachrichten</li><li>Mail Versand per Skript</li>} 
  en {<li>Secure VPN remote access</li><li>Send SMS Messages</li><li>Send push notifications</li><li>Send dynamic eMails</li>}
}

::HomeMatic::Addon::AddConfigPage $ID $URL $NAME [array get DESCRIPTION]
