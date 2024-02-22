# inclrease the amount of traffic nginx can handle

# increase the default ULIMIT of nginx from 15 to 4096
exec { 'replace':
  command => '/bin/sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/',
  before  => Exec['restart-nginx'],
}

# restart nginx service
exec { 'restart-nginx':
  command => '/etc/init.d/nginx restart',
  path    => '/etc/init.d/',
}
