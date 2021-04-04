# Kills a proces named killmenow, using exec

exec { 'pkill':
    command  => 'pkill -f killmenow'
    provider => 'shell'
}
