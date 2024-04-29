# Puppet to make changes to our configuration file
# set up your client SSH configuration file to connect to a server
# without typing a password.

file_line { 'Turn off passwd auth':
  ensure => present,
  line   => 'PasswordAuthentication n',
  path   => '/etc/ssh/ssh_config',
}

file_line { 'Set identify file':
  ensure => present,
  line   => 'IdentityFile ~/.ssh/school',
  path   => '/etc/ssh/ssh_config',
}
