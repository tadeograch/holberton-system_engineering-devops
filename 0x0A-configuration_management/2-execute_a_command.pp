# Kills a proces named killmenow, using exec

exec { 'killmenow':
    command  => 'pkill killmenow'
    provider => 'shell'
}
