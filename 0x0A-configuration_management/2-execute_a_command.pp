# Kill a script called killmenow
exec { 'pkill -f killmenow':
path => '/usr/bin',
}
