# Manifest kills a process named `killmenow`

exec { 'pkill killmenow':
  path => '/bin:/usr/bin',
  onlyif => 'pgrep killmenow',
}
