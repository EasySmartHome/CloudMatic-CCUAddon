#!/bin/tclsh

package require HomeMatic

set serial unknown
catch { set serial [::HomeMatic::GetSerialNumber] }

set bidcos unknown
set content [::HomeMatic::Util::LoadFile "/etc/config/addons/mh/ids"]
catch { [regexp -line {BidCoS-Address=(.*)} $content dummy bidcos] }

set user_has_account unknown
set base_url "meine-homematic.de"
set content [::HomeMatic::Util::LoadFile "/etc/config/addons/mh/mhcfg"]
catch { [regexp -line {user_has_account=(.*)} $content dummy user_has_account] }
catch { [regexp -line {base_url=(.*)} $content dummy base_url] }

set register_pending unknown
set content [::HomeMatic::Util::LoadFile "/etc/config/addons/mh/register_pending"]
catch { [regexp -line {status=(.*)} $content dummy register_pending] }

puts "Content-Type: text/html; charset=utf-8"

puts {
<!DOCTYPE html>
<html>
  <head>
    <link type="text/css" rel="stylesheet" href="css/materialize.min.css"  media="screen,projection">
    <link type="text/css" rel="stylesheet" href="css/cloudmatic.css"  media="screen,projection">
    <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <title>CloudMatic (v2023310501)</title>
  </head>
<body>
<script>
  var heute = new Date();
  var jahr = heute.getYear()+1900;
  var monat = heute.getMonth()+1;
  var tag = heute.getDate();
}
  puts "var base_url = '$base_url';"
  puts "</script>"

