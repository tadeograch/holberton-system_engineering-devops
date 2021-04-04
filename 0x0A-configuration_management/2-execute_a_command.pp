# Kills a proces named killmenow, using exec

exec { 'killmenow':
    command  => 'pkill -f killmenow'
    provider => 'shell'
}
