# fixes wrong extention name 'phpp' to 'php' in wp-settings

exec {'fix-wordpress':
	command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
	path    => '/usr/local/bin/:/bin/'
}