if {$user_has_account == 0} {
  if {$register_pending == 1} {
puts {
<div class="navbar-fixed">
  <nav class="white" role="navigation">
    <div class="nav-wrapper container">
      <a id="logo-container" href="/addons/mh/index.cgi" class="brand-logo grey-text text-darken-2"><img src="img/CloudMaticLogo.png" alt="CloudMatic"></a>
      <ul class="right hide-on-med-and-down" style="padding-top:6px;">
        <li class="active"><a href="index.cgi" class="cm-nav" data-content="start">Start</a></li>
        <li><a href="#!" class="cm-nav" data-content="support">Support</a></li>
      </ul>
      <ul id="nav-mobile" class="side-nav">
        <li class="active"><a href="index.cgi" class="cm-nav" data-content="start">Start</a></li>
        <li><a href="#!" class="cm-nav" data-content="support">Support</a></li>
      </ul>
      <a href="#" data-activates="nav-mobile" class="button-collapse"><i class="material-icons">menu</i></a>
    </div>
  </nav>
</div>
<!-- /Navigation -->
<main>
<div class="container">
<div id="start" class="cm-content">
  <div class="row">
    <div class="col s12">
      <h4>CloudMatic | Steuern Sie Ihr Haus doch einfach EASY.</h4>
      Sicherer Fernzugriff auf Ihre SmartHome Zentrale
    </div>
  </div>
  <div class="row">
    <div class="col s12">
      <h6>Sie haben sich bereits registriert, bitte haben Sie ein paar Minuten Geduld.</h6>
      <p>
        Ihr CloudMatic Konto wird aktiviert und der Schl&uuml;ssel automatisch auf die Zentrale &uuml;bertragen. Nach erfolgreicher
        Aktivierung und &Uuml;bertragung haben Sie hier einen zentralen &Uuml;berblick auf Ihre pers&ouml;nlichen Daten und Zug&auml;nge.
        <br><br>
        <b>Hinweis</b>: sollte diese Meldung auch nach ca. 15 Minuten noch erscheinen konnte Ihr pers&ouml;nlicher Schl&uuml;ssel nicht 
        automatisch auf die Zentrale &uuml;bertragen werden. Bitte installieren Sie in diesm Fall den Schl&uuml;ssel manuell. Eine genaue
        Anleitung zur manuellen Installation finden Sie hier: 
        <a href="http://go.cloudmatic.de/install-key" target="_blank">http://go.cloudmatic.de/install-key</a>.
        <br><br>
      </p>
      <a href="index.cgi" class="waves-effect waves-light btn blue"><i class="material-icons left">loop</i>Seite neu laden</a>
    </div>
  </div>
</div>
}
  } else {
  
puts {
<!-- Navigation -->
<div class="navbar-fixed">
  <nav class="white" role="navigation">
    <div class="nav-wrapper container">
      <a id="logo-container" href="/addons/mh/index.cgi" class="brand-logo grey-text text-darken-2"><img src="img/CloudMaticLogo.png" alt="CloudMatic"></a>
      <ul class="right hide-on-med-and-down" style="padding-top:6px;">
        <li class="active"><a href="index.cgi" class="cm-nav" data-content="start">Start</a></li>
        <li><a href="clregister.cgi" data-content="register">Registrieren</a></li>
        <li><a href="#!" class="cm-nav" data-content="support">Support</a></li>
      </ul>
      <ul id="nav-mobile" class="side-nav">
        <li class="active"><a href="index.cgi" class="cm-nav" data-content="start">Start</a></li>
        <li><a href="clregister.cgi" data-content="register">Registrieren</a></li>
        <li><a href="#!" class="cm-nav" data-content="support">Support</a></li>
      </ul>
      <a href="#" data-activates="nav-mobile" class="button-collapse"><i class="material-icons">menu</i></a>
    </div>
  </nav>
</div>
<!-- /Navigation -->
<main>
<div class="container">
<div id="start" class="cm-content">
  <div class="row">
    <div class="col s12">
      <h4>CloudMatic | Steuern Sie Ihr Haus doch einfach EASY.</h4>
      Sicherer Fernzugriff auf Ihre SmartHome Zentrale
    </div>
  </div>
  <div class="row">
    <div class="col s12">
      Sie haben noch kein CloudMatic Konto aktiviert. Testen Sie alle CloudMatic Dienste 30 Tage lang ganz unverbindlich und kostenlos!<br><br>
      <a href="clregister.cgi" class="waves-effect waves-light btn blue"><i class="material-icons left">mode_edit</i>Jetzt Testen</a> 
    </div>
  </div>
  <div class="divider"></div>
  <div class="row">
    <div class="col s12">
      <div class="row">
        <div class="col s4">
          <img src="img/cmvpn.png" alt="CloudMatic Connect" class="responsive-img">
        </div>
        <div class="col s8">
          <h4>CloudMatic Connect - sicherer Fernzugriff auf Ihre Haussteuerung</h4>
          <p>
            <h6>Weltweiter Zugriff - per APP und Webbrowser</h6>
            Sie m&ouml;chten von &uuml;berall auf Ihre Haussteuerung zugreifen k&ouml;nnen? Sicher und komfortabel? Nutzen Sie CloudMatic Connect!
            &Uuml;ber die sichere Anbindung von CloudMatic Connect greifen Sie &uuml;ber das Internet auf Ihre HomeMatic Haussteuerung zu.
          </p> 
        </div>
        <div class="col s12">
          <h6>So funktioniert es:</h6>
          <ul>
            <li>Sie melden sich von Ihrer HomeMatic Zentrale zu unserem Dienst an</li>
            <li>Sie erhalten einen pers&ouml;nlichen Schl&uuml;ssel, der nur f&uuml;r Sie gilt. Dieser wird auf Ihrer HomeMatic Zentrale eingespielt.</li>
            <li>Ihre Zentrale baut nun einen sicheren Tunnel zu unserem Portal auf. Nat&uuml;rlich AES 256bit verschl&uuml;sselt und &uuml;ber digitale Zertifikate authentisiert - was dem aktuellen Stand der Technik entspricht. F&uuml;r Sie passiert das alles vollkommen transparent im Hintergrund!</li>
            <li>Sie k&ouml;nnen nun &uuml;ber unser Portal auf Ihre CCU zugreifen. Klicken Sie einfach auf den Link im Portal - schon werden Sie auf Ihre Haussteuerung geleitet.</li>
            <li>Sicherheit geht vor: Damit kein Dritter Zugriff auf Ihre Zentrale hat, sichern wir Ihre CCU &uuml;ber unsere Webfirewall. Erst nach Authentisierung mit Benutzername und Passwort ist ein Zugriff auf Ihre Haussteuerung m&ouml;glich.</li>
          </ul>
          <a href="clregister.cgi" class="waves-effect waves-light btn blue"><i class="material-icons left">mode_edit</i>Jetzt testen</a> 
        </div>
      </div>
    </div>
  </div>
  <div class="divider"></div>
  <div class="row">
    <div class="col s12">
      <div class="row">
        <div class="col s4">
          <img src="img/cmcomplete.png" alt="CloudMatic Complete" class="responsive-img">
        </div>
        <div class="col s8">
          <h4>CloudMatic Complete - sicherer Fernzugriff & komfortable Bedienoberfl&auml;che</h4>
          <p>
            <h6>Alles in einem</h6>
            Mit CloudMatic Complete steht Ihnen ein sicherer Fernzugriff und eine komfortable Bedienoberfl&auml;che zur 
            Verf&uuml;gung. Hiermit brauchen Sie Ihre HomeMatic Haussteuerung nicht mehr &uuml;ber die Oberfl&auml;che der Zentrale bedienen, sondern nutzen 
            unsere Cloud-basierte L&ouml;sung - von &uuml;berall und mit jedem Endger&auml;t ... auch per Smartphone/Tablet! 
          </p> 
        </div>
        <div class="col s12">
          <h6>Mit CloudMatic Complete k&ouml;nnen Sie:</h6>
          <ul>
            <li>Ihre HomeMatic Zentrale vom SmartPhone, Tablet oder PC aus bedienen, lokal und per Internet durch einen gesicherten VPN-Tunnel.</li>
            <li>Eine beliebige Zahl individuelle Ansichten erstellen, die eine schnelle Status-&Uuml;bersicht und eine einfache Bedienung erlauben.</li>
            <li>Den Zugriff f&uuml;r unterschiedliche Benutzer einschr&auml;nken.</li>
            <li>Auf weitere Ger&auml;te wie Webcams durch den VPN-Tunnel zugreifen.</li>
            <li>Mehrere Zentralen &uuml;ber eine Oberfl&auml;che verwalten.</li>
          </ul>
          <a href="clregister.cgi" class="waves-effect waves-light btn blue"><i class="material-icons left">mode_edit</i>Jetzt testen</a> 
        </div>
      </div>
    </div>
  </div>
  <div class="divider"></div>
  <div class="row">
    <div class="col s12">
      <div class="row">
        <div class="col s4">
          <img src="img/cmsms.png" alt="CloudMatic NotifyMe" class="responsive-img">
        </div>
        <div class="col s8">
          <h4>CloudMatic NotifyMe - Schnell informiert dank SMS, Pushnachrichten und Mail</h4>
          <p>
            <h6>Versenden Sie SMS direkt von Ihrer HomeMatic Zentrale!</h6>
            SMS k&ouml;nnen ganz einfach per Skript von der Zentrale versendet werden. Der SMS Versand kann als zus&auml;tzliche Aktion bei einem 
            Ereignis hinterlegt werden. Es ist ein nationaler und ein internationaler Versand m&ouml;glich, die Kosten einer SMS liegen unter 
            denen vieler Mobilfunkanbieter.  
          </p> 
        </div>
        <div class="col s12">
          <h6>Push Nachrichten direkt auf Ihr Smartphone*</h6>
          Sie m&ouml;chten zus&auml;tzlich Pushnachrichten auf Ihr Smartphone erhalten? Mit CloudMatic NotifyMe kein Problem.
          Einfach Premium-Guthaben buchen, ggf. die ben&ouml;tigte App auf Ihr Smartphone installieren und ein Script auf Ihrer Zentrale erstellen!
          <br><br>
          <a href="clregister.cgi" class="waves-effect waves-light btn blue"><i class="material-icons left">mode_edit</i>Jetzt testen</a>
          <br><br>
          <sup>* Unterst&uuml;tzte Betriebssysteme: iOS/Android. F&uuml;r den Versand von Pushnachrichten per iPad/iPhone/Android sind Apps von Fremdanbietern Voraussetzung durch die ggf. weitere Kosten entstehen.</sup> 
        </div>
      </div>
    </div>
  </div>
  <div class="divider"></div>
  <div class="row">
    <div class="col s12">
      <div class="row">
        <div class="col s4">
          <img src="img/zufrieden.jpg" alt="CloudMatic NotifyMe" class="responsive-img">
        </div>
        <div class="col s8">
          <h4>Alle Funktionen 30 Tage kostenlos und unverbindlich testen</h4>
          <p>
            Wer kauft schon gerne die Katze im Sack? Sie k&ouml;nnen alle CloudMatic Dienste inkl. VPN Zugang 30 Tage kostenlos und 
            unverbindlich testen. Melden Sie sich jetzt an und &uuml;berzeugen sich von der Qualit&auml;t der Services.  
          </p> 
        </div>
        <div class="col s12">
          <a href="clregister.cgi" class="waves-effect waves-light btn blue"><i class="material-icons left">mode_edit</i>Jetzt testen</a>
        </div>
      </div>
    </div>
  </div>
</div>
}
}
}

