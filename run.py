import sys

base = '''
$TTL 60
@            IN    SOA  localhost. root.localhost.  (
                          2015112501   ; serial
                          1h           ; refresh
                          30m          ; retry
                          1w           ; expiry
                          30m)         ; minimum
                   IN     NS    localhost.

'''

import json

with open('config.json','r') as f:
    config = json.loads(f.read())

with open('/etc/bind/db.dnas.rpz', 'w') as f:
    f.write(base)
    for host, ip in config.items():
        f.write('{}    A        {}\n'.format(host, ip))


base = '''
//
// Do any local configuration here
//

// Consider adding the 1918 zones here, if they are not used in your
// organization
//include "/etc/bind/zones.rfc1918";

zone "rpz" {
  type master;
  file "/etc/bind/db.dnas.rpz";
};
'''

with open('/etc/bind/named.conf.local','w') as f:
    f.write(base)

base = '''
options {
	directory "/var/cache/bind";

	// If there is a firewall between you and nameservers you want
	// to talk to, you may need to fix the firewall to allow multiple
	// ports to talk.  See http://www.kb.cert.org/vuls/id/800113

	// If your ISP provided one or more IP addresses for stable
	// nameservers, you probably want to use them as forwarders.
	// Uncomment the following block, and insert the addresses replacing
	// the all-0's placeholder.

	// forwarders {
	// 	0.0.0.0;
	// };

	//========================================================================
	// If BIND logs error messages about the root key being expired,
	// you will need to update your keys.  See https://www.isc.org/bind-keys
	//========================================================================
	dnssec-validation auto;

	auth-nxdomain no;    # conform to RFC1035
	listen-on-v6 { any; };

	allow-query { any; };

	response-policy { zone "rpz"; };
};
'''

with open('/etc/bind/named.conf.options','w') as f:
    f.write(base)


base = '''
<IfModule mod_ssl.c>

<VirtualHost *:443>
	SSLEngine on
	SSLCipherSuite ALL
	SSLCertificateFile    /etc/dnas/cert-us.pem
	SSLCertificateKeyFile /etc/dnas/cert-us-key.pem
	SSLCertificateChainFile /etc/dnas/ca-cert.pem

	ServerName gate1.us.dnas.playstation.org
	ServerAlias gate1.us.dnas.playstaion.org

	ServerAdmin webmaster@localhost

	DocumentRoot /var/www/dnas
	<Directory />
		Options FollowSymLinks
		AllowOverride None
	</Directory>

	<Directory "/var/www/dnas">
		Options -Indexes
		Order allow,deny
		Allow from all
	</Directory>

	# needed because of linknames being non-php
	<FilesMatch "v2.5_i-connect">
		SetHandler application/x-httpd-php
	</FilesMatch>
	<FilesMatch "v2.5_others">
		SetHandler application/x-httpd-php
	</FilesMatch>

	# Possible values include: debug, info, notice, warn, error, crit,
	# alert, emerg.
	LogLevel warn

	<FilesMatch "\.(cgi|shtml|phtml|php)$">
		SSLOptions +StdEnvVars
	</FilesMatch>
	<Directory /usr/lib/cgi-bin>
		SSLOptions +StdEnvVars
	</Directory>

	BrowserMatch "MSIE [2-6]" \
		nokeepalive ssl-unclean-shutdown \
		downgrade-1.0 force-response-1.0
	# MSIE 7 and newer should be able to use keepalive
	BrowserMatch "MSIE [17-9]" ssl-unclean-shutdown

</VirtualHost>

<VirtualHost *:443>
	SSLEngine on
	SSLCipherSuite ALL
	SSLCertificateFile    /etc/dnas/cert-jp.pem
	SSLCertificateKeyFile /etc/dnas/cert-jp-key.pem
	SSLCertificateChainFile /etc/dnas/ca-cert.pem

	ServerName gate1.jp.dnas.playstation.org
	ServerAlias gate1.jp.dnas.playstaion.org

	ServerAdmin webmaster@localhost

	DocumentRoot /var/www/dnas
	<Directory />
		Options FollowSymLinks
		AllowOverride None
	</Directory>

	<Directory "/var/www/dnas">
		Options -Indexes
		Order allow,deny
		Allow from all
	</Directory>

	# proxy to login page
    <Location /00000040/>
        ProxyPass http://login/
        SetEnv force-proxy-request-1.0 1
        SetEnv proxy-nokeepalive 1
    </Location>

	# needed because of linknames being non-php
	<FilesMatch "v2.5_i-connect">
		SetHandler application/x-httpd-php
	</FilesMatch>
	<FilesMatch "v2.5_others">
		SetHandler application/x-httpd-php
	</FilesMatch>

	# Possible values include: debug, info, notice, warn, error, crit,
	# alert, emerg.
	LogLevel warn

	<FilesMatch "\.(cgi|shtml|phtml|php)$">
		SSLOptions +StdEnvVars
	</FilesMatch>
	<Directory /usr/lib/cgi-bin>
		SSLOptions +StdEnvVars
	</Directory>

	BrowserMatch "MSIE [2-6]" \
		nokeepalive ssl-unclean-shutdown \
		downgrade-1.0 force-response-1.0
	# MSIE 7 and newer should be able to use keepalive
	BrowserMatch "MSIE [17-9]" ssl-unclean-shutdown

</VirtualHost>

<VirtualHost *:443>
	SSLEngine on
	SSLCipherSuite ALL
	SSLCertificateFile    /etc/dnas/cert-eu.pem
	SSLCertificateKeyFile /etc/dnas/cert-eu-key.pem
	SSLCertificateChainFile /etc/dnas/ca-cert.pem

	ServerName gate1.eu.dnas.playstation.org
	ServerAlias gate1.eu.dnas.playstaion.org

	ServerAdmin webmaster@localhost

	DocumentRoot /var/www/dnas
	<Directory />
		Options FollowSymLinks
		AllowOverride None
	</Directory>

	<Directory "/var/www/dnas">
		Options -Indexes
		Order allow,deny
		Allow from all
	</Directory>

	# needed because of linknames being non-php
	<FilesMatch "v2.5_i-connect">
		SetHandler application/x-httpd-php
	</FilesMatch>
	<FilesMatch "v2.5_others">
		SetHandler application/x-httpd-php
	</FilesMatch>

	# Possible values include: debug, info, notice, warn, error, crit,
	# alert, emerg.
	LogLevel warn

	<FilesMatch "\.(cgi|shtml|phtml|php)$">
		SSLOptions +StdEnvVars
	</FilesMatch>
	<Directory /usr/lib/cgi-bin>
		SSLOptions +StdEnvVars
	</Directory>

	BrowserMatch "MSIE [2-6]" \
		nokeepalive ssl-unclean-shutdown \
		downgrade-1.0 force-response-1.0
	# MSIE 7 and newer should be able to use keepalive
	BrowserMatch "MSIE [17-9]" ssl-unclean-shutdown

</VirtualHost>

</IfModule>
'''

with open('/etc/apache2/sites-available/dnas.conf','w') as f:
    f.write(base)
