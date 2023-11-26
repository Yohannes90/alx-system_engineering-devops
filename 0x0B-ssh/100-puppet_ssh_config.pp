# using Puppet to make changes to our configuration file
include stdlib

file_line { 'authenticate without password':
    ensure => present,
    path   => '/etc/ssh/ssh_config',
    line   => 'PasswordAuthentication no'
}

file_line { 'use the private key':
    ensure => present,
    path   => '/etc/ssh/ssh_config',
    line   => 'IdentityFile ~/.ssh/school'
}