if {$user_has_account == 1} {
  if {$register_pending == 1} {
    exec /bin/rm /etc/config/addons/mh/register_pending
  }
	set premiumjahr unknown
	set premiummonat unknown
	set premiumtag unknown
	set userid unknown
	set userkey unknown
  set standardsms 0
  set premiumsms 0
	set smarthomeliz 0
	set smarthometype "Keine Internetverbindung / keine Buchung?"
  set key 0
	set content [::HomeMatic::Util::LoadFile "/etc/config/addons/mh/mhcfg"]
	catch { [regexp -line {premiumjahr=(.*)} $content dummy premiumjahr] }
	catch { [regexp -line {premiummonat=(.*)} $content dummy premiummonat] }
	catch { [regexp -line {premiumtag=(.*)} $content dummy premiumtag] }
	catch { [regexp -line {userid=(.*)} $content dummy userid] }
	catch { [regexp -line {userkennung=(.*)} $content dummy username] }
	catch { [regexp -line {userkey=(.*)} $content dummy userkey] }
	catch { exec /bin/sh /etc/config/addons/mh/csmsg.sh $userid $userkey }  
	set content [::HomeMatic::Util::LoadFile "/etc/config/addons/mh/smsguthaben"]
	catch { [regexp -line {Standard=(.*)} $content dummy standardsms] }
	catch { [regexp -line {Premium=(.*)} $content dummy premiumsms] }
	catch { [regexp -line {Lizenz=(.*)} $content dummy smarthomeliz] }
	catch { [regexp -line {Typ=(.*)} $content dummy smarthometype] }
	catch { [regexp -line {Key=(.*)} $content dummy key] }

  puts {
<!-- Navigation -->
<div class="navbar-fixed">
  <nav class="white" role="navigation">
    <div class="nav-wrapper container">
      <a id="logo-container" href="/addons/mh/index.cgi" class="brand-logo grey-text text-darken-2"><img src="img/CloudMaticLogo.png" alt="CloudMatic"></a>
      <a href="#" data-activates="nav-mobile" class="button-collapse"><i class="material-icons">menu</i></a>
      <ul class="right hide-on-med-and-down" style="padding-top:6px;">
        <li class="active"><a href="#!" class="cm-nav" data-content="status">Status</a></li>
        <li><a href="#!" class="cm-nav" data-content="services">Dienste</a></li>
        <li><a href="#!" class="cm-nav" data-content="check">Funktionspr&uuml;fung</a></li>
        <li><a href="#!" class="cm-nav" data-content="update">Updates</a></li>
        <li><a href="#!" class="cm-nav" data-content="remove">Entfernen</a></li>
        <li><a href="#!" class="cm-nav" data-content="support">Support</a></li>
      </ul>
      <ul id="nav-mobile" class="side-nav">
        <li class="active"><a href="#!" class="cm-nav side-nav-link" data-content="status">Status</a></li>
        <li><a href="#!" class="cm-nav side-nav-link" data-content="services">Dienste</a></li>
        <li><a href="#!" class="cm-nav side-nav-link" data-content="check">Funktionspr&uuml;fung</a></li>
        <li><a href="#!" class="cm-nav side-nav-link" data-content="update">Updates</a></li>
        <li><a href="#!" class="cm-nav side-nav-link" data-content="remove">Entfernen</a></li>
        <li><a href="#!" class="cm-nav side-nav-link" data-content="support">Support</a></li>
      </ul>
    </div>
  </nav>
</div>
<!-- /Navigation -->
<main>
<div class="container">
  }
  puts "<script>"
  puts "var userid = '$userid';"
  puts "var username = '$username';"
  puts "var yyyy = '$premiumjahr';"
  puts "var mm = '$premiummonat';"
  puts "var dd = '$premiumtag';"
  puts "var ssms = '$standardsms';"
  puts "var psms = '$premiumsms';"
  puts "</script>"

	puts {
    <div id="status" class="cm-content" style="display:none;">
      <!-- Headline -->
      <div class="row">
        <div class="col s12">
          <h4>CloudMatic <sup><small>CCU</small></sup> Dashboard</h4>Hier haben Sie einen zentralen &Uuml;berblick auf Ihre pers&ouml;nlichen Daten und Zug&auml;nge.<br>
          <b>Hinweis</b>: es wird nur die Laufzeit der aktuellen Buchung angezeigt! Eventuelle Neubuchungen k&ouml;nnen online im <a href="https://www.cloudmatic.de/member/dashboard" target="_blank">Kundencenter</a> eingesehen werden.
        </div>
      </div>
      <!-- /Headline -->
      <!-- Status Cards -->
      <div class="row">
        <!-- Account Data -->
        <div class="col s12 m6">
          <div class="card white">
            <div class="card-content black-text">
              <span class="card-title">Ihre Daten</span>
              <p>
                Ihre CloudMatic-ID: <script>document.write(userid);</script><br>
                Ihr Benutzername: <script>document.write(username);</script><br>
  }
  if {$smarthometype != "CloudMatic SmartHome"} {
    # cosmetics: add newline, because we need 2 rows vor complete/FullService 
    puts "<br>"
  }
  puts {
              </p>
            </div>
            <div class="card-action">
              <script>document.write('<a href="http://go.cloudmatic.de/edit-data" target="_blank" class="waves-effect waves-light btn blue">');</script><i class="material-icons left">mode_edit</i>Daten bearbeiten</a>
            </div>
          </div>
        </div>
        <!-- /Account Data -->
  }
# check if user has no valid complete/FullService
if {$smarthomeliz == "Fehler beim Pr&uuml;fen der Lizenz oder keine Lizenz gebucht" || $smarthometype == "CloudMatic SmartHome"} {
  puts {
        <!-- CloudMatic Connect -->
        <div class="col s12 m6">
          <div class="card white">
            <div class="card-content black-text">
              <span class="card-title">CloudMatic Connect</span>
              <p>
                Fernzugriff: <script>document.write('<a href="https://'+userid+'.'+base_url+'" target="_blank">');</script>https://<script>document.write(userid);</script>.<script>document.write(base_url);</script></a><br>
                Laufzeit:
  }
  puts "$key"
  puts {
                <br>
              </p>
            </div>
            <div class="card-action">
              <script>document.write('<a href="http://go.cloudmatic.de/order-cloudmatic-connect" target="_blank" class="waves-effect waves-light btn blue">');</script><i class="material-icons left">shopping_cart</i>Zugang buchen</a>
            </div>
          </div>
        </div>
        <!-- /CloudMatic Connect -->
  }
  if {$smarthomeliz != "Fehler beim Pr&uuml;fen der Lizenz oder keine Lizenz gebucht" && $smarthometype == "CloudMatic SmartHome"} {
    puts {
        <!-- CloudMatic SmartHome -->
        <div class="col s12 m6">
          <div class="card white">
            <div class="card-content black-text">
              <span class="card-title">CloudMatic SmartHome</span>
              <p>
                Oberfl&auml;che: <script>document.write('<a href="https://'+userid+'.cloud-matic.net" target="_blank">');</script>https://<script>document.write(userid);</script>.cloud-matic.net</a><br>
                Laufzeit: 
  }
  puts "$smarthomeliz"
  puts {
              </p>
            </div>
            <div class="card-action">
              <script>document.write('<a href="http://go.cloudmatic.de/order-cloudmatic-smarthome" target="_blank" class="waves-effect waves-light btn blue">');</script><i class="material-icons left">shopping_cart</i>Zugang buchen</a>
            </div>
          </div>
        </div>
    }
  }
} else {
  puts {
        <!-- CloudMatic Complete / FullService -->
        <div class="col s12 m6">
          <div class="card white">
            <div class="card-content black-text">
              <span class="card-title">
  }
  if {$smarthometype == "TESTZUGANG CloudMatic Complete" || $smarthometype == "TESTZUGANG CloudMatic complete"} {
    puts "CloudMatic Complete <sup><small>Testzugang</small></sup>"
  } else { 
    puts "$smarthometype"
  } 
  puts { </span>
              <p>
                Fernzugriff: <script>document.write('<a href="https://'+userid+'.'+base_url+'" target="_blank">');</script>https://<script>document.write(userid);</script>.<script>document.write(base_url);</script></a><br>
                Oberfl&auml;che: <script>document.write('<a href="https://'+userid+'.cloud-matic.net" target="_blank">');</script>https://<script>document.write(userid);</script>.cloud-matic.net</a><br>
                Laufzeit:
  }
  puts "$key"
  puts {
                <br>
              </p>
            </div>
            <div class="card-action">
  }
  if {$smarthometype == "CloudMatic Complete" || $smarthometype == "TESTZUGANG CloudMatic Complete" || $smarthometype == "CloudMatic complete" || $smarthometype == "TESTZUGANG CloudMatic complete"} {
    puts {
              <script>document.write('<a href="http://go.cloudmatic.de/order-cloudmatic-complete" target="_blank" class="waves-effect waves-light btn blue">');</script><i class="material-icons left">shopping_cart</i>Zugang buchen</a>
    }
  }
  if {$smarthometype == "CloudMatic FullService"} {
    puts {
              <script>document.write('<a href="http://go.cloudmatic.de/order-cloudmatic-fullservice" target="_blank" class="waves-effect waves-light btn blue">');</script><i class="material-icons left">shopping_cart</i>Zugang buchen</a>
    }
  }
  puts {
            </div>
          </div>
        </div>
        <!-- /CloudMatic Complete / FullService -->
  }
}
  puts {
        <!-- CloudMatic NotifyMe -->
        <div class="col s12 m6">
          <div class="card white">
            <div class="card-content black-text">
              <span class="card-title">Ihr Guthaben</span>
              <p>
                Guthaben Standard SMS: <script>document.write(ssms);</script><br>
                Guthaben Premium SMS: <script>document.write(psms);</script><br>
              </p>
            </div>
            <div class="card-action">
              <script>document.write('<a href="http://go.cloudmatic.de/order-cloudmatic-notifyme" target="_blank" class="waves-effect waves-light btn blue">');</script><i class="material-icons left">shopping_cart</i>Guthaben buchen</a>
            </div>
          </div>
        </div>
        <!-- /CloudMatic NotifyMe -->

      </div>
      <!-- /Status Cards -->
    </div>
	}
	#<!-- Ende Tab 1 -->
	#<!-- Ende User hat Konto -->
puts {
  <div id="check" class="cm-content" style="display:none;">
    <div class="row">
      <div class="col s12">
        <h4>Funktionspr&uuml;fung</h4>
        Hier haben Sie die M&ouml;glichkeit eine Funktionspr&uuml;fung der CloudMatic Installation / Dienste durchzuf&uuml;hren.
      </div>
    </div>
    <div class="row">
      <div class="col s12">
        <p>
          <a href="dotest.cgi" target="_blank" class="waves-effect waves-light btn blue"><i class="material-icons left">build</i>Diagnose starten</a><br><br>
          <a href="dotest2.cgi" target="_blank" class="waves-effect waves-light btn blue"><i class="material-icons left">build</i>erweiterte Diagnose starten</a>
        </p>
      </div>
    </div>
  </div>
}


#<!-- Beginn Tab 3 -->
	
set dienst unknown
set content [::HomeMatic::Util::LoadFile "/etc/config/addons/mh/dienst"]
catch { [regexp -line {(.*)} $content dummy dienst] }
set dienstngx unknown
set content [::HomeMatic::Util::LoadFile "/etc/config/addons/mh/dienstngx"]
catch { [regexp -line {(.*)} $content dummy dienstngx] }
set dienstzbx unknown
set content [::HomeMatic::Util::LoadFile "/etc/config/addons/mh/dienstzbx"]
catch { [regexp -line {(.*)} $content dummy dienstzbx] }

puts {
  <div class="cm-content" id="services" style="display:none;">
    <div class="row">
      <div class="col s12">
        <h4>Dienststatus</h4>Hier haben Sie einen &Uuml;berblick auf die CloudMatic Dienste der CCU.
      </div>
    </div>
    <div class="row">
      <div class="col s12">
        <div class="row">
          <div class="col s4">
            <img src="img/cmvpn.png" alt="CloudMatic Connect" class="responsive-img">
          </div>
          <div class="col s8">
            <h6>CloudMatic VPN Zugang</h6>
}
if {$dienst == 0} {
  puts {
          Der VPN Dienst ist nicht gestartet, <br>VPN Zugang ist nicht aktiv<br>
          <br>
          <a href="dienstan.cgi" class="waves-effect waves-light btn blue startservice" data-type="vpn"><i class="material-icons left">check_box</i>Dienst starten</a>
  }
} else {
  puts {
          Der VPN Dienst ist gestartet, <br>VPN Zugang kann genutzt werden<br>
          <br>
          <a href="dienstaus.cgi" class="waves-effect waves-light btn blue stopservice" data-type="vpn"><i class="material-icons left">cancel</i>Dienst beenden</a>
  }
}
puts {
          </div>
        </div>
      </div>
    </div>
    <div class="divider"></div>
    <div class="row">
      <div class="col s12">
        <h4>Zusatzdienste</h4>
      </div>
    </div>
    <div class="row">
      <div class="col s12">
        <h6>Reverse Proxy</h6>
}
if {$dienstngx == 0} {
  puts {
        Der Reverse Proxy Dienst ist nicht gestartet, erweiterte CloudMatic Dienste sind nicht aktiv.<br><br>
        <a href="dienstanngx.cgi" class="waves-effect waves-light btn blue startservice" data-type="nginx"><i class="material-icons left">check_box</i>Dienst starten</a>
  }
} else {
  puts {
        Der Reverse proxy Dienst ist gestartet, erweiterte CloudMatic Dienste k&ouml;nnen genutzt werden.<br><br>
        <a href="dienstausngx.cgi" class="waves-effect waves-light btn blue stopservice" data-type="nginx"><i class="material-icons left">cancel</i>Dienst beenden</a>
  }
}
puts {
      </div>
    </div>
<!--    <div class="divider"></div>
    <div class="row">
      <div class="col s12">
        <h6>CloudMatic monitoring</h6>
}
if {$dienstzbx == 0} {
  puts {
        Der CloudMatic monitoring Dienst ist nicht gestartet, System&uuml;berwachung aus der Cloud ist nicht aktiv.<br><br>
       <a href="dienstanzbx.cgi" class="waves-effect waves-light btn blue startservice" data-type="zbx"><i class="material-icons left">check_box</i>Dienst starten</a>
  }
} else {
  puts {
        Der CloudMatic monitoring Dienst ist gestartet, System&uuml;berwachung aus der Cloud kann genutzt werden.<br><br>
        <a href="dienstauszbx.cgi" class="waves-effect waves-light btn blue stopservice" data-type="zbx"><i class="material-icons left">cancel</i>Dienst beenden</a>
  }
}
puts {
      </div>
    </div> -->
  </div>
}

#<!-- Beginn Tab 6 -->
set autoupdate unknown
set content [::HomeMatic::Util::LoadFile "/etc/config/addons/mh/autoupdate"]
catch { [regexp -line {(.*)} $content dummy autoupdate] }
puts {
  <div id="update" class="cm-content" style="display:none;">
    <div class="row">
      <div class="col s12">
        <h4>Updates</h4>
      </div>
    </div>
    <div class="row">
      <div class="col s12">
	      <h6>Status automatische Updates</h6>
}
if {$autoupdate == 0} {
	puts {
		    Automatische Updates sind nicht aktiviert. Updates m&uuml;ssen manuell eingespielt werden.<br><br>
		    <a href="autoupdatean.cgi" class="waves-effect waves-light btn blue startupdate"><i class="material-icons left">check_box</i>Automatische Updates aktivieren</a>
	}
} else {
	puts {
		    Automatische Updates sind aktiv, die Pr&uuml;fung erfolgt mehrmals t&auml;glich.<br><br>
		    <a href="autoupdateaus.cgi" class="waves-effect waves-light btn blue stopupdate"><i class="material-icons left">cancel</i>Automatische Updates deaktivieren</a>
	}
}
puts {
      </div>
    </div>
    <div class="row">
      <div class="col s12">
			  <h6>Manuelles Update</h6>
			  <a href="doupdate.cgi" class="waves-effect waves-light btn blue manualupdate"><i class="material-icons left">update</i>Manuelles Update starten</a>
      </div>
    </div>
  </div>
}
#<!-- Ende Tab 6 -->

#<!-- Beginn Tab 7 -->
puts {
  <div id="remove" class="cm-content" style="display:none;">
    <div class="row">
      <div class="col s12">
        <h4>Pers&ouml;nliche Daten l&ouml;schen</h4>
        Hier k&ouml;nnen Sie die pers&ouml;nlichen Daten der CloudMatic Installation l&ouml;schen.
      </div>
    </div>
    <div class="row">
      <div class="col s12">
        <p>
		      Sie m&ouml;chten Ihre CCU einschicken oder verkaufen und deshalb Ihre pers&ouml;nlichen CloudMatic Daten l&ouml;schen?<br>
          Oder Sie haben sich gegen eine weitere Nutzung der Vorteile von CloudMatic entschieden?
        </p>
        <p>
          Sie haben hier die M&ouml;glichkeit alle personifizierten Daten von der CCU zu l&ouml;schen. Die Daten k&ouml;nnen bei einem 
          bestehenden CloudMatic Konto mittels Key-Update wiederhergestellt werden.
        </p>
			  <a href="#!" class="waves-effect waves-light btn blue" id="delete"><i class="material-icons left">delete_forever</i>Daten l&ouml;schen</a>
		  </div>
    </div>
  </div>
}
#<!-- Ende Tab 7 -->
}	
#<!-- Beginn Tab 8 -->
puts {
  <div id="support" class="cm-content" style="display:none;">
    <div class="row">
      <div class="col s12">
        <h4>Support</h4>
          <p>
            Wir bieten Ihnen E-Mail-Support, eine Telefonsupport-Hotline mit hilfsbereiten Mitarbeitern und eine schnelle Bearbeitung Ihrer Anliegen via Ticketsystem. 
            Oder Sie nutzen unsere umfangreiche Knowledge Base, hier finden Sie ganz bequem und unkompliziert Antworten und Hilfestellungen auf die gängigsten Fragen.
          </p>
      </div>
    </div>
    
    <div class="row">
            
      <div class="col s12 m12">                  
        <div class="card white">
        
            <div class="card-content black-text">
              <span class="card-title">Knowledge Base</span>
              <p>
                In unserer Knowledge Base finden Sie Anleitungen und How-to-Guides zu unseren Produkten, Antworten auf die gängigsten Fragen und praktische Anwendungsbeispiele für verschiedene Nutzungszwecke.
              </p>
            </div>
                        
            <div class="card-action">
                <script>document.write('<a href="http://kb.easy-smarthome.de/Start" target="_blank" class="waves-effect waves-light btn blue">');</script><i class="material-icons left">live_help</i>Zur Knowledge Base</a>
            </div>
              
        </div>           
      </div><!-- col s12 m12 -->
    
    </div><!-- row -->

    <div class="row">
        
      <div class="col s12 m6">                  
        <div class="card white">
        
            <div class="card-content black-text">
              <span class="card-title">Telefonsupport-Hotline</span>
              <p>
                Unsere Knowledge Base konnte Ihnen nicht weiterhelfen und Sie wünschen sich telefonische Hilfestellung bei einer technischen Angelegenheit?
                <br><br>
                Kein Problem, unser Support-Team steht Ihnen Montags bis Freitags von 10:00 - 12:00 Uhr und 13:00 - 17:00 Uhr zur Verfügung.
              </p>
            </div>
                        
            <div class="card-action">
              <span class="h4blue">+49 (0)2921 / 370 380</span>
            </div>
              
        </div>           
      </div><!-- col s12 m6 -->
      
      <div class="col s12 m6">                  
        <div class="card white">
        
            <div class="card-content black-text">
              <span class="card-title">E-Mail-Support</span>
              <p>
                Senden Sie uns Ihre technischen Fragen oder Supportwünsche. 
                Um Rückfragen zu vermeiden, beschreiben Sie ihr Anliegen so genau wie möglich. Das erspart Ihnen mögliche Rückfragen und gewährleistet eine schnelle Bearbeitung Ihres Anliegens. Unsere Mitarbeiter melden sich schnellstmöglich bei Ihnen.
              </p>
            </div>
                        
            <div class="card-action">
                <script>document.write('<a href="https://support.easy-smarthome.de/supportrequest.html" target="_blank" class="waves-effect waves-light btn blue">');</script><i class="material-icons left">content_paste</i>Supportanfrage stellen</a>
            </div>
              
        </div>           
      </div><!-- col s12 m6 -->
    
    </div><!-- row -->
    
    <div class="row">
            
      <div class="col s12 m12">                  
        <div class="card white">
        
            <div class="card-content black-text">
              <span class="card-title">Unsere Supportleistungen</span>
              <p>
                Sie planen ein Smarthome wissen aber nicht so recht, wie Sie beginnen sollen bzw. welche Geräte Sie benötigen? 
                Wir unterstützen Sie gerne bei Ihrem Vorhaben! Sie wählen die Funktionen, wir finden herstellerunabhängig die beste Smarthome-Technik für Sie.                
              </p>
              <ul>
              <li>Planung und Vorkonfiguration von Smarthome Installationen</li>
              <li>Individuelle Smarthome Programmierungen</li>
              <li>Konfiguration von Zentralen und Gateways</li>
              <li>Einrichtungen nach Vorgabe</li>
              </ul>
            </div>
                        
            <div class="card-action">
                <script>document.write('<a href="https://support.easy-smarthome.de/" target="_blank" class="waves-effect waves-light btn blue">');</script><i class="material-icons left">info</i>Mehr dazu im Support Center</a>
            </div>
              
        </div>           
      </div><!-- col s12 m12 -->
    
    </div><!-- row -->
    
  </div>
}

