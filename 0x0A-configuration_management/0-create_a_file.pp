# Creates the file holberton in /tmp using Puppet

file { 'holberton':
    path    => '/tmp/holberton',
    mode    => '0744',
    owner   => 'www-data',
    group   => 'www-data',
    content => 'I love Puppet',
}
