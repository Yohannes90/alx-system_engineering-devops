# configuration so that it is possible to login with the holberton user and open a file without any error message

# increase soft file limit for Holberton user to login
exec { 'increase-hard-limit':
  provider => shell,
  command  => 'sed -i "/^holberton hard/s/5/50000/" /etc/security/limits.conf',
  path     => '/usr/local/bin/:/bin/',
}

# increase soft file limit for Holberton user to login
exec {'increase-soft-limit':
  provider => shell,
  command  => 'sed -i "/^holberton soft/s/4/40000/" /etc/security/limits.conf',
  path     => '/usr/local/bin/:/bin/',
}