#<!-- Ende Tab 8 -->

#<!-- Ende Dokument -->
puts {
	</div>
  </div>
</main>
<footer class="page-footer light-blue darken-4">
  <div class="container">
    <div class="row">
      <div class="col l4 s12">
        <h5 class="white-text">Kontakt</h5>
        <p class="grey-text text-lighten-4">
          EASY SmartHome GmbH<br>
          Neuer Weg 1<br>
          59505 Bad Sassendorf<br>
          <br>
          <a href="#!" class="cm-nav grey-text text-lighten-4" style="text-decoration:underline;" data-content="support">Support erhalten</a>
        </p>
      </div>
      <div class="col l8 s12">
        <h5 class="white-text">CloudMatic <sup>by EASY SmartHome GmbH</sup></h5>
        <p class="grey-text text-lighten-4">
          &Uuml;ber CloudMatic erhalten Sie einen sicheren Fernzugriff auf Ihre Haussteuerung.
          Greifen Sie &uuml;ber das Internet auf Ihre Haussteuerung zu - ganz ohne Portweiterleitungen, Firewallfreischaltungen, DynDNS Einrichtungen. etc.
          <br><br>
          <a href="http://go.cloudmatic.de/products" class="grey-text text-lighten-4" target="_blank" style="text-decoration:underline;">Komplette CloudMatic Produkt&uuml;bersicht</a>
        </p>
      </div>
    </div>
  </div>
  <div class="footer-copyright">
    <div class="container">
    Copyright &copy; <script>document.write(jahr);</script> by <a href="http://www.easy-smarthome.de" target="_blank" class="white-text">EASY SmartHome GmbH</a>
    </div>
  </div>
</footer>
<div id="service_modal_attention" class="modal">
  <div class="modal-content">
    <span id="service_modal_attention_headline"></span>
  </div>
  <div class="modal-footer">
    <a href="dienstaus.cgi" class="waves-effect waves-light btn red stopservice">Dienst beenden</a>&nbsp;&nbsp;&nbsp;
    <a href="" class="modal-submit modal-action modal-close waves-effect waves-blue btn-flat">Abbrechen</a>
  </div>
</div>
<div id="service_modal" class="modal">
  <div class="modal-content">
    <span id="service_modal_headline"></span>
    <span id="serviceresult" style="display:none;"></span>
    <div class="center-align" id="spinner">
      <div class="preloader-wrapper big active">
        <div class="spinner-layer spinner-blue-only">
          <div class="circle-clipper left">
            <div class="circle"></div>
          </div><div class="gap-patch">
            <div class="circle"></div>
          </div><div class="circle-clipper right">
            <div class="circle"></div>
          </div>
        </div>
      </div>
    </div>
  </div>
  <div class="modal-footer">
    <a href="" class="modal-submit modal-action modal-close waves-effect waves-blue btn-flat">Ok</a>
  </div>
</div>
<div id="delete_modal" class="modal">
  <div id="predelete">
    <div class="modal-content">
      <h6>Sind Sie sicher?</h6>
      Nach dem Entfernen der personifizierten Daten werden s&auml;mtliche CloudMatic Dienste deaktiviert und k&ouml;nnen
      nicht mehr Verwendet werden.
    </div>
    <div class="modal-footer">
      <a href="#!" class="modal-submit modal-action waves-effect waves-blue btn-flat" id="dodelete">Daten wirklich l&ouml;schen</a>
      &nbsp;&nbsp;&nbsp;
      <a href="#!" class="modal-submit modal-action modal-close waves-effect waves-blue btn-flat">Abbrechen</a>
    </div>
  </div>
  <div id="postdelete" style="display:none;">
    <div class="modal-content">
      <h6>Daten werden gel&ouml;scht</h6>
      Bitte haben Sie einen Moment Geduld ...
      <span id="deleteresult"></span>
      <div class="center-align" id="deletespinner">
        <div class="preloader-wrapper big active">
          <div class="spinner-layer spinner-blue-only">
            <div class="circle-clipper left">
              <div class="circle"></div>
            </div><div class="gap-patch">
              <div class="circle"></div>
            </div><div class="circle-clipper right">
              <div class="circle"></div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="modal-footer">
      <a href="index.cgi" class="modal-submit modal-action modal-close waves-effect waves-blue btn-flat postdelete" style="display:none";>Ok</a>
      &nbsp;
    </div>
  </div>
</div>
<script type="text/javascript" src="js/jquery-2.2.1.min.js"></script>
<script type="text/javascript" src="js/materialize.min.js"></script>
<script type="text/javascript" src="js/cloudmatic.js"></script>
</body>
</html>
}
