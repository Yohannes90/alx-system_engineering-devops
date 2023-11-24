# Install flask from pip3, using Puppet

package { 'Werkzeug':
    ensure   => '2.2.2',
    provider => 'pip3'
}

package { 'flask':
    ensure   => '2.1.0',
    provider => 'pip3'
}
