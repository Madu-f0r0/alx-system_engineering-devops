# Manifest kills a process named `killmenow`

exec { 'kill_killmenow':
  command => 'pkill killmenow',
  path    => '/bin:/usr/bin',
  onlyif  => 'pgrep killmenow',
}
