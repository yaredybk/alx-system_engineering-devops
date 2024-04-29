# Puppet to make changes to our configuration file
# set up your client SSH configuration file to connect to a server
# without typing a password.

file_line { 'Turn off passwd auth':
  path => '/etc/ssh/ssh_config',
  line => 'PasswordAuthentication n',
  ensure => present,
}

file_line { 'Set identify file':
  path => '/etc/ssh/ssh_config',
  line => 'IdentityFile ~/.ssh/school',
  ensure => present,
}
